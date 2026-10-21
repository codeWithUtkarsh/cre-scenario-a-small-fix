# Scenario A: small code change

Vulnerable Flask, Werkzeug, and requests. Updating Werkzeug to 3.x removes
`werkzeug.urls.url_quote`, which `app.py` uses: a one-line fix.

Expected: one PR that updates the dependencies, fixes the import, and lists the
CVEs it resolves.
