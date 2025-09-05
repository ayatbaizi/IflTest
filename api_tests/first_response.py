import requests

HOST = "https://apigate-dev.inguru.dev/property-insurance-service"

response = requests.post(
    url= f"{HOST}//public/company",
    headers={"Authorization": "ING ffffeeeee55555"}
)

print(response.json(), response.status_code)
