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

            # Save the captured frame to a file
            # image_path = "_archive/captured_image.jpg"
            # cv2.imwrite(image_path, frame)

            # Encode the captured frame to base64
            _, buffer = cv2.imencode('.jpg', frame)
            image_base64 = base64.b64encode(buffer).decode('utf-8')

            # prompt
            prompt = "explain this photo briefly as you do for a blind person (answer without any opening sentence)"
            response_text = explain_photo(prompt, image_base64)
            print(response_text)
            text_to_speech([response_text])


            # Wait for before next capture
            time.sleep(sleep_duration)

    finally:
        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_generate(5)  # Call the function with a 3-second sleep duration
