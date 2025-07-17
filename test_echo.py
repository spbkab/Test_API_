import requests
import json


def test_get_request():
    response = requests.get("https://postman-echo.com/get")
    assert response.status_code == 200
    data = response.json()
    assert 'args' in data and isinstance(data['args'], dict), "No args or not a dictionary."


def test_post_json():
    payload = {'hello': 'world'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://postman-echo.com/post', json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data and data['data'] == json.dumps(payload), f"Expected {json.dumps(payload)}, got {data['data']}."


def test_get_with_query_params():
    params = {'key': 'value', 'foo': 'bar'}
    response = requests.get('https://postman-echo.com/get', params=params)
    assert response.status_code == 200
    data = response.json()
    assert 'args' in data and data['args'] == params, f"Arguments mismatch. Expected {params}, got {data['args']}."


def test_post_form_data():
    form_data = {'form_field': 'form_value'}
    response = requests.post('https://postman-echo.com/post', data=form_data)
    assert response.status_code == 200
    data = response.json()
    assert 'form' in data and data['form'] == form_data, f"Form data mismatch. Expected {form_data}, got {data['form']}."


def test_post_multipart_file_upload():
    files = {'file': ('example.txt', b'Sample file content')}
    response = requests.post('https://postman-echo.com/post', files=files)
    assert response.status_code == 200
    data = response.json()
    assert 'files' in data and len(data['files']) > 0, "Files section is missing or empty."