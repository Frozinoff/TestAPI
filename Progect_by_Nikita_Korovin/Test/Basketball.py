import requests
import jsonschema

api_token = "354ae034a6mshfba4ca44ab43425p1da669jsn9d7187c4078f"
basketball_schema = {
    "type": "object",
    "properties": {
        "leagues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string"}
                },
                "required": ["name", "type"]
            }
        }
    },
    "required": ["leagues"]
}

def test_api_basketball():
    url = "https://api-basketball.p.rapidapi.com/leagues"
    headers = {
        "X-RapidAPI-Key": api_token,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    
    json_data = response.json()
    jsonschema.validate(instance=json_data, schema=basketball_schema)

    assert len(json_data["leagues"]) > 0
    for league in json_data["leagues"]:
        assert "name" in league
        assert "type" in league
        assert league["country"]["code"].isalpha()
        assert isinstance(league["type"], str)

    for league in json_data["leagues"]:
        assert league["active"] == True
    
    league_ids = [league["id"] for league in json_data["leagues"]]
    assert len(set(league_ids)) == len(league_ids)

test_api_basketball()