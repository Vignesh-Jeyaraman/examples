import json
import jwt
from flask import Flask, render_template
from base import LambdaBase
from utils import sendErrorMessage, sendSuccessMessage
from local import SECRET_KEY

app = Flask(__name__)

class TestParsing(LambdaBase):
    """
        Class to parse HTML if Authorization token is present on Header.
    """
    def handle(self, event, context):
        # check whether Authorization token is there on header else send error message
        if 'Authorization' not in event['headers']:
            return sendErrorMessage(event=event,message="PLEASE PROVIDE AUTHORIZATION TOKEN ON HEADER TO CONTINUE")
        creds = jwt.decode(event['headers']['Authorization'], SECRET_KEY)
        # Decode the token and check whether we got email as well as username after decoding else send error message
        if 'email' not in  creds or 'username' not in creds:
            return sendErrorMessage(event=event,message="INVALID TOKEN")
        # If everything is fine send success response
        return sendSuccessMessage(username=creds['username'].capitalize())

# Call handler method based upon the routes.
testParsing = TestParsing.get_handler()
