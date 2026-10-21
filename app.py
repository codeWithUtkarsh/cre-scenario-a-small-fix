"""Search-link service: builds shareable search URLs."""

import requests
from flask import Flask, jsonify, request
from werkzeug.urls import url_quote

app = Flask(__name__)


def search_link(term: str) -> str:
    """Relative URL that searches for `term`."""
    return "/search?q=" + url_quote(term)


@app.get("/link")
def link():
    return jsonify(url=search_link(request.args.get("q", "")))


@app.get("/health")
def health():
    return jsonify(status="ok", http_client=requests.__version__)
