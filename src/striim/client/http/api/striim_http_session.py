import requests
from striim.client.helpers.striim_api_error_helper import StriimException
from authorization_api import StriimAuthorization

class StriimSession:
    
    def __init__(self, striim_http_address, is_authorizing=False, striim_authorization=None):
        self.__base_url = striim_http_address

        self.create_session()

        
        if not is_authorizing:
            print('Setting the Striim auth token to None. Use the authorize_session function to retrieve the auth token from Striim.')
            striim_auth_token = ''
        else:
            self.__striim_authorization = striim_authorization
            striim_auth_token = self.__striim_authorization.get_authorization_token()
        
        self.set_api_header(striim_auth_token)
        
    def create_session(self):
        self.__session = requests.Session()

    def authorize_session(self, username, password):

        striim_auth_payload = {
            'username': username,
            'password': password
        }

        try:
            auth_token_response = self.__session.post(url=self.__base_url + self.AUTH_PATH, data=striim_auth_payload)
            
            if auth_token_response.status_code != 200:
                auth_token_response.raise_for_status
            
            else:
                return auth_token_response.json()['token']

        except Exception as error:
            raise StriimSession(error.message)   

    def set_api_header(self, striim_auth_token=None):
        
        self.__api_header = {
            'authorization': f'STRIIM-TOKEN {striim_auth_token}',
            'content-type': 'text/plain'
        } if striim_auth_token else {
            'content-type': 'text/plain'
        }

        self.__session.headers.update(self.__api_header)

    def set_content_type(self, accepts_json=False):
        
        if accepts_json:
            self.__api_header['content-type'] = 'json/application'
        else:
            self.__api_header['content-type'] = 'text/plain'

    def get_base_url(self):
        return self.__base_url