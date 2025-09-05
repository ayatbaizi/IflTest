from api_tests.api.endpoints import Endpoints
from api_tests.api.payloads import Payloads

#Получение списка компаний
def test_get_company_list(api_client, auth_headers):
    response = api_client.get(Endpoints.get_company_list(), headers=auth_headers)

    #Проверки
    assert response.status_code == 200
    assert response, "Ответ пустой"
    assert isinstance(response, list), "Ожидался список компаний"
    assert "id" in response[0], "Нет поля id в объекте компании"
    assert "products" in response[0], "Нет products у компании"


#Запрос на калькуляцию в СК
def test_post_policy_calc(api_client, auth_headers):
    # Получение списка компаний
    companies = api_client.get(Endpoints.get_company_list(), headers=auth_headers)

    # Из списка компаний берем параметры, что бы прокинуть в запрос за калькуляцию
    company = companies[0]
    company_id = company["id"]
    product = company["products"][0]["id"]

    # Формирование тела запроса
    payload = Payloads.policy_calc(product=product)

    # Запрос на калькуляцию в СК
    response = api_client.post(
        Endpoints.make_policy_calc(company_id),
        json=payload,
        headers=auth_headers
    )
    #Проверки
    assert response.status_code == 200
    assert "price" in response, "В ответе нет параметра 'price'"
    assert int(response["partnerKv"]) > 0, "partnerKv должно быть больше 0"

