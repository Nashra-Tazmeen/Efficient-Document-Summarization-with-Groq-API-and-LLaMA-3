# **PDF Summarizer with Groq API and LLaMA 3 (8B-8192 Model)**

This project is an AI-powered PDF summarizer developed to extract and summarize key elements from business documents. Using the Groq API and the LLaMA 3 (8B-8192) model, the tool focuses on identifying critical information, such as future growth prospects, key business changes, triggers, and material factors that could impact next year’s earnings and growth of a company. Designed for efficiency, it processes lengthy documents by chunking them into batches, ensuring accurate and relevant summaries suitable for strategic decision-making and large-scale document analysis.

---

## **Table of Contents**

- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## **Installation**

Follow these steps to install and run the project:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Nashra-Tazmeen/Efficient-Document-Summarization-with-Groq-API-and-LLaMA-3.git
   
    ```

2. **Create and activate a virtual environment** (recommended):

    ```bash
    python -m venv venv
    On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Ensure you have a `.env` file with the following content:

    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```

    Replace `your_groq_api_key_here` with your actual Google API key. You can obtain the key by visiting the [**Groq cloud**](https://console.groq.com/keys) and enabling the **create API key**.

---

## **Project Structure**

The project is organized as follows:

```
Multi-PDF-Chat-with-LangChain-and-LLMs/
│
├── main.py              #main execution  
├── Data_extraction.py   # Extracts data from pdf
├── text_chunker.py      # divides text into chunks 
├── batches.py           # chunks into batches 
├── summarizer.py        # summarizes the text 
├── requirement.txt      # Python dependencies
├── env                  # Environment variables (G_API_KEY)
└── README.md            # Project documentation
```



---

## **How to Run the Project**

### 1. **Run the main.py file**

Once the dependencies are installed, you can start running main.py:

```bash
python main.py
```



---







