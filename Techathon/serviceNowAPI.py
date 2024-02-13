import json
import requests
from requests.auth import HTTPBasicAuth

def createINC(short_desc,desc):
    auth = HTTPBasicAuth("admin", "LYlI59w=r*sB")
    uri = "https://dev93933.service-now.com/api/now/table/incident"

    headers = {
        "Accept": "application/json;charset=utf-8",
        "Content-Type": "application/json"
    }

    payload = {
        "sysparm_action": "insert",
        "category": "Infrastructure",
        "impact": "1",
        "urgency": "2",
        "short_description": short_desc,
        "description": desc,
        "caller_id": "Satcom Bot"

    }

    r = requests.post(url=uri, data=json.dumps(payload), auth=auth, verify=False, headers=headers)
    content = r.json()
    if r.status_code == 201:
        return content['result']['task_effective_number']
    else:
        return "Response Status Code: " + str(r.status_code)





