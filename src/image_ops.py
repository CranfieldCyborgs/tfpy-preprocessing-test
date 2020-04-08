import tensorflow as tf
from pathlib import Path
from PIL import Image


def display_image(image_path_as_str):
    """
    This function captures the image reading operation available in Tensorflow.
    """
    image_path = Path(image_path_as_str)
    image = tf.keras.preprocessing.image.load_img(
        image_path, grayscale=False, color_mode='rgb', target_size=None, interpolation='nearest')

    print("Image read operation completed.")

    image.show()
    # image.rotate(45).show()
