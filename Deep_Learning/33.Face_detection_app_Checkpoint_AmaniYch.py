# Checkpoint Objective: Improving the Streamlit app for face detection using Viola-Jones algorithm of the example of the content

Add instructions to the Streamlit app interface to guide the user on how to use the app.
Add a feature to save the images with detected faces on the user's device.
Add a feature to allow the user to choose the color of the rectangles drawn around the detected faces.
Add a feature to adjust the minNeighbors parameter in the face_cascade.detectMultiScale() function.
Add a feature to adjust the scaleFactor parameter in the face_cascade.detectMultiScale() function.



import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Upload an image to detect faces:")

    # Upload image
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Convert the file to an opencv image
        image = np.array(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(image, 1)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Load the pre-trained Haar Cascade model for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Adjust parameters using sliders
        min_neighbors = st.slider("Select the minNeighbors parameter", 1, 10, 5)
        scale_factor = st.slider("Select the scaleFactor parameter", 1.01, 2.0, 1.2)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=scale_factor, minNeighbors=min_neighbors)

        # Get user-selected rectangle color
        rectangle_color = st.color_picker("Select the color of the rectangles", "#ff0000")

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), tuple(int(rectangle_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)), 2)

        # Display the original and processed images
        st.image(image, channels="BGR", caption="Processed Image", use_column_width=True)

        # Add a button to save the image with detected faces
        if st.button("Save Image"):
            cv2.imwrite("image_with_faces.jpg", image)
            st.success("Image with detected faces saved successfully!")

if __name__ == "__main__":
    main()
