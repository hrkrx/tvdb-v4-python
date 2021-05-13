import json
import urllib.parse
import urllib.request
from urllib.request import urlopen

url = "http://localhost:8081/v4/login"


class Auth:
    def __init__(self, url, apikey, pin=""):
        loginInfo = {"apikey": apikey}
        if pin != "":
            loginInfo["pin"] = pin

        loginInfoBytes = json.dumps(loginInfo, indent=2).encode('utf-8')
        req = urllib.request.Request(url, data=loginInfoBytes)
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, data=loginInfoBytes) as response:
            res = json.load(response)
            self.token = res["data"]["token"]
            print(self.token)
