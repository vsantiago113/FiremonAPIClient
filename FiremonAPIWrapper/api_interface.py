import requests
from requests.auth import HTTPBasicAuth
import urllib3
import inspect
from abc import ABCMeta, abstractmethod


class APIPlugin(metaclass=ABCMeta):
    def __init__(self, verify: bool = False, warnings: bool = False, api_version: [str, bytes] = 'v1'):
        """
        The APIPlugin is the foundation to creating API Plugins from many different vendors. The APIPlugin help you
        create the most dynamic API Wrapper possible with minimal coding in few different ways. The APIPlugin is design
        to work with the RESTful API designs most used by developers specially in the Network Field.
        :param verify: SSL Cert verification, default to False to not verify SSL Cert.
        :param warnings: Request Warnings, default to False to disable all warnings.
        :param api_version: The version of the API as a string, defaults to v1.
        """
        self.verify = bool(verify)
        self.api_version = api_version
        if warnings is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @property
    @abstractmethod
    def headers(self):
        """
        The HTTP Headers as a python dictionary
        :return:
        """
        pass

    @property
    @abstractmethod
    def base_url(self):
        """
        The Base URL will be the namespace of the URL that will be the same across all the API calls.
        :return:
        """
        pass

    @abstractmethod
    def connect(self, url: [str, None] = None, username: [str, bytes] = '',
                password: [str, bytes] = '') -> requests.Response:
        """
        The way to connect to the API by authenticating and generating tokens.
        :param url: The URL of the resource you are trying to access.
        :param username: The username of the system you are trying to authenticate.
        :param password: The password of the system you are trying to authenticate.
        :return:
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        The way to disconnect from the API by revoking tokens or logging out of the session.
        :return:
        """
        pass

    def get(self, url: [str, None] = None, method: [str, bytes] = '', data: dict = None, auth: HTTPBasicAuth = None,
            **kwargs) -> requests.Response:
        """

        :param url: The URL of the resource you are trying to access. Defaults to base_url + method.
        :param method: The method is the part of the url that changes and is appended to basic_url.
        :param data: The data to change or update as a Python dictionary. Defaults to None.
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None.
        :param kwargs: All parameters required by the API call.
        :return: The requests.Response of the API call.
        """
        http_method = inspect.stack()[0][3].upper()
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        return requests.request(http_method, url, headers=self.headers, verify=self.verify, json=data,
                                auth=auth, params=kwargs)

    def post(self, url: [str, None] = None, method: [str, bytes] = '', data: dict = None, auth: HTTPBasicAuth = None,
             **kwargs) -> requests.Response:
        """

        :param url: The URL of the resource you are trying to access. Defaults to base_url + method.
        :param method: The method is the part of the url that changes and is appended to basic_url.
        :param data: The data to change or update as a Python dictionary. Defaults to None.
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None.
        :param kwargs: All parameters required by the API call.
        :return: The requests.Response of the API call.
        """
        http_method = inspect.stack()[0][3].upper()
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        return requests.request(http_method, url, headers=self.headers, verify=self.verify, json=data,
                                auth=auth, params=kwargs)

    def put(self, url: [str, None] = None, method: [str, bytes] = '', data: dict = None, auth: HTTPBasicAuth = None,
            **kwargs) -> requests.Response:
        """

        :param url: The URL of the resource you are trying to access. Defaults to base_url + method.
        :param method: The method is the part of the url that changes and is appended to basic_url.
        :param data: The data to change or update as a Python dictionary. Defaults to None.
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None.
        :param kwargs: All parameters required by the API call.
        :return: The requests.Response of the API call.
        """
        http_method = inspect.stack()[0][3].upper()
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        return requests.request(http_method, url, headers=self.headers, verify=self.verify, json=data,
                                auth=auth, params=kwargs)

    def delete(self, url: [str, None] = None, method: [str, bytes] = '', data: dict = None, auth: HTTPBasicAuth = None,
               **kwargs) -> requests.Response:
        """

        :param url: The URL of the resource you are trying to access. Defaults to base_url + method.
        :param method: The method is the part of the url that changes and is appended to basic_url.
        :param data: The data to change or update as a Python dictionary. Defaults to None.
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None.
        :param kwargs: All parameters required by the API call.
        :return: The requests.Response of the API call.
        """
        http_method = inspect.stack()[0][3].upper()
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        return requests.request(http_method, url, headers=self.headers, verify=self.verify, json=data,
                                auth=auth, params=kwargs)

    def get_method1_x(self, *args, url: [str, None] = None, data: dict = None,
                      auth: HTTPBasicAuth = None, placeholder: [str, bytes] = 'x',
                      split_method: [str, bytes, None] = '_', **kwargs) -> requests.Response:
        """

        :param args: The arguments are specific URL methods withing the method for example device_id or UUID fields.
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method.
        :param data: The data to change or update as a Python dictionary. Defaults to None.
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None.
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Used to split the class method name to build the URL method. Defaults to '_' underscore.
        :param kwargs: All parameters required by the API call.
        :return: The requests.Response of the API call.
        """
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)
