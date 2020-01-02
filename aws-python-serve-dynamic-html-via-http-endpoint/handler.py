import json
from app import testParsing, loginView

def landingPage(event, context):
    """
        Entry point to our serverless code. It will call various handler depending upon the
        URL requested.
    """
    handler_mapping = {
                        '/test': testParsing,
                        '/login':loginView
                      }
    event_path = event.get('resource')
    response = handler_mapping[event_path](event, context)
    return response
