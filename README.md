# FiremonAPIWrapper
![PyPI - Status](https://img.shields.io/pypi/status/FiremonAPIWrapper)
![PyPI - Format](https://img.shields.io/pypi/format/FiremonAPIWrapper)
![GitHub](https://img.shields.io/github/license/vsantiago113/Firemon-API-Wraper)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/vsantiago113/Firemon-API-Wraper)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/FiremonAPIWrapper)

An API Wrapper for Firemon to be able to easily use the API in a more standard way.

## How to install
```ignorelang
$ pip install FiremonAPIWrapper
```

## Usage
the argument "method" must be specify everytime. Look at authentication validation for an example.

#### Default arguments and attributes
```python
from FiremonAPIWrapper import Wrapper

client = Wrapper(verify=False, warnings=False, api_version='v1')

client.get(url=None, method='', data=None, auth = None)

# client.headers
# client.url_base
# client.token

```

#### Import and instantiate the class
```python
from FiremonAPIWrapper import Wrapper

client = Wrapper()
```

#### Connect, Validate authentication and Disconnect
```python
from FiremonAPIWrapper import Wrapper
import json

client = Wrapper()

client.connect(url='https://firemon-server.local', username='admin', password='Admin123')

response = client.post(method='/authentication/validate', data={'username': 'admin', 'password': 'Admin123'})
print(json.dumps(response.json(), indent=4), response.status_code, response.reason)

client.disconnect()
```

#### How to get an object
```python
from FiremonAPIWrapper import Wrapper
import json

client = Wrapper()
client.connect(url='https://firemon-server.local', username='admin', password='Admin123')

domain_id = 1
group_name = 'mytestgroup'
response = client.get(method=f'/domain/{domain_id}/usergroup/name/{group_name}')
print(json.dumps(response.json(), indent=4), response.status_code, response.reason)

client.disconnect()
```

#### How to create an object
```python
from FiremonAPIWrapper import Wrapper
import json

client = Wrapper()
client.connect(url='https://firemon-server.local', username='admin', password='Admin123')

domain_id = 1
group_name = 'mytestgroup'
response = client.post(method=f'/domain/{domain_id}/usergroup', domainId=domain_id, data={
            "name": group_name, "description": "This group is a test and can be deleted"})
print(json.dumps(response.json(), indent=4), response.status_code, response.reason)

client.disconnect()
```

#### How to update an object
```python
from FiremonAPIWrapper import Wrapper
import json

client = Wrapper()
client.connect(url='https://firemon-server.local', username='admin', password='Admin123')

domain_id = 1
group_id = 123
group_name = 'mytestgroup'
response = client.put(method=f'/domain/{domain_id}/usergroup/{group_id}', domainId=domain_id, id=group_id,
                      data={"id": group_id, "domainId": domain_id, "name": group_name,
                            "description": "This group is a test and it has been updated and can be deleted"})
print(response.status_code, response.reason)

client.disconnect()
```

#### How to delete an object
```python
from FiremonAPIWrapper import Wrapper
import json

client = Wrapper()
client.connect(url='https://firemon-server.local', username='admin', password='Admin123')

domain_id = 1
group_id = 123
response = client.delete(method=f'/domain/{domain_id}/usergroup/{group_id}', domainId=domain_id, id=group_id)
print(response.status_code, response.reason)

client.disconnect()
```
