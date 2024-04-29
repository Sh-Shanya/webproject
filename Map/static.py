import sys
import requests


def get_image(name, size, ll, spn, l):

    map_params = {
        "ll": ll,
        "spn": f"{str(spn)},{str(spn)}",
        "l": l,
        "size": size,
        "pt": ll + "," + "pm2rdm",
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    with open(name, "wb") as f:
        f.write(response.content)
    return
