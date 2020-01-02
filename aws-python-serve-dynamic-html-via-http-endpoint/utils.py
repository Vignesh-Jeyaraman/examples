import json
from flask import Flask, render_template
app = Flask(__name__)

def sendErrorMessage(event,message):
    with app.app_context():
        if 'Authorization' not in event['headers']:
            dynamicHtml = render_template('error.html',message=message)
        else:
            dynamicHtml = render_template('error.html',message=message )
        response = {
        "statusCode": 400,
        "body": dynamicHtml,
        "headers": {
            'Content-Type': 'text/html',
                }
        }
        return response

def sendSuccessMessage(username):
    with app.app_context():
        dynamicHtml = render_template('dynamic.html', username=username)
        response = {
        "statusCode": 200,
        "body": dynamicHtml,
        "headers": {
            'Content-Type': 'text/html',
                }
        }
        return response

def sendAPISuccessResponse(token, username):
    print(token)
    body = {
        "username": username,
        "token": token.decode('UTF-8')
    }
    response = {
        "statusCode": 200,
        "body": json.dumps({'data': body}),
        "headers": {
            'Content-Type': 'application/json',
        }
    }
    return response