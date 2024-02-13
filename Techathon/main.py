from flask import Flask, jsonify, request, make_response
from watsonx import watsonx_response
from serviceNowAPI import createINC
from flask_cors import CORS, cross_origin

app = Flask("My Server")
CORS(app, resources={r"/api/*": {"origins": "http://localhost:63343"}})

app.config.update({
    'DEBUG': True,
    'methods': ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    'headers': ["Content-Type", "Authorization"]
})


responses=[]
issueType=""


@app.route('/api/data', methods=['POST'])
@cross_origin()
def get_data():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = "http://localhost:63343"
        response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS"
        response.headers['Access-Control-Allow-Headers'] = "Content-Type, Authorization"
    else:
        data = request.get_json()
        received_data = data.get('data')
        app.logger.info("Calling watsonx for prompt:{}...".format(received_data))
        responses.append('User:'+received_data)
        issueCheck(received_data)
        response = watsonx_response(received_data)
        responses.append('Bot:'+response)
        app.logger.info("Watsonx response:{}...".format(response))

    return response


@app.route('/api/inc', methods=['POST'])
@cross_origin()
def getINC():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = "http://localhost:63343"
        response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS"
        response.headers['Access-Control-Allow-Headers'] = "Content-Type, Authorization"
    else:
        app.logger.info("Calling ServiceNow API")
        response = createINC(issueType,responses)
        app.logger.info("INC is:{}".format(response))

    return response


def issueCheck(input):
    global issueType
    if 'MODEM' or 'MODEM'.lower() in input:
        issueType = 'Modem Issue'
    elif 'DTV' or 'DTV'.lower() in input:
        issueType='DTV Issue'
    elif 'Hand Phone' or 'Hand Phone'.lower() in input:
        issueType='Hand Phone Issue'
    elif 'INTERNET' or 'INTERNET'.lower() in input:
        issueType='INTERNET Issue'
    else:
        issueType = 'General Accessibility Issue'


if __name__ == '__main__':
    app.run(debug=True)
