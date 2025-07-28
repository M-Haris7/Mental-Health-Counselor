# 🤖 Fine-tuned Gemma Mental Health Assistant

A mental health conversational AI built by fine-tuning Google's Gemma 2B model, deployed via Ollama, and accessible through a user-friendly Gradio interface.

## 🌟 Overview

This project provides a mental health support chatbot powered by a fine-tuned Gemma 2B language model. The model has been specifically trained to provide empathetic, helpful, and safe responses to mental health-related queries. The system uses Ollama for efficient model serving and Gradio for an intuitive web interface.

**⚠️ Disclaimer**: This AI assistant is designed to provide general mental health information and support. It is NOT a replacement for professional mental health care. Always consult with qualified healthcare providers for medical advice.

## ✨ Features

- **Fine-tuned Gemma 2B Model**: Specialized for mental health conversations
- **Ollama Integration**: Fast and efficient model serving with low resource usage
- **Gradio Web Interface**: User-friendly chat interface accessible via web browser
- **Streaming Responses**: Real-time response generation for better user experience
- **Customizable Parameters**: Adjust temperature, max tokens, and system prompts
- **Privacy-Focused**: All processing happens locally - no data sent to external servers

## 🛠️ Tech Stack

- **Model**: Google Gemma 2B (fine-tuned)
- **Format**: GGUF (Q8_0 quantization)
- **Serving**: Ollama
- **Frontend**: Gradio
- **Backend**: Python 3.8+
- **Dependencies**: requests, gradio, ollama (optional)

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **Ollama**
   - Download from [https://ollama.ai](https://ollama.ai)
   - Verify installation:
     ```bash
     ollama --version
     ```

3. **Git** (for cloning the repository)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/gemma-mental-health-bot.git
cd gemma-mental-health-bot
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```txt
gradio>=4.0.0
requests>=2.28.0
ollama>=0.1.0  # Optional, for using ollama Python package
```

### Step 4: Set Up the Model in Ollama

1. Create a Modelfile:
   ```bash
   echo "FROM ./models/unsloth.Q8_0.gguf" > Modelfile
   ```

2. Create the model in Ollama:
   ```bash
   ollama create gemma-mental -f Modelfile
   ```

3. Verify the model is loaded:
   ```bash
   ollama list
   ```

## 📖 Usage

### Starting the Application

1. **Start Ollama server** (if not already running):
   ```bash
   ollama serve
   ```

2. **Run the Gradio app**:
   ```bash
   python app.py
   ```

3. **Access the interface**:
   - Local URL: `http://localhost:7860`
   - Public URL: Will be displayed in terminal if `share=True`

### Configuration Options

You can modify the following in `app.py`:

```python
# Model configuration
MODEL_NAME = "gemma-mental"  # Your Ollama model name
OLLAMA_URL = "http://localhost:11434"  # Ollama API endpoint

# Gradio configuration
demo.launch(
    share=True,  # Create public link
    server_port=7860,  # Port number
    server_name="0.0.0.0"  # For network access
)
```

## 🧠 Model Details

### Base Model
- **Model**: Google Gemma 2B
- **Parameters**: 2 billion
- **Architecture**: Transformer-based language model

### Fine-tuning Details
- **Dataset**: Mental health conversations and resources
- **Quantization**: Q8_0 (8-bit quantization)
- **File Size**: ~2.5GB
- **Training Method**: LoRA/QLoRA using Unsloth

