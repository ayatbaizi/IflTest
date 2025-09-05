import pytest
from api.api_client import ApiClient

HOME = "https://apigate-dev.inguru.dev/property-insurance-service"
TOKEN = "ffffeeeee55555"

@pytest.fixture(scope="session")
def base_url():
    return HOME

@pytest.fixture(scope="session")
def token():
    return TOKEN

@pytest.fixture(scope="session")
def api_client(base_url):
    return ApiClient(base_url=base_url)

@pytest.fixture(scope="session")
def auth_headers(token):
    return {"Authorization": f"ING {token}"}
