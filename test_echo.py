import requests
import json


def test_get_request():
    """Проверяет базовое получение данных через GET."""
    response = requests.get("https://postman-echo.com/get")
    assert response.status_code == 200
    data = response.json()
    assert 'args' in data and isinstance(data['args'], dict), "Нет параметра 'args' или это не словарь"


def test_post_json():
    """Тестирует передачу JSON-данных в теле POST-запроса."""
    payload = {'hello': 'world'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://postman-echo.com/post', json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    # Используем прямое сравнение объектов
    assert 'data' in data and data['data'] == payload, f"Ожидался объект {payload}, получен {data['data']}"

def test_get_with_query_params():
    """Тестирует GET-запрос с параметрами в строке запроса."""
    params = {'key': 'value', 'foo': 'bar'}
    response = requests.get('https://postman-echo.com/get', params=params)
    assert response.status_code == 200
    data = response.json()
    assert 'args' in data and data['args'] == params, f"Параметры в ответе отличаются от ожидаемых. Получено: {data['args']}"


def test_post_form_data():
    """Тестирует POST-запрос с формой данных."""
    form_data = {'form_field': 'form_value'}
    response = requests.post('https://postman-echo.com/post', data=form_data)
    assert response.status_code == 200
    data = response.json()
    assert 'form' in data and data['form'] == form_data, f"Данные формы отличаются от ожидаемых. Получено: {data['form']}"


def test_post_multipart_file_upload():
    """Тестирует загрузку файла через multipart/form-data."""
    files = {'file': ('example.txt', b'Sample file content')}
    response = requests.post('https://postman-echo.com/post', files=files)
    assert response.status_code == 200
    data = response.json()
    assert 'files' in data and len(data['files']) > 0, "Файл не обнаружен в ответе"