from FiremonAPIWrapper import Wrapper
import unittest
import os
import json

url = 'https://firemon-server.local'
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
domain_id = 1


def run_full_test():
    test_group = 'mytestgroup'

    client = Wrapper()

    print(f'***** Testing: Login '.ljust(60, '*'))
    response = client.connect(url, username, password)
    print('Authentication: Login', response.status_code, response.reason, '\n')

    print(f'***** Testing: Login Validation '.ljust(60, '*'))
    response = client.post(method='/authentication/validate', data={'username': username, 'password': password})
    print('Authentication: Validation', response.status_code, response.reason, '\n')

    print(f'***** Testing: GET method by getting current user '.ljust(60, '*'))
    response = client.get(method='/user/current')
    print(json.dumps(response.json(), indent=4), response.status_code, response.reason, '\n')

    print(f'***** Testing: GET method by checking if group already exists '.ljust(60, '*'))
    response = client.get(method=f'/domain/{domain_id}/usergroup/name/{test_group}')
    group_data = response.json()
    if response.status_code == 404:
        print(f'Group {test_group} does not exists, lets create it')

        print(f'***** Testing: POST method by a new group '.ljust(60, '*'))
        response = client.post(method=f'/domain/{domain_id}/usergroup', domainId=domain_id, data={
            "name": test_group,
            "description": "This group is a test and can be deleted"})
        group_data = response.json()
        print(json.dumps(response.json(), indent=4), response.status_code, response.reason, '\n')

        print(f'***** Testing: PUT method by a updating the group description '.ljust(60, '*'))
        response = client.put(method=f'/domain/{domain_id}/usergroup/{group_data.get("id")}', domainId=domain_id,
                              id=group_data.get('id'), data={"id": group_data.get('id'), "domainId": domain_id,
                                                             "name": "mytestgroup",
                                                             "description": "This group is a test and it has been "
                                                                            "updated and can be deleted"})
        if response.status_code == 204:
            print(response.status_code, response.reason, '\n')
        else:
            print(json.dumps(response.json(), indent=4), response.status_code, response.reason, '\n')

        print(f'***** Testing: GET method by confirming our change '.ljust(60, '*'))
        response = client.get(method=f'/domain/{domain_id}/usergroup/name/{test_group}')
        print(json.dumps(response.json(), indent=4), response.status_code, response.reason, '\n')

        print(f'***** Testing: DELETE method by deleting the test group '.ljust(60, '*'))
        response = client.delete(method=f'/domain/{domain_id}/usergroup/{group_data.get("id")}', domainId=domain_id, 
                                 id=group_data.get('id'))
        if response.status_code == 204:
            print(response.status_code, response.reason, '\n')
        else:
            print(json.dumps(response.json(), indent=4), response.status_code, response.reason, '\n')
    else:
        print(json.dumps(group_data, indent=4), response.status_code, response.reason, '\n')

        print(f'***** Testing: DELETE method by deleting the test group '.ljust(60, '*'))
        response = client.delete(method=f'/domain/{domain_id}/usergroup/{group_data.get("id")}', domainId=domain_id, 
                                 id=group_data.get('id'))
        if response.status_code == 204:
            print(response.status_code, response.reason, '\n')
        else:
            print(json.dumps(response.json(), indent=4), response.status_code, response.reason, '\n')

    print(f'***** Testing: Logout '.ljust(60, '*'))
    response = client.disconnect()
    print('Authentication: Logout', response.status_code, response.reason, '\n')


class TestFiremonAPIWrapper(unittest.TestCase):

    def test_authentication(self):
        client = Wrapper()

        response = client.connect(url, username, password)
        self.assertEqual(response.status_code, 200)

        response = client.post(method='/authentication/validate', data={'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)

        response = client.disconnect()
        self.assertEqual(response.status_code, 204)
        
    def test_methods_get_put_post_delete(self):
        group_name = 'mytestgroup'
        
        client = Wrapper()
        client.connect(url, username, password)

        response = client.post(method=f'/domain/{domain_id}/usergroup', domainId=domain_id, data={
            "name": group_name, "description": "This group is a test and can be deleted"})
        self.assertEqual(response.status_code, 200)
        group_id = response.json().get('id')

        response = client.put(method=f'/domain/{domain_id}/usergroup/{group_id}', domainId=domain_id, id=group_id,
                              data={"id": group_id, "domainId": domain_id, "name": "mytestgroup",
                                    "description": "This group is a test and it has been updated and can be deleted"})
        self.assertEqual(response.status_code, 204)

        response = client.get(method=f'/domain/{domain_id}/usergroup/name/{group_name}')
        self.assertEqual(response.status_code, 200)

        response = client.delete(method=f'/domain/{domain_id}/usergroup/{group_id}', domainId=domain_id, id=group_id)
        self.assertEqual(response.status_code, 204)

        client.disconnect()


if __name__ == '__main__':
    unittest.main()
