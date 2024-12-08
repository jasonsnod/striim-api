import requests
from striim.client.helpers.striim_api_error_helper import StriimException

# python 2 and 3 compatibility library
import six

class StriimAuthorizationApi(object):

    def __init__(self, api_url=None, username=None, password=None, mtls_enabled=False):
        if api_url:
            self.api_url = api_url

        if username and password:
            self.authorization_payload = {
                'username': username,
                'password': password
            } 
        
        self.mtls_enabled = mtls_enabled
    
    def get_authorization_token(self):
        
        try:
            authorization_token_response = requests.post(url = self.api_url, data = self.authorization_payload, verify = self.mtls_enabled)
        
        except requests.exceptions.RequestException as error:
            request_exception_error_string = ""
            raise StriimException(error, request_exception_error_string)
        
        except requests.exceptions.SSLError as error:
            ssl_exception_error_string = ""
            raise StriimException(error, ssl_exception_error_string)
        
        except requests.exceptions.HTTPError as error:
            http_exception_error_string = ""
            raise StriimException(error, http_exception_error_string)

        except requests.exceptions.Timeout as error:
            timeout_exception_error_string = ""
            raise StriimException(error, timeout_exception_error_string)

        except requests.exceptions.ConnectionError as error:
            connection_exception_error_string = ""
            raise StriimException(error, connection_exception_error_string)
            


    
