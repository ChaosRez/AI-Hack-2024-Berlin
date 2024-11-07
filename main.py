import cv2
import time
import base64
from explainer import explain_photo
from tts import text_to_speech


def capture_and_generate(sleep_duration):
    cap = cv2.VideoCapture(0)  # Initialize the camera

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Encode the captured frame to base64
            _, buffer = cv2.imencode('.jpg', frame)
            image_base64 = base64.b64encode(buffer).decode('utf-8')

            # prompt and generate explanation
            prompt = "explain this photo briefly as you do for a blind person (answer without any opening sentence)"

            start_time = time.time()
            response_text = explain_photo(prompt, image_base64)
            explain_photo_duration = time.time() - start_time
            print(f"explain execution time: {explain_photo_duration:.2f} seconds")

            # Print and speak the response
            print(response_text)

            start_time = time.time()
            text_to_speech([response_text])  # tts  #TODO Async this?
            text_to_speech_duration = time.time() - start_time
            print(f"speech run time: {text_to_speech_duration:.2f} seconds")

            # Wait for before next capture
            time.sleep(sleep_duration)

    finally:
        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_generate(5)  # Call the function with a 3-second sleep duration
