# TrafficVision

**TrafficVision** is a Streamlit web application that detects traffic lights in uploaded images and identifies their colors using a YOLOv5 model and OpenCV.

## Features

- Upload images in PNG, JPG, JPEG, or WEBP formats.
- Detect traffic lights and other objects in the uploaded images.
- Identify the color of detected traffic lights (Red, Green, Yellow).

## Screenshot
![TrafficVision App Screenshot]("Screenshot 2025-02-21 200900.png")


## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd Traffic_Light_Detection
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image using the file uploader.

4. View the original and detected images side by side.

5. See the detected objects and the color of any detected traffic lights.


