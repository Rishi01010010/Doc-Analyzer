from flask import Flask, render_template, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
import language_tool_python
import google.generativeai as genai
from gtts import gTTS
from dotenv import load_dotenv
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['AUDIO_FOLDER'] = 'audio'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload and audio folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

# Load environment variables and configure Gemini
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# Setup generation configuration
generation_config = {
    "temperature": 0.5,
    "max_output_tokens": 200,
    "response_mime_type": "text/plain",
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Save the uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text
            extracted_text = extract_text(filepath)
            
            # Correct text
            corrected_text = correct_text(extracted_text)
            
            # Summarize text
            summarized_text = summarize_text_with_gemini(corrected_text)
            
            # Generate audio file for summarized text
            audio_filename = generate_audio(summarized_text)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return jsonify({
                'extracted_text': extracted_text,
                'corrected_text': corrected_text,
                'summarized_text': summarized_text,
                'audio_filename': audio_filename
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/audio/<filename>')
def get_audio(filename):
    try:
        return send_file(
            os.path.join(app.config['AUDIO_FOLDER'], filename),
            mimetype='audio/mp3'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def extract_text(image_path):
    """Extract text from image using pytesseract"""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def correct_text(input_text):
    """Correct text using LanguageTool"""
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(input_text)
    return language_tool_python.utils.correct(input_text, matches)

def summarize_text_with_gemini(text):
    """Summarize text using Gemini"""
    summary_prompt = f"Refer and analyze the given text and draw a simple summary out of this text in simpler words:\n\n{text}"
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)
    chat_session = model.start_chat(history=[])
    summary_response = chat_session.send_message(summary_prompt)
    return summary_response.text

def generate_audio(text):
    """Generate audio file from text using gTTS"""
    # Generate unique filename
    audio_filename = f"audio_{uuid.uuid4()}.mp3"
    audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
    
    # Create gTTS object and save to file
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)
    
    # Clean up old audio files
    cleanup_old_audio_files()
    
    return audio_filename

def cleanup_old_audio_files():
    """Clean up audio files older than 1 hour"""
    import time
    current_time = time.time()
    audio_folder = app.config['AUDIO_FOLDER']
    
    for filename in os.listdir(audio_folder):
        filepath = os.path.join(audio_folder, filename)
        # If file is older than 1 hour (3600 seconds)
        if os.path.getmtime(filepath) < current_time - 3600:
            try:
                os.remove(filepath)
            except:
                pass

if __name__ == '__main__':
    app.run(debug=True)