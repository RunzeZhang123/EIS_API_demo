# coding=utf-8


# import modules here
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import json
import pandas as pd
import numpy as np

from julia import Julia
# this should be the absolute directory of executable julia
jl = Julia(runtime=r"D:\Julia-1.7.2\bin\julia.exe")
from julia import EquivalentCircuits as eq

# import importlib,sys
# importlib.reload(sys)

app = Flask(__name__)



@app.route("/")
def titles():
    return "This is the main page of api"


@app.route('/upload', methods=['POST'])
def upload_file():
    # store the uploaded file
    UPLOAD_FOLDER = 'app/task_files/'
    file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)

    # if there's no existing file directory, create a new directory
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # load the uploaded file
    f = request.files['file']
    # or using f = request.file.get("filename")
    filename = secure_filename(f.filename)

    # save the file
    f.save(file_dir + str(filename))

    # data processing part- load the data
    data = f'{file_dir}{str(filename)}'
    # load the required characteristics of EIS data
    df = pd.read_json(data)
    abs_Ewe = df['GEIS']["Ewe_bar"]
    abs_I = df["GEIS"]["I_bar"]
    Phase_Zwe = np.array(df["GEIS"]["phase_Zwe"])

    abs_Z = np.divide(abs_Ewe, abs_I)
    Re_Z = np.multiply(abs_Z, (np.cos(Phase_Zwe)))
    Im_Z = np.multiply(abs_Z, (np.sin(Phase_Zwe)))

    reals = Re_Z
    imags = Im_Z
    frequencies = df["GEIS"]["freq"]
    measurements = reals + 1j * imags

    # calling the julia package to do EIS analysis
    eq.circuitevolution(measurements, frequencies, cutoff=0.5, head=10)
    # print(result)

    # return jsonify({"results": result})
    return 'ok'


if __name__ == '__main__':
    app.run()
