from deepface import DeepFace
import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Perform emotion analysis using DeepFace
    results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Extract emotion and confidence score from the first result
    result = results[0]
    dominant_emotion = result['dominant_emotion']
    emotion_confidence = result['emotion'][dominant_emotion]

    # Draw emotion label on the frame
    cv2.putText(frame, f"{dominant_emotion} ({emotion_confidence:.2f})",
                (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Emotion Detection', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()