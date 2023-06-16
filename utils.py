import tensorflow as tf
from PIL import Image


def preprocess(image: Image.Image):
    image = image.resize((224, 224), resample=Image.BILINEAR).convert("RGB")
    image = tf.keras.utils.img_to_array(image)
    image = image / 255.0
    image = tf.expand_dims(image, 0)
    return image


# def read_image_from_base64(image_data):
#     image_bytes = base64.b64decode(image_data)
#     image = Image.open(BytesIO(image_bytes))
#     return image


# def preprocess(image: Image.Image):
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     image = cv2.resize(image, input_shape)
#     image = tf.keras.utils.img_to_array(image)
#     image = image / 255.0
#     image = tf.expand_dims(image, 0)
#     return image
