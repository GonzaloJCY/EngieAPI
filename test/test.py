from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Engie Fast API"}


def test_convert():
    body = {"list": ["A","a","x","X","Q","k","R","B","b","G","H","i","j","J"]}
    body = json.dumps(body)
    response = client.post('/convert', data=body)

    assert response.content == b'{"result_list":[650,970,0,0,0,0,0,660,980,710,0,0,0,0]}'
    assert response.status_code == 200

