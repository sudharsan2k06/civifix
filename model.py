import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.applications.MobileNetV2(
    weights="imagenet",
    include_top=True
)

def predict_issue(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    img_array = np.array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]

    # Take top prediction
    label = decoded[0][1].lower()
    confidence = decoded[0][2]   # probability score (0–1)

    # Confidence filter (IMPORTANT)
    if confidence < 0.10:
        return "other issues"

    # Civic issue mapping (hackathon logic)
    if "street" in label or "road" in label or "pavement" in label or "path" in label:
        return "pothole"
    elif "trash" in label or "garbage" in label or "bin" in label:
        return "garbage"
    else:
        return "streetlight"
