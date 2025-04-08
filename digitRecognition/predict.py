from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load the trained model
model = load_model('model.h5')

# Load and preprocess your custom image
def preprocess_image(img_path):
    # Load the image
    img = Image.open("drawing.png").convert("L")  # Convert to grayscale

    # Resize to 28x28 (if needed)
    img_resized = img.resize((28, 28), Image.ANTIALIAS)

    # Invert if background is black and digit is white (which is correct for MNIST)
    img_inverted = ImageOps.invert(img_resized)

    # Convert to NumPy array
    img_array = np.array(img_inverted)

    # Normalize
    img_array = img_array / 255.0

    # Reshape for prediction
    img_input = img_array.reshape(1, 28, 28, 1)  # If using a CNN model

    print(img_input.shape)  # Should be (1, 28, 28, 1)
    return img_input

# Predict
input_image = preprocess_image('drawing.png')
# prediction = model.predict(input_image)
# print("Predicted class:", np.argmax(prediction))

print(input_image)
