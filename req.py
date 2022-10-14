from urllib import response
import requests
def find_most_int(supers):
    heroes = {}
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    dic_ = response.json()
    for el in dic_:
        if el["name"] in supers:
            heroes[el["name"]] = el["powerstats"]["intelligence"]
    print(sorted(heroes.items(), key = lambda item: item[1])[-1][0])


if __name__ == '__main__':
    find_most_int(["Thanos", "Hulk", "Captain America"])
