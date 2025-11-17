from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np, os
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # allow frontend (localhost:5173) to access backend (localhost:5000)

# Load trained model
model_path = "models/coral_model.h5"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")
model = tf.keras.models.load_model(model_path)

# Get class labels from your dataset folder
classes = sorted(os.listdir("images"))

@app.route("/")
def home():
    return jsonify({"message": "CoralSight backend running ✅"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "no file uploaded"}), 400

    f = request.files["file"]
    filepath = os.path.join("temp_upload.jpg")
    f.save(filepath)

    # Preprocess image
    img = image.load_img(filepath, target_size=(224, 224))
    x = image.img_to_array(img)[None, ...] / 255.0

    # Predict
    pred = model.predict(x)[0]
    pred_class = classes[np.argmax(pred)]
    confidence = round(float(np.max(pred) * 100), 2)

    return jsonify({
        "prediction": pred_class,
        "confidence": confidence
    })

if __name__ == "__main__":
    print("🚀 Starting CoralSight backend on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
