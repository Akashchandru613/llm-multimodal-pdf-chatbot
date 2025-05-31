# File: app.py
import gradio as gr
from pdf_utils import extract_text_from_pdf
from chat_chain import get_gemini_response

def handle_pdf_and_question(file, question):
    if file is None or question.strip() == "":
        return "Please upload a PDF and enter a question."

    pdf_text = extract_text_from_pdf(file.name)
    prompt = f"Based on this PDF content:\n{pdf_text}\n\nAnswer the question: {question}"
    return get_gemini_response(prompt)

with gr.Blocks() as demo:
    gr.Markdown("# 📄 LLM-Powered PDF Chatbot (Gemini)")
    file_input = gr.File(label="Upload PDF", type="filepath")
    question_input = gr.Textbox(label="Ask a question")
    output = gr.Textbox(label="Gemini's Answer")
    submit = gr.Button("Submit")

    submit.click(fn=handle_pdf_and_question, inputs=[file_input, question_input], outputs=output)

if __name__ == "__main__":
    demo.launch()
