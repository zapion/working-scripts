from requests import request
from pprint import pprint
import json

data = {"httpRequest": {"path": "/videopass"},
        "httpResponse": {"body": "hello world again"},
        }

path = {'path': "/videopass"}

response = request("PUT", 'http://localhost:1080/mockserver/clear', data=json.dumps(path))
pprint(response)
response = request("PUT", "http://localhost:1080/mockserver/expectation",
        data=json.dumps(data))

pprint(response)
