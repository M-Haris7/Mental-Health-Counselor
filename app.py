import gradio as gr
import requests
import json

# Your Ollama model name - change this to match your model
MODEL_NAME = "gemma-counselor"  # Replace with your actual model name in Ollama

def chat(message, history):
    """
    Send message to Ollama and get response
    """
    try:
        # Prepare the API request
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": MODEL_NAME,
                "prompt": message,
                "stream": False
            }
        )
        
        # Parse the response
        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}"

# Create Gradio interface
demo = gr.ChatInterface(
    fn=chat,
    title="Gemma Mental Health Assistant",
    description="Chat with your fine-tuned Gemma model via Ollama",
    examples=[
        "I'm feeling stressed about work",
        "What are some relaxation techniques?",
        "How can I improve my sleep quality?"
    ],
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(share=True)