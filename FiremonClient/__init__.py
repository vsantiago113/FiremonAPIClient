import requests
import json
import urllib3


class FiremonError(Exception):
    pass


class FiremonAuthError(Exception):
    pass


class Client:
    def __init__(self, verify=False, headers=None, server=None, token=None):
        self.verify = bool(verify)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if headers:
            self.headers = headers
        else:
            if token:
                self.headers = {'Content-Type': 'application/json', 'X-FM-AUTH-Token': token}
            else:
                self.headers = {'Content-Type': 'application/json'}

        self.server = server
        self.token = token

    def connect(self, server='', username='', password=''):
        self.server = server.replace('https://', '').replace('http://', '').strip('/')
        url = ('https://{}/securitymanager/api/authentication/login'.format(server))
        _response = requests.post(url, headers=self.headers,
                                  data=json.dumps({'username': username, 'password': password}), verify=self.verify)

        if _response.status_code in [200]:
            token = _response.json().get('token')
            self.headers = {'Content-Type': 'application/json', 'X-FM-AUTH-Token': token}
            self.token = token
            return _response.status_code
        elif _response.status_code == 401:
            raise FiremonAuthError('Authentication Error!')
        else:
            raise FiremonError('HTTP Error,  Status Code: {}'.format(_response.status_code))

    def close(self):
        url = ('{}/{}'.format('https://{}/securitymanager/api'.format(self.server).strip('/'), 'authentication/logout'))
        __response = requests.post(url, headers=self.headers, verify=False)
        return __response.status_code

    def get(self, method=str(), **kwargs):
        response = requests.get('{}/{}'.format('https://{}/securitymanager/api'.format(self.server).strip('/'), method),
                                headers=self.headers, verify=self.verify, params=kwargs)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)

    def add(self, method: str, data: dict) -> dict:
        response = requests.post('{}/{}'.format('https://{}/securitymanager/api'.format(self.server).strip('/'),
                                                method), headers=self.headers, verify=self.verify, json=data)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)

    def update(self, method: str, data: dict) -> dict:
        response = requests.put('{}/{}'.format('https://{}/securitymanager/api'.format(self.server).strip('/'), method),
                                headers=self.headers, verify=self.verify, json=data)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)

    def delete(self, method: str) -> dict:
        response = requests.delete('{}/{}'.format('https://{}/securitymanager/api'.format(self.server).strip('/'),
                                                  method), headers=self.headers, verify=self.verify)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)
