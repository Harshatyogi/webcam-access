📖 Real-Time OCR Text Reader with Speech (Python + OpenCV + Tesseract + PyTTSX3)

This project is a real-time text reader that captures video from your webcam, extracts text using Tesseract OCR, and reads it aloud using a Text-to-Speech (TTS) engine.

It is helpful for:

Visually impaired users

Reading printed documents

Live text scanning

Hands-free reading assistance

This application uses:

OpenCV → Webcam frame capture

Pytesseract → Extract text from video frames

pyttsx3 → Convert text to speech

Tesseract-OCR engine for high-quality OCR

✨ Features
🎥 Real-time webcam capture

Continuously reads frames from your webcam.

🔍 Live OCR (Optical Character Recognition)

Extracts readable text from the camera feed using Pytesseract.

🔊 Text-to-Speech Output

Automatically speaks every detected text using pyttsx3.

🖼️ Live Preview Window

Shows your webcam feed in real time.

⌨️ Quit Anytime

Press Q to quit the application safely.

🛠️ Tech Stack
Component	Library
Webcam capture	OpenCV (cv2)
Optical Character Recognition	Tesseract OCR + pytesseract
Text-to-Speech	pyttsx3
Programming Language	Python
📦 Installation & Setup
1️⃣ Install Python Libraries
pip install opencv-python pytesseract pyttsx3

2️⃣ Install Tesseract OCR

Download Tesseract for Windows:

🔗 https://github.com/UB-Mannheim/tesseract/wiki

Example installation path:

C:\Program Files\Tesseract-OCR\tesseract.exe

3️⃣ Update the code with your Tesseract path:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

🚀 How to Run
python main.py


(Replace main.py with your filename)

🧠 How It Works (Step-by-Step)

OpenCV starts the webcam.

Each frame is converted to grayscale for better OCR performance.

Pytesseract extracts text from the frame.

pyttsx3 speaks the recognized text.

The frame is displayed on screen.

Press Q to exit the program.
