import requests

def test_bored_api():
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url)
    
    assert response.status_code == 200
    
    json_data = response.json()
    assert "activity" in json_data
    assert json_data["activity"]
    assert "type" in json_data
    assert isinstance(json_data["type"], str)
    assert "participants" in json_data
    assert isinstance(json_data["participants"], int)
    assert "price" in json_data
    assert isinstance(json_data["price"], float)

    if json_data["type"] == "education":
        assert "link" in json_data
    
    assert json_data["price"] >= 0

test_bored_api()