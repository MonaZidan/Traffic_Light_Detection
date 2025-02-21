# LIBs
import cv2
import torch
import numpy as np
from PIL import Image
import streamlit as st

# Streamlit UI Congiguration
st.set_page_config(page_title="TrafficVision", page_icon="🚦", layout="centered")

# Load yolov5s Model
@st.cache_resource
def load_model():
     return torch.hub.load("ultralytics/yolov5","yolov5s")

yolov5_model = load_model()

# Color Detection Function
def color_detection(img, box):
    x1, y1, x2, y2 = map(int, box)
    cropped_img = img[y1:y2, x1:x2]

    hsv_img = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2HSV)

    red_lower = np.array([0, 70, 50])
    red_upper = np.array([10, 255, 255])

    red_lower2 = np.array([170, 70, 50])
    red_upper2 = np.array([180, 255, 255])

    green_lower = np.array([40, 40, 40])
    green_upper = np.array([80, 255, 255])

    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    red_mask = cv2.inRange(hsv_img, red_lower, red_upper)
    red_mask2 = cv2.inRange(hsv_img, red_lower2, red_upper2)
    red_mask_2ranges = red_mask | red_mask2
    red_pixels = cv2.countNonZero(red_mask_2ranges)

    green_mask = cv2.inRange(hsv_img, green_lower, green_upper)
    green_pixels = cv2.countNonZero(green_mask)

    yellow_mask = cv2.inRange(hsv_img, yellow_lower, yellow_upper)
    yellow_pixels = cv2.countNonZero(yellow_mask)

    if max(red_pixels, green_pixels, yellow_pixels) == red_pixels:
        return "The detected traffic light is **Red**"
    elif max(red_pixels, green_pixels, yellow_pixels) == green_pixels:
        return "The detected traffic light is **Green**"
    elif max(red_pixels, green_pixels, yellow_pixels) == yellow_pixels:
        return "The detected traffic light is **Yellow**"
    else:
        return "Unable to detec the traffic light"


# Streamlit UI
st.title("🚦 TrafficVision: Detect Traffic Lights and More")

# User Image Upload
user_img = st.file_uploader("Please upload your image : ", type= ["png", "jpg", "jpeg", "webp"])

original, detected = st.columns(2)
# Detect traffic ligth
if user_img is not None:
    image = Image.open(user_img)
    image_array = np.array(image)
    with original:
        st.image(image_array, caption="Original Image", use_container_width=True)
    
    with detected:
        with st.spinner("Detecting objects..."):
            result = yolov5_model(image_array)
            boxes = result.xyxy[0].numpy()
            st.image(result.render()[0], caption="Detected Objects", use_container_width=True)

    for box in boxes:
        detected_object = result.names[int(box[5])]
        if detected_object == "traffic light":
            light_color = color_detection(image_array, box[:4])
            st.write("- Traffic Light:",light_color) 
        else:
            st.write("- Detected Object: ",detected_object)
            




















