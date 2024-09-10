from flask import Flask, request, jsonify, render_template
from PIL import Image
import os
import openai
import torch
import clip

app = Flask(__name__, static_folder='static')


# OpenAI API Key
openai.api_key = 'sk-proj-hqtBugPv2m9oj1Jz1sSoT3BlbkFJkLXO7aPXylHPqC8yANv5'

# CLIP Model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Folder for image uploads
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_image_description(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    descriptions = ["a boy", "a girl","a baby", "a dog", "a cat","a bear","a superhero", "a forest", "a castle", "a dragon", "a caterpillar"]
    text = clip.tokenize(descriptions).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        similarities = (image_features @ text_features.T).softmax(dim=-1)
    
    best_description_idx = similarities.argmax().item()
    return descriptions[best_description_idx]

def generate_story(descriptions):
    prompt = f"Print {descriptions[0]}, {descriptions[1]}, and {descriptions[2]}, then create a child-friendly bedtime story for 5 year olds that includes {descriptions[0]}, {descriptions[1]}, and {descriptions[2]}. Make sure the story has a clear beginning, middle, and end, and finishes with a happy ending."

    # Use the chat completions endpoint with a supported model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are an experience children's book writer that writes bedtime stories for children."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,  # Increase this value
        temperature=0.7
    )

    story = response['choices'][0]['message']['content'].strip()

    
    return story


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file1' not in request.files or 'file2' not in request.files or 'file3' not in request.files:
        return jsonify({'error': 'Please upload 3 images'}), 400

    images = []
    for i in range(1, 4):
        file = request.files[f'file{i}']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(img_path)
        images.append(img_path)

    # Get descriptions for each image using CLIP
    descriptions = [get_image_description(image) for image in images]

    # Generate a story using GPT
    story = generate_story(descriptions)

    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

