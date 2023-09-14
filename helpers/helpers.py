import requests
from bs4 import BeautifulSoup as bs
import json


def dev_soup(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    return bs(page.text, "lxml")


def fix_title(title: list) -> str:
    return " ".join(title)


def write_to_file(dic: dict) -> None:
    with open("data/Results.csv", "a") as f:
        f.write(str(dic))
        f.write("\n")


def write_to_json(dic: dict) -> None:
    with open("data/Results.json", "a") as g:
        json.dump(dic, g, indent=4)


def dump_to_json(results: list()) -> None:
    for dic in results:
        with open("data/Results_final.json", "w") as out:
            json.dump(results, out, indent=4)
