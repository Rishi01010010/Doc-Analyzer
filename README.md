# 📄 Doc Analyzer: Simplifying Legal Documents 📄

Welcome to *Doc Analyzer*, an innovative AI-powered tool developed by students at SAI Vidya Institute of Technology, Bengaluru, under the guidance of Prof. Salma Itagi. Submitted as part of the Visvesvaraya Technological University’s AI Mini Project (BCS515B) for the 2024-25 academic year, this project transforms complex legal documents into clear, concise summaries accessible to non-experts. Leveraging Optical Character Recognition (OCR), Natural Language Processing (NLP), and grammar correction, Doc Analyzer empowers users across various sectors with informed decision-making.

## 🔍 Project Overview

Legal documents often pose challenges due to their specialized language and structure, leading to misunderstandings and dependency on legal professionals. *Doc Analyzer* addresses this by extracting text from scanned documents, correcting errors, and summarizing content into layman-friendly language. With an intuitive interface and robust backend, it democratizes access to legal knowledge, applicable in legal aid, real estate, healthcare, education, and finance.

### ✨ Key Features:

- *Text Extraction:* Uses OCR to digitize scanned legal documents.
- *Grammar Correction:* Refines extracted text for accuracy.
- *Text Summarization:* Converts complex legal jargon into simple summaries.
- *User-Friendly Interface:* Web-based UI for easy access.
- *Scalability:* Designed to handle large volumes of documents.

## 🚀 Getting Started

### 1. *Prerequisites:*
- Python 3.x installed on your system.
- Required libraries: Tesseract-OCR, PyTorch, Flask, and NLP libraries (e.g., transformers).
- Tesseract-OCR installed and added to system PATH.
- A system with at least 8 GB RAM and a multi-core processor.

### 2. *Setting Up:*

- Clone the repository (if hosted on GitHub):
  ```bash
  git clone https://github.com/your-username/Doc_Analyzer.git
  cd Doc_Analyzer
  ```

- Install dependencies:
  ```bash
  pip install flask pytesseract torch transformers pillow
  ```

- Configure environment:
  - Create a `.env` file with necessary API keys or paths (e.g., Tesseract path).
  - Ensure Tesseract-OCR is installed (e.g., `sudo apt install tesseract-ocr` on Linux).

- Place sample documents:
  - Add scanned documents (e.g., `agreement.jpg`, `fees.jpg`) in the root directory or `uploads/` folder.

### 3. *Running the System:*

- Run the Flask application:
  ```bash
  python app.py
  ```

- Open a web browser and navigate to `http://127.0.0.1:5000/` to access the interface.
- Upload a scanned document (e.g., `agreement.jpg`) and view the summarized output.

### 4. *Sample Output:*
- **Input:** Scanned receipt (`fees.jpg`).
- **Output:**
  ```
  Summarized Text:
  This is a receipt from the Salvador Institute of Technology in Bangalore, India. Bishkek R, a Computer Science student (ID 22/CSE/063), paid 11,834 (Eleven Thousand Eight Hundred and Thirty-Four Rupees) on February 7, 2024, for tuition and other fees for the 2023-24 academic year. The payment was made via RTGS. Some fee details are unclear/missing on the receipt.
  ```

## 💾 Directory Structure

```
Doc_Analyzer/
│
├── .env                   # Environment variables (e.g., Tesseract path)
├── agreement.jpg          # Sample legal document
├── app.py                 # Main Flask application
├── fees.jpg               # Sample receipt document
├── README.md              # Project documentation
│
├── .dist/                 # Distribution files (empty or unused)
│
├── dummy/                 # Development/testing files
│   ├── app1.html          # Sample HTML template
│   ├── app1.py            # Test Python script
│   ├── dummy.py           # Test script
│   ├── dummy1.css         # Test CSS file
│   └── dummy2.css         # Test CSS file
│
├── static/                # Static files
│   └── style.css          # CSS for the web interface
│
├── templates/             # HTML templates
│   └── index.html         # Main web interface template
│
└── uploads/               # Directory for uploaded documents
```

### 📝 Code Explanation

1. **app.py**:
   - Implements the Flask server to handle document uploads.
   - Integrates OCR (Tesseract) for text extraction, NLP for summarization, and grammar correction.
   - Renders results via the `index.html` template.

2. **static/style.css**:
   - Styles the web interface for a user-friendly experience.

3. **templates/index.html**:
   - Provides the upload form and displays summarized text.

## 🌐 System Design

- **Input:** Scanned documents (e.g., PDFs, images).
- **Processing Pipeline:** OCR → Grammar Correction → Summarization.
- **Output:** Clear, concise summaries displayed via a web interface.
- **Architecture:** Combines OCR tools, NLP models, and a Flask-based frontend.

## 🛠️ How It Works

1. *Text Extraction:* Uses Tesseract-OCR to convert scanned images into digital text.
2. *Grammar Correction:* Applies NLP techniques to correct spelling and grammar errors.
3. *Summarization:* Employs transformer models to simplify legal text into layman terms.
4. *User Interface:* Displays results through a web browser, ensuring accessibility.

## 🎯 Project Intent

*Doc Analyzer* aims to bridge the gap between legal professionals and the public by simplifying complex documents. It reduces dependency on legal experts, promotes transparency, and has potential applications in diverse sectors, making legal knowledge accessible to all.

## 🔧 Customization

Enhance the project with these ideas:
- *Multilingual Support:* Add translation capabilities for non-English documents.
- *Advanced Summarization:* Integrate larger language models (e.g., GPT-based).
- *Batch Processing:* Enable analysis of multiple documents simultaneously.
- *Mobile App:* Develop a mobile version for on-the-go use.

## 📌 References
- Yang, M. (2024). *Multi Head Attention based Confusion Module for English Grammar Error Correction Model*. ICDCECE.
- Facunla, R., & Martinez, J. J. (2023). *Adaptive Real-Time Data Collection Device using Pytesseract-OCR*. I2CACIS.
- Hasan, S. M. T., et al. (2023). *Advancing Abstractive Bangla Text Summarization*. STI.
- Islam, R., & Ahmed, I. (2024). *Gemini-the Most Powerful LLM: Myth or Truth*. ICTC.
- Merchant, K., & Pande, Y. (2024). *NLP Based Latent Semantic Analysis for Legal Text Summarization*. DJSCOE.
