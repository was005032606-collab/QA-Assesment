import requests

def test_stake_below_minimum_returns_422(api_base_url, api_headers):

    payload = {
        "matchId": "premier-league-manutd-chelsea",
        "selection": "HOME",
        "stake": 0.50
    }
    response = requests.post(
        f"{api_base_url}/place-bet",
        json=payload,
        headers=api_headers
    )
    assert response.status_code == 422
    body = response.json()
    assert "stake" in body.get("message", "").lower() or "minimum" in str(body).lower()
