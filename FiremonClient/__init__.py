import requests
import json
import urllib3


class FiremonError(Exception):
    pass


class FiremonAuthError(Exception):
    pass


class Client:
    def __init__(self, verify=bool(), warnings=bool(), api_version='v1'):
        self.verify = bool(verify)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) if warnings is False else None

        self.api_version = api_version
        self.headers = {'Content-Type': 'application/json'}
        self.server = None
        self.token = None
        self.base_url = None
        self.username = None
        self.password = None

    def connect(self, server=str(), username=str(), password=str()):
        self.server = server.replace('https://', '').replace('http://', '').strip('/')
        self.username = username
        self.password = password
        url = ('https://{}/securitymanager/api/authentication/login'.format(server))
        _response = requests.post(url, headers=self.headers, data=json.dumps({'username': username,
                                                                              'password': password}),
                                  verify=self.verify)

        if _response.status_code in [200]:
            token = _response.json().get('token')
            self.token = token
            self.base_url = 'https://{}/securitymanager/api'.format(server, self.api_version)
            self.headers.update({'X-FM-AUTH-Token': token})
            return _response.status_code
        elif _response.status_code == 401:
            raise FiremonAuthError('Authentication Error!')
        else:
            raise FiremonError('HTTP Error,  Status Code: {}'.format(_response.status_code))

    def close(self):
        url = ('{}/{}'.format(self.base_url, 'authentication/logout'))
        __response = requests.post(url, headers=self.headers, verify=False)
        return __response.status_code

    def get(self, method=str(), **kwargs):
        response = requests.get('{}/{}'.format(self.base_url.strip('/'), method), headers=self.headers,
                                verify=self.verify, params=kwargs)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)

    def add(self, method: str, data: dict) -> dict:
        response = requests.post('{}/{}'.format(self.base_url.strip('/'), method), headers=self.headers,
                                 verify=self.verify, json=data)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)

    def update(self, method: str, data: dict) -> dict:
        response = requests.put('{}/{}'.format(self.base_url.strip('/'), method), headers=self.headers,
                                verify=self.verify, json=data)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)

    def delete(self, method: str) -> dict:
        response = requests.delete('{}/{}'.format(self.base_url.strip('/'), method), headers=self.headers,
                                   verify=self.verify)
        if response.status_code in [200]:
            return response.json()
        else:
            raise FiremonError(response.status_code)
