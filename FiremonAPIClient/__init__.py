from FiremonAPIClient.api_interface import APIPlugin
import requests
import json


class Client(APIPlugin):
    headers = {'Content-Type': 'application/json'}
    base_url = None
    token = None

    def connect(self, url: [str, bytes] = '', username: [str, bytes] = '', password: [str, bytes] = ''):
        self.base_url = f'{url.strip("/")}/securitymanager/api'
        response = requests.post(f'{self.base_url}/authentication/login', data=json.dumps({'username': username,
                                                                                           'password': password}),
                                 headers=self.headers, verify=self.verify)
        if response.status_code == 200:
            token = response.json().get('token')
            self.headers = {'Content-Type': 'application/json', 'X-FM-AUTH-Token': token}
            self.token = token
            return response
        return response

    def disconnect(self):
        response = requests.post(f'{self.base_url}/authentication/logout', headers=self.headers, verify=self.verify)
        return response
