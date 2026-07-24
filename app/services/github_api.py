import urllib.request
import urllib.error
import json
from config import Config

github_api_url = ""


def get_repos():

    headers = {
        "Authorization": f"Bearer {Config.GITHUB_API_KEY}",
        "Accept": "application/vnd.github-json",
        "X-Github-Api-Version": "2026-03-10",
        "User-Agent": "PublicPortfolio/1.0",
    }

    request = urllib.request.Request(url=github_api_url, headers=headers, method="GET")

    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())

            return data

    except urllib.error.HTTPError as err:
        return f"An error happened! Error Code: {err.code}, Reason: {err.reason}"

    except urllib.error.URLError as err:
        return f"An error happened! Reason: {err.reason}"
