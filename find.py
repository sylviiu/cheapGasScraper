import json
from util import payloadItem

info = {
    "state": payloadItem.get("Two letter state code?", 2).upper(),
    "city": payloadItem.get("City?"),
}