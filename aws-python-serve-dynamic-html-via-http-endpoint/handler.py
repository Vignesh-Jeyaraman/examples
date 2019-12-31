import json
from app import testParsing

def landingPage(event, context):
    """
        Entry point to our serverless code. It will call various handler depending upon the
        URL requested.
    """
    handler_mapping = {
                        '/test': testParsing
                      }
    event_path = event.get('resource')
    response = handler_mapping[event_path](event, context)
    return response
