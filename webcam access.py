import cv2
import pytesseract
import pyttsx3

# Set the path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for better text recognition
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the frame
    text = pytesseract.image_to_string(gray_frame)

    # Speak the extracted text
    engine.say(text)
    engine.runAndWait()

    # Display the original frame with the extracted text
    cv2.imshow('Text Reader', frame)

    # Print the extracted text to the console
    print("Extracted Text:", text)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
