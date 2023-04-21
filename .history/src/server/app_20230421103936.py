from flask import Flask, request, jsonify
from flask_cors import CORS
import transformers
import spacy
import weaviate

import json
from transformers import AutoTokenizer, AutoModel
import torch
import weaviate

# Load pre-trained model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Initialize Weaviate client
client = weaviate.Client("http://localhost:8080")  # Replace with your Weaviate instance URL


app = Flask(__name__)
CORS(app)

@app.route('/api/questions', methods=['POST'])
def get_similar_questions():
    # Your code for processing the question, NLP, and vector similarity search will go here
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
