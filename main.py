from flask import Flask, request, jsonify
from src.ai.assistant import Assistant
from src.pdf.parser import PDFParser
from src.conversation.chat import Chat

app = Flask(__name__)

# Initialize components
assistant = Assistant()
pdf_parser = PDFParser()
chat = Chat()

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if file:
        text = pdf_parser.extract_text(file)
        return jsonify({"message": "PDF uploaded successfully", "text": text}), 200
    return jsonify({"error": "No file uploaded"}), 400

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    context = data.get('context')
    if question and context:
        response = assistant.get_response(question, context)
        chat.add_to_history(question, response)
        return jsonify({"response": response}), 200
    return jsonify({"error": "Question or context missing"}), 400

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(chat.get_history()), 200

if __name__ == '__main__':
    app.run(debug=True)