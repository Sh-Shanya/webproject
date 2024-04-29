import requests


class Get:
    def __init__(self, a):
        self.geocoder_request = "https://geocode-maps.yandex.ru/1.x"
        self.data = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "format": "json",
            "geocode": a,
        }
        self.res = requests.get(self.geocoder_request, self.data).json()
        self.obj = self.res["response"]["GeoObjectCollection"]["featureMember"][0][
            "GeoObject"
        ]

    def Get_Coords(self):
        return str(self.obj["Point"]["pos"]).replace(" ", ",")

    def Get_Index(self):
        return (
            self.res.get("response")
            .get("GeoObjectCollection")
            .get("featureMember")[0]
            .get("GeoObject")
            .get("metaDataProperty")
            .get("GeocoderMetaData")
            .get("Address")
            .get("postal_code")
        )

    def Get_Adress(self):
        return self.obj["metaDataProperty"]["GeocoderMetaData"]["text"]

    def get_spn(self):
        coords = list(self.obj.get("boundedBy").get("Envelope").values())
        x1, y1 = map(float, coords[0].split())
        x2, y2 = map(float, coords[1].split())
        return f"{abs(x2 - x1)},{abs(y2 - y1)}"

