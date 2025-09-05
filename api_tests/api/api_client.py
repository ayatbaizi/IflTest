import requests
#обертка над request
class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params=None, headers=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)
        return response.json()

    def post(self, endpoint: str, json=None, headers=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=json, headers=headers)
        return response.json()