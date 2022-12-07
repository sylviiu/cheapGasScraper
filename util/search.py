import requests
import urllib.parse
import re

def parse(info):
    location = "https://www.google.com/maps/search/gas+in+" + str(urllib.parse.quote(info["city"].replace(" ", "+").lower())) + ",+" + str(urllib.parse.quote(info["state"].replace(" ", "+").lower()))
    req = requests.get(location, headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
    })
    
    responseLn = None

    for ln in req.text.splitlines():
        if responseLn is None and "/Regular" in ln:
            responseLn = ln
    
    responseSplit = ''.join(responseLn.split("[\"gas in ")[:1])

    with open('resp.json', 'w') as f:
        f.write(responseSplit)
    
    regularSplit = responseSplit.split('/Regular')

    locations = []

    for i in range(len(regularSplit)):
        if "SearchResult.TYPE_GAS_STATION" in regularSplit[i-1][:150] :
            obj = {
                "price": re.findall("\d+\.\d+", regularSplit[i-1][-15:])[0],
                "priceFloat": float(re.findall("\d+\.\d+", regularSplit[i-1][-15:])[0]),
                "name": regularSplit[i-1][:150].split("\\\"US\\\",69,84,85,151],")[1].split("\"")[1].split("\"")[0].replace("\\", "")
            }

            if "Sells diesel gas" in regularSplit[i-1][:500]:
                obj["diesel"] = True
            else:
                obj["diesel"] = False

            addresses = regularSplit[i][:1500].split(obj["name"])[1].split("[")

            obj["location"] = { }

            for i in range(len(addresses)):
                if len(addresses[i]) > 5:
                    name = "address"
                    if len(obj["location"]) > 0:
                        name = "address" + str(len(obj["location"])+1)
                    obj["location"][name] = addresses[i].split("\"")[1].split("\"")[0].replace("\\", "")

            locations.append(obj)
    
    return sorted(locations, key=lambda location: location["priceFloat"])