#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# For Genrating test images
#from PIL import Image
#from keras.datasets import mnist
#import numpy as np
#
#(X_train, y_train), (X_test, y_test) = mnist.load_data()
#for i in np.random.randint(0, 10000+1, 10):
#    arr2im = Image.fromarray(X_train[i])
#    arr2im.save('{}.png'.format(i), "PNG")

from keras.models import load_model
import keras
from PIL import Image
import tensorflow.keras
import numpy as np
from flasgger import Swagger

from flask import Flask, request

abspath = "C:\\Users\\Jeevan\\Desktop\\Monika\\"

app = Flask(__name__)
swagger = Swagger(app)

config = tensorflow.ConfigProto(
device_count={'GPU': 1},
intra_op_parallelism_threads=1,
allow_soft_placement=True
)

config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.6

session = tensorflow.Session(config=config)
keras.backend.set_session(session)

model = load_model(abspath+'MNIST\\model.h5')
model._make_predict_function()
@app.route('/predict_digit', methods=['POST'])
def predict_digit():
    with session.as_default():
        with session.graph.as_default():    
            """Example endpoint returning a prediction of mnist
            ---
            parameters:
                - name: image
                in: formData
                type: file
                required: true
                """
            im = Image.open(request.files['image'])
            im2arr = np.array(im).reshape((1, 1, 28, 28))
            print(str(np.argmax(model.predict(im2arr))))
            return str(np.argmax(model.predict(im2arr)))

if __name__ == '__main__':
    app.run()