import os
import tensorflow as tf
from utils import preprocess
from tensorflow_hub.keras_layer import KerasLayer
from fastapi import FastAPI, Response, status, UploadFile, File
from io import BytesIO
from PIL import Image
from numpy import argmax, array
from uvicorn import run


app = FastAPI()

model_dir = "Model_Mobilenet_v2.h5"
with tf.keras.utils.custom_object_scope({'KerasLayer': KerasLayer}):
    model = tf.keras.models.load_model(model_dir)

class_fruits = array([
    'fresh_apple',
    'fresh_banana',
    'fresh_guava',
    'fresh_lime',
    'fresh_mango',
    'fresh_orange',
    'fresh_strawberry',
    'rotten_apple',
    'rotten_banana',
    'rotten_guava',
    'rotten_lime',
    'rotten_mango',
    'rotten_orange',
    'rotten_strawberry'
])


@app.get("/")
async def index():
    return {"Welcome to the Fruitarians API for freshness!"}


@app.post("/api/prediction/")
async def api_prediction_classification_freshness(image_data: UploadFile = File(...)):
    if not image_data:
        return {"message": "No image provided"}

    image = await image_data.read()
    image = Image.open(BytesIO(image))

    prep_image = preprocess(image)
    pred = model.predict(prep_image)

    score = tf.nn.softmax(pred[0])
    class_prediction = class_fruits[argmax(score)]
    pred_score = float(pred[0][pred.argmax()])

    return {
        "model-prediction": class_prediction,
        "model-prediction-confidence-score": pred_score,
    }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    run(app, host="0.0.0.0", port=port)
