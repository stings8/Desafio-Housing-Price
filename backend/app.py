from flask import Flask, request, jsonify
from sklearn.externals import joblib
import matplotlib as pl
from joblib import dump, load

import numpy as np
pl.use('Agg')
import matplotlib.pyplot as plt



# declare constants
HOST = '0.0.0.0'
PORT = 8081

app = Flask(__name__)


@app.route('/api/train', methods=['POST'])
def train():

    grad = load('/Users/erickkelvin/Desktop/Housing/gradB.joblib')
    reg  = load('/Users/erickkelvin/Desktop/Housing/reg.joblib')

    # persist model
    joblib.dump(grad, 'modelGrad.pkl')
    joblib.dump(reg, 'modelReg.pkl')


    return jsonify({'accuracy': round(grad.score(X, Y))})


@app.route('/api/predict', methods=['POST'])
def predict():
    # get Boston object from request
    X = request.get_json()
    X = [[float (X['CRIM', 'ZN']), float (X['INDUS']), float (X['CHAS']), float (X['NOX']), float (X['RM']),float (X['AGE']), float (X['DIS']),
          float (X['RAD']), float (X['TAX']), float (X['PTRATIO']), float (X['B']), float (X['LSTAT']), float (X['MEDV'])]]
    # read model
    grad = joblib.load('model.pkl')

    probabilities = grad.predict_proba(X)

    return jsonify([{'Valor': 'MEDV', 'value': round(probabilities[0, 0])}])


class HttpResponse(object):
    pass


def getimage(request):
    x = np.arange(0, 2 * np.pi, 0.01)
    s = np.cos(x) ** 2
    plt.plot(x, s)

    plt.xlabel('xlabel(X)')
    plt.ylabel('ylabel(Y)')
    plt.title('Simple Graph!')
    plt.grid(True)

    response = HttpResponse(content_type="image/jpeg")
    plt.savefig(response, format="png")
    return response


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
