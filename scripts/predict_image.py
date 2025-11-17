import tensorflow as tf, os, sys
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("models/coral_model.h5")
img_path = sys.argv[1]
img = image.load_img(img_path, target_size=(224,224))
x = image.img_to_array(img)[None, ...] / 255.0
pred = model.predict(x)[0]
classes = sorted(os.listdir("images"))
print("Classes:", classes)
print(f"Predicted: {classes[pred.argmax()]} (confidence: {pred.max():.3f})")
