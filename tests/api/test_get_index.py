import allure
import jsonschema
from allure_commons.types import Severity

from zonatelecom_demo_project.utils.json_schema_utils import load_schema


@allure.title('GET index. Валидация схемы ответа')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_index_schema_is_valid(api_get_index):
    with allure.step('Подгрузка схемы для валидации ответа'):
        schema = load_schema('index.json')

    response = api_get_index

    with allure.step('Ответ по запросу совпадация с валидационной схемой'):
        jsonschema.validate(response.json(), schema)


@allure.title('GET index. Статус код равен 200')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_index_status_code_is_200(api_get_index):
    response = api_get_index

    with allure.step('Статус-код равен 200'):
        assert response.status_code == 200


@allure.title('GET index. В ответе присутствуют заголовки')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_index_headers_are_not_empty(api_get_index):
    response = api_get_index

    with allure.step('В ответе присутствуют заголовки'):
        assert response.headers


@allure.title('GET index. Время получения ответа не превышает 1 секунды')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_get_index_response_time_is_valid(api_get_index):
    response = api_get_index

    with allure.step('Время получения ответа не превышает 1 секунды'):
        assert response.elapsed.total_seconds() < 1
