import tensorflow
print(tensorflow.__version__)
from keras.models import load_model# TensorFlow is required for Keras to work
model = load_model("keras_model.h5", compile=False)
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import base64
import io
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# TEST FIX
import h5py


# # f = h5py.File("keras_model.h5", mode="r+")
# model_config_string = f.attrs.get("model_config")

# if model_config_string.find('"groups": 1,') != -1:
#     model_config_string = model_config_string.replace('"groups": 1,', '')
# f.attrs.modify('model_config', model_config_string)
# f.flush()

# model_config_string = f.attrs.get("model_config")

# assert model_config_string.find('"groups": 1,') == -1



# # Disable scientific notation for clarity
# np.set_printoptions(suppress=True)

# # Load the model
model = load_model("keras_model.h5", compile=False)

# # Load the labels
class_names = open("labels.txt", "r").readlines()


def predict_image(image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image).astype(np.float32)

    normalized_image_array = (image_array / 127.5) - 1

    data = np.expand_dims(normalized_image_array, axis=0)

    prediction = model.predict(data)

    index = np.argmax(prediction)

    class_name = class_names[index].strip()

    confidence = float(prediction[0][index])

    return {
        "class": class_name,
        "confidence": confidence
    }

# def predict_image(image):
    

# # # Create the array of the right shape to feed into the keras model
# # # The 'length' or number of images you can put into the array is
# # # determined by the first position in the shape tuple, in this case 1
#     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#     # image = Image.open("<IMAGE_PATH>").convert("RGB")
#     # FIX later; find img of user taken pic

# # # Replace this with the path to your image


# # # resizing the image to be at least 224x224 and then cropping from the center
#     size = (224, 224)
#     image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# # # turn the image into a numpy array
#     image_array = np.asarray(image)

# # # Normalize the image
#     normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# # # Load the image into the array
#     data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)
#     data[0] = normalized_image_array

# # # Predicts the model
#     prediction = model.predict(data)
#     index = np.argmax(prediction)
#     class_name = class_names[index][2:].strip()
#     confidence_score = prediction[0][index]

# # # Print prediction and confidence score
#     return {
#         "Class": class_name[index].strip(),
#         "Confidence Score": float(prediction[0][index])
#     }




@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["image"]

    image_data = base64.b64decode(data.split(",")[1])
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    result = predict_image(image)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
    

    image_data = base64
    # return "<h>Rock paper... SCISSOR sisters</h>"
    # return "<p>Ready to play?</p>"
    # return "<button id=\"start\">Start</button>"
    # return "<video id=\"video\" autoplay style=\"display:none\"></video>"
    # data = {'message': 'Webcam access', 'status': 'success'}
    

