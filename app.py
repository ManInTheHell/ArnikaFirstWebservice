from flask import Flask, jsonify

import numpy as np
import random

app = Flask(__name__)

first_parameter = None
primal_first_parameter = None
second_parameter = None
primal_second_parameter = None


def fetch_parameter(param):
    global first_parameter
    global second_parameter
    global primal_first_parameter
    global primal_second_parameter

    if param == 'a':
        if first_parameter is not None:
            first_parameter += np.random.normal(0, 0.3)
            return first_parameter
        else:
            first_parameter = random.randint(30, 50)
            primal_first_parameter = first_parameter
            return first_parameter
    elif param == 'b':
        if second_parameter is not None:
            second_parameter += np.random.normal(0, 0.3)
            return second_parameter
        else:
            second_parameter = random.randint(30, 50)
            primal_second_parameter = second_parameter
            return second_parameter
    else:
        return None


def reset_parameter(param):
    global first_parameter
    global second_parameter
    global primal_first_parameter
    global primal_second_parameter

    if param == 'a':
        first_parameter = primal_first_parameter
        first_parameter += random.choice([-2, 2])
        primal_first_parameter = first_parameter
        return first_parameter
    elif param == 'b':
        second_parameter = primal_second_parameter
        second_parameter += random.choice([-2, 2])
        primal_second_parameter = second_parameter
        return second_parameter
    else:
        return None


@app.route('/params', methods=['GET'])
def get_random_numbers():
    a = fetch_parameter('a')
    b = fetch_parameter('b')

    response_data = {
        'a': a,
        'b': b
    }

    return jsonify(response_data)


@app.route('/params/<string:parameter>', methods=['GET'])
def get_parameter(parameter):
    if parameter == 'a':
        a = fetch_parameter('a')
        return jsonify({'a': a})
    elif parameter == 'b':
        b = fetch_parameter('b')
        return jsonify({'b': b})
    else:
        return jsonify({'message': 'Not valid!'})


@app.route('/reset/params/<string:parameter>', methods=['PUT'])
def reset(parameter):
    if parameter == 'a':
        a = reset_parameter('a')
        return jsonify({'a': a})
    elif parameter == 'b':
        b = reset_parameter('b')
        return jsonify({'b': b})
    else:
        return jsonify({'message': 'Not valid!'})


if __name__ == '__main__':
    app.run(debug=True)
