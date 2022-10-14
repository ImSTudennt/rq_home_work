import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def upload(self, file_path, file_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'
        }
        params = {"path": file_path, "overwrite": "true"}
        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        href = result.get('href', '')
        response = requests.put(href, data=open(file_name, "rb"))
        if response.status_code == 201:
            print("Успешно")


if __name__ == '__main__':
    token = "y0_A___"
    uploader = YaUploader(token)
    result = uploader.upload("test1006.txt", "H_W.txt")
    print(result)