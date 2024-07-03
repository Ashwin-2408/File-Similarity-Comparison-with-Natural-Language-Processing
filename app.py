from flask import Flask, render_template, request
import os
import numpy as np
from FlagEmbedding import BGEM3FlagModel

app = Flask(__name__)


app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)

def encode_sentences(sentences):
    return model.encode(sentences)['dense_vecs']

@app.route("/")
def index():
    return render_template('upload.html')

@app.route("/submit_data", methods=['POST'])
def get_file():
    uploaded_file = request.files['file']
    content = ''
    if uploaded_file:
        content = uploaded_file.read().decode('utf-8').strip()
    
    if not content:
        return "No content found in uploaded file"
    
    array1 = [content]

    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    array2 = []
    filename=[]
    for file_name in file_list:
        filename.append(file_name)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read().strip()
                array2.append(file_content)
    
    if array1 and array2:
        
        embeddings1 = encode_sentences(array2)
        embeddings2 = encode_sentences(array1)
        
        similarity=embeddings1 @ embeddings2.T
        lenth=len(similarity)
        

        return render_template("compare.html",  similarity=similarity,filename=filename,length=lenth)
    else:
        return "No files to compare with"

if __name__ == '__main__':
    app.run(debug=True)
