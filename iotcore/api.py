import requests

def request(url, method="get", headers=None, response_type="json", data=None, debug=False):
    response = None
    if debug:
        print(url)
        if data:
            print(data)
    if method == "get":
        response = requests.get(url, headers=headers)
    if method == "post":
        response = requests.post(url, headers=headers, data=data)
        if debug:
            print(response.status_code)
            print(response.text)
    if response_type == "json":
        response = response.json()
    if response_type == "text":
        response = response.text
    return response
