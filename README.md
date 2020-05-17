# API-Wrapper-Boilerplate

An API Wrapper for Firemon to be able to easily use the API in a more standard way.

## How to install
```ignorelang
$ pip install FiremonAPIWrapper
```

## Usage

#### Import and instantiate the class
```python
from FiremonAPIWrapper import Wrapper

client = Wrapper(verify=False, warnings=False, api_version='v1')
```

#### Connect and Disconnect
```python
from FiremonAPIWrapper import Wrapper

client = Wrapper(verify=False)

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

client.disconnect()
```
