import json
import jwt
from flask import Flask, render_template
from base import LambdaBase
from utils import sendErrorMessage, sendSuccessMessage, sendAPISuccessResponse
from local import SECRET_KEY, ADMIN_PASSWORD, ADMIN_USERNAME
    
app = Flask(__name__)

class userLogin(LambdaBase):
    """
        Class to check whether login creds are valid or not
    """
    def handle(self, event, context):
        # load the json we got on request body
        api_body = json.loads(event["body"])
        if 'username' not in api_body or 'password' not in api_body:
            return sendErrorMessage(event = event, message="PLEASE PROVIDE USERNAME, EMAIL AND PASSWORD")
        # check whether the username and password received matches the one stored in local.py
        if api_body['username'] == ADMIN_USERNAME and api_body['password'] == ADMIN_PASSWORD:
            token = jwt.encode({"username":api_body['username']}, SECRET_KEY)
            return sendAPISuccessResponse(username=api_body['username'],token=token)
        # If issue with creds throw error.
        return sendErrorMessage(event = event, message="INVALID CREDENTIALS")

class TestParsing(LambdaBase):
    """
        Class to parse HTML if Authorization token is present on Header.
    """
    def handle(self, event, context):
        # check whether Authorization token is there on header else send error message
        if 'Authorization' not in event['headers']:
            return sendErrorMessage(event=event,message="PLEASE PROVIDE AUTHORIZATION TOKEN ON HEADER TO CONTINUE")
        try:
            creds = jwt.decode(event['headers']['Authorization'], SECRET_KEY)
        except:
            return sendErrorMessage(event=event,message="INVALID TOKEN")
        # Decode the token and check whether we got email as well as username after decoding else send error message
        if 'email' not in  creds or 'username' not in creds:
            return sendErrorMessage(event=event,message="INVALID TOKEN")
        # If everything is fine send success response
        return sendSuccessMessage(username=creds['username'].capitalize())

# Call handler method based upon the routes.
testParsing = TestParsing.get_handler()
loginView = userLogin.get_handler()