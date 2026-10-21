from app import app, search_link


def test_search_link_escapes_term():
    assert search_link("a b&c") == "/search?q=a%20b%26c"


def test_link_endpoint():
    client = app.test_client()
    assert client.get("/link?q=hello world").get_json() == {"url": "/search?q=hello%20world"}


def test_health():
    assert app.test_client().get("/health").get_json()["status"] == "ok"
