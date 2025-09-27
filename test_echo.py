import requests
import json
import allure


# Генерация отчета Allure с помощью allure-pytest
@pytest.fixture(scope="session", autouse=True)
def setup_allure_report(request):
    request.config.pytest_plugins.append("pytest_allure_adf")


@allure.feature("GET Requests")
@allure.story("Basic Get Request")
@allure.title("Получение данных через GET-запрос")
@allure.description("""
Проверяем простейший GET-запрос, проверяя статус-код и наличие параметра args.
""")
def test_get_request():
    with allure.step("Отправляем GET-запрос"):
        response = requests.get("https://postman-echo.com/get")

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем наличие аргументов"):
        data = response.json()
        assert 'args' in data and isinstance(data['args'], dict), "Нет параметра 'args' или это не словарь"


@allure.feature("POST Requests")
@allure.story("JSON Data Posting")
@allure.title("Передача JSON-данных через POST-запрос")
@allure.description("""
Тестируем отправку JSON-данных в теле POST-запроса.
""")
def test_post_json():
    payload = {'hello': 'world'}
    headers = {'Content-Type': 'application/json'}
    with allure.step("Отправляем POST-запрос с JSON-датами"):
        response = requests.post('https://postman-echo.com/post', json=payload, headers=headers)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем тело ответа"):
        data = response.json()
        assert 'data' in data and data['data'] == payload, f"Ожидался объект {payload}, получен {data['data']}"


@allure.feature("GET Requests")
@allure.story("Query Parameters")
@allure.title("Запрос с параметрами строки")
@allure.description("""
Проверяем GET-запросы с передачей параметров в строку запроса.
""")
def test_get_with_query_params():
    params = {'key': 'value', 'foo': 'bar'}
    with allure.step("Отправляем GET-запрос с параметрами"):
        response = requests.get('https://postman-echo.com/get', params=params)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем параметры в ответе"):
        data = response.json()
        assert 'args' in data and data[
            'args'] == params, f"Параметры в ответе отличаются от ожидаемых. Получено: {data['args']}"


@allure.feature("POST Requests")
@allure.story("Form Data Submission")
@allure.title("Отправка формовых данных через POST")
@allure.description("""
Проверьте, что форма отправляется успешно через POST-запрос.
""")
def test_post_form_data():
    form_data = {'form_field': 'form_value'}
    with allure.step("Отправляем POST-запрос с формами"):
        response = requests.post('https://postman-echo.com/post', data=form_data)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем форму в ответе"):
        data = response.json()
        assert 'form' in data and data[
            'form'] == form_data, f"Данные формы отличаются от ожидаемых. Получено: {data['form']}"


@allure.feature("File Upload")
@allure.story("Multipart File Upload")
@allure.title("Загрузка файлов через Multipart Form Data")
@allure.description("""
Этот тест проверяет успешную загрузку файла через multipart POST-запрос.
""")
def test_post_multipart_file_upload():
    files = {'file': ('example.txt', b'Sample file content')}
    with allure.step("Отправляем файл через POST-запрос"):
        response = requests.post('https://postman-echo.com/post', files=files)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем файлы в ответе"):
        data = response.json()
        assert 'files' in data and len(data['files']) > 0, "Файл не обнаружен в ответе"