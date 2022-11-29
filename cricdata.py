import requests


def make_get_call(url):
    print("Hello VNS")
    return requests.get(url).json()
def get_India_series():
    data1 = make_get_call("https://api.cricapi.com/v1/series?apikey=2b3e809c-021f-448b-8403-8417effeef22&offset=0")
    flag = False
    print(data1)
    for series in data1["data"]:
        if "India" in series["name"]:
            return True
    return False

def get_India_series1():
    data1 = requests.get("https://api.cricapi.com/v1/series?apikey=2b3e809c-021f-448b-8403-8417effeef22&offset=0")
    data1 = data1.json()
    print(data1)
    for series in data1["data"]:
        if "India" in series["name"]:
            return True
    return False

if __name__ == "__main__":
    get_India_series()