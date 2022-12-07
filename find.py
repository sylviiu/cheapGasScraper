import json
from util import payloadItem, search

info = {
    "city": payloadItem.get("City?"),
    "state": payloadItem.get("Two letter state code?", 2).upper(),
}

locations = search.parse(info)

print("Found " + str(len(locations)) + " location(s) for " + info["city"][0].upper() + info["city"][1:] + ", " + info["state"])

for location in locations:
    print("-" * 40)
    print("| Name: " + location["name"])
    print("| Price: $" + location["price"])
    print("| Sells diesel? " + str(location["diesel"]))

    for addr in location["location"].values():
        print("| - " + addr)

print("-" * 40)