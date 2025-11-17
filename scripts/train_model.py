import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# ==== CONFIG ====
base_dir = "images"
batch_size = 8        # reduce to 4 if memory errors
img_size = (224,224)
epochs = 10           # can increase later to improve accuracy
# =================

train_gen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = train_gen.flow_from_directory(
    base_dir, target_size=img_size, batch_size=batch_size,
    class_mode='categorical', subset='training', shuffle=True
)
val_data = train_gen.flow_from_directory(
    base_dir, target_size=img_size, batch_size=batch_size,
    class_mode='categorical', subset='validation', shuffle=False
)

# ==== MODEL ====
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=img_size+(3,))
x = GlobalAveragePooling2D()(base_model.output)
x = Dense(256, activation='relu')(x)
out = Dense(train_data.num_classes, activation='softmax')(x)
model = Model(base_model.input, out)

# freeze base model
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer=Adam(1e-4), loss='categorical_crossentropy', metrics=['accuracy'])

# ==== TRAIN ====
history = model.fit(train_data, validation_data=val_data, epochs=epochs)

# ==== SAVE MODEL ====
os.makedirs("models", exist_ok=True)
model.save("models/coral_model.h5")
print("\\n✅ Model saved to models/coral_model.h5")

plt.figure()
plt.plot(history.history.get('accuracy', []), label='train acc')
plt.plot(history.history.get('val_accuracy', []), label='val acc')
plt.legend(); plt.title("Accuracy")
plt.xlabel("Epochs"); plt.ylabel("Accuracy")
plt.savefig("models/training_accuracy.png")
print("✅ Training plot saved to models/training_accuracy.png")
