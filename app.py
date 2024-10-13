from flask import Flask, request, jsonify
from email_processing import summarize_email, generate_email_response

# Initialize Flask app
app = Flask(__name__)

# Define a route for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    email_content = data.get("email_content", "")
    
    if not email_content:
        return jsonify({"error": "Email content is required"}), 400

    summary = summarize_email(email_content)
    return jsonify({"summary": summary})

# Define a route for response generation
@app.route('/generate-response', methods=['POST'])
def generate_response():
    data = request.json
    email_content = data.get("email_content", "")
    
    if not email_content:
        return jsonify({"error": "Email content is required"}), 400

    response = generate_email_response(email_content)
    return jsonify({"response": response})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
