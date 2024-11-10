import cv2
import time
import base64
from explainer import explain_photo
from tts import text_to_speech
from stt import speech_to_text


def capture_and_generate(sleep_duration):
    cap = cv2.VideoCapture(0)  # Initialize the camera

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            start_time = time.time()
            question = speech_to_text()
            stt_duration = time.time() - start_time
            print(f"Recognized text: {question} (stt duration: {stt_duration:.2f} seconds)")
            if question == "":
                # print("Appearently, no questions were asked.")
                continue

            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Encode the captured frame to base64
            _, buffer = cv2.imencode('.jpg', frame)
            image_base64 = base64.b64encode(buffer).decode('utf-8')

            # prompt and generate explanation
            prompt = "answer my question concisely about what you see from my rear phone camera concisely. I am blind and need your assist (answer without any opening sentence):  "
            # prompt += "is there a barrier in front of me? if yes how far?"
            prompt += question + "?"

            start_time = time.time()
            response_text = explain_photo(prompt, image_base64)
            explain_photo_duration = time.time() - start_time
            print(f"explain execution time: {explain_photo_duration:.2f} seconds")

            # Print and speak the response
            print(response_text)

            start_time = time.time()
            text_to_speech([response_text])  # tts  #TODO Async this?
            text_to_speech_duration = time.time() - start_time
            print(f"tts time: {text_to_speech_duration:.2f} seconds")

            # Wait for before next capture
            time.sleep(sleep_duration)

    finally:
        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_generate(0)  # Call the function with an x-second sleep duration
