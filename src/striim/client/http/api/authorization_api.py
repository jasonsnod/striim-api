import requests
import json
from striim.client.helpers.striim_api_error_helper import StriimException

# python 2 and 3 compatibility library
import six

class StriimAuthorization(object):

    AUTHENTICATE_ENDPOINT = '/security/authenticate'

    def __init__(self, api_url=None, username=None, password=None, mtls_enabled=False):
        
        if not api_url or not username or not password:
            raise Exception('You will need a url, username, and password for your Striim implementation to be able to authorize with it.')
        
        self.__api_url = api_url

        self.__authorization_payload = {
                'username': username,
                'password': password
            } 
        
        self.__mtls_enabled = mtls_enabled
    
    def get_authorization_token(self):
        
        try:
            authorization_token_response = requests.post(url = self.__api_url + self.AUTHENTICATE_ENDPOINT, data = self.__authorization_payload, verify = self.__mtls_enabled)

            if authorization_token_response.status_code != 200:
                authorization_token_response.raise_for_status()

            return authorization_token_response.json['token']
            

        except requests.exceptions.RequestException as error:
            request_exception_error_string = ""
            raise StriimException(error, request_exception_error_string)
        
        except requests.exceptions.SSLError as error:
            ssl_exception_error_string = ""
            raise StriimException(error, ssl_exception_error_string)
        
        except requests.exceptions.HTTPError as error:
            http_exception_error_string = "There was a problem authenticating to Striim. Please check your credentials"
            raise StriimException(error, http_exception_error_string)

        except requests.exceptions.Timeout as error:
            timeout_exception_error_string = ""
            raise StriimException(error, timeout_exception_error_string)

        except requests.exceptions.ConnectionError as error:
            connection_exception_error_string = ""
            raise StriimException(error, connection_exception_error_string)
            


    
