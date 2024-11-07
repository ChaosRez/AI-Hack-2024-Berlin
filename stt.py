import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio_data)  # Use Google's speech recognition
            return text
        except sr.UnknownValueError:
            return "" # Could not understand the audio
        except sr.RequestError as e:
            return f"Could not request results from speech recognition service; {e}"

#
# if __name__ == "__main__":
#     text = speech_to_text()
#     print("Recognized text:", text)
