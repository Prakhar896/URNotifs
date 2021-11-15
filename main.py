from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

def fileContent(fileName):
    with open(fileName, 'r') as f:
        f_content = f.read()
        return f_content

@app.route('/')
def home():
    return fileContent('homepage.html')

@app.route('/newUpdate', methods=['POST'])
def newUpdate():
    if request.headers['Content-Type'] != 'application/json':
        return {'failed': "Incorrect Content-Type"}, 400
    else:
        for elem in ["monitorID", "monitorURL", "monitorFriendlyName", "alertType", "alertTypeFriendlyName", "alertDuration", "alertDatetime", "monitorAlertContacts"]:
            if elem not in request.json:
                return {'failed': "Missing required field: " + elem}, 400
        print(request.json)
        return {'success': "New update received"}, 200


# Service assets
@app.route('/assets/copyright')
def copyright():
    return fileContent('copyright.js')

if __name__ == '__main__':
    app.run(port=8000)