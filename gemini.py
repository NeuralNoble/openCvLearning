import cv2
from google.gemini import Gemini

# Your Gemini API key
gemini = Gemini(api_key="YOUR_GEMINI_API_KEY")

def caption_image(image_path):
    """Captures an image from your webcam and uses the Gemini API to generate a caption."""

    response = gemini.generate_text(
        model="gemini-pro",
        prompt=f"What is this image?\n```tool_code\nfile=open('{image_path}', 'rb'); print(file.read())\n```",
    )

    return response.text.strip()

def main():
    """Captures images from your webcam and generates captions for them."""
    video_capture = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Press 's' to capture and caption the image
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Save the captured image
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)

            try:
                # Generate a caption
                caption = caption_image(image_path)
                print("Gemini says:", caption)

            except Exception as e:
                print(f"An error occurred: {e}")

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()