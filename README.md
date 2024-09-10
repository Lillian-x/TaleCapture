# TaleCapture

TaleCapture is an AI-powered web application that generates personalized, child-friendly bedtime stories based on three user-uploaded images. By combining advanced image recognition using OpenAI's CLIP model and story generation through GPT, TaleCapture offers a unique and interactive storytelling experience for kids.

## Table of Contents
- [How It Works](#how-it-works)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## How It Works
1. **Image Upload**: The user uploads three images via the simple web interface.
2. **Image Recognition**: The app uses OpenAI's CLIP model to analyze the uploaded images and extract key descriptions or themes.
3. **Story Generation**: Based on the image descriptions, the app uses OpenAI's GPT model to generate a creative and child-friendly bedtime story.
4. **Interactive Story**: The generated story is displayed on the web interface, providing a magical storytelling experience based on the uploaded images.

## Key Features
- **AI-powered Image Recognition**: Extracts key elements from images using OpenAI's CLIP model.
- **Custom Story Generation**: Uses GPT to generate a unique, personalized story for each set of uploaded images.
- **User-friendly Interface**: Built using Gradio for a simple, interactive interface.
- **Educational and Fun**: Provides an engaging tool for children, parents, and educators to create unique storytelling experiences.

## Technology Stack
- **Python**: Backend logic and AI model integration.
- **Gradio**: For the user-friendly frontend interface.
- **OpenAI CLIP**: For image recognition and analysis.
- **OpenAI GPT**: For generating creative text and stories.
- **Google Colab**: Platform for running the app in the cloud without the need for extensive deployment.
- **PIL**: For image handling and processing.

## Usage
1. Open the app via the provided Google Colab or Gradio link.
2. Upload three images (supported formats: `.jpg`, `.jpeg`, `.png`).
3. Wait for the app to process the images and generate a unique bedtime story.
4. Enjoy the personalized story based on the images you provided!

## Installation
If you want to run the project locally, follow the instructions below.

### Prerequisites
- Python 3.x
- An OpenAI API Key
- The following Python libraries:
  - `openai`
  - `torch`
  - `Pillow`
  - `clip-by-openai`

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/talecapture.git
   cd talecapture
2. **Install dependencies**:
   pip install -r requirements.txt
3. **Set you OpenAI API Key**:
   export OPENAI_API_KEY='your-openai-api-key'
4. **Run the app**: Launch the Gradio interface locally:
   python app.py
5. **Use the app**
  Open your browser and go to http://localhost:7860. Upload three images and let the app generate a story!



## Contributing
I welcome contributions to improve TaleCapture! Here’s how you can contribute:

1. Fork the repository.
2. Create a new feature branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request and describe your changes.

## License
This project is licensed under the MIT License.
