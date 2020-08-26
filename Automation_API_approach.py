import gevent.monkey
gevent.monkey.patch_all()
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests


openURL = "https://www.autohero.com/de/search/"
searchURL = "https://www.autohero.com/de/api/v1/search-template/classified/findAds/v2"
operationsPayload = {"meta":{"fields":["firstRegistrationYear","offerPrice"],"from":0,"locale":"de-de","location":{"countries":["DE"],"locations":[]},"published":True,"registrationDate":{"from":2015},"sellerType":[3],"size":900,"sort":[{"field":"sellerType","direction":"desc"},{"field":"offerPrice.amountMinorUnits","direction":"desc"}],"retailAdState":["imported-to-retail","reserved"]}}


def iterate_API(d):
    old_price = 0
    for k, v in d.items():
        if k == "hits" and isinstance(v, list):
            for index, item in enumerate(v):
                current_price = item["_source"]["offerPrice"]["amountMinorUnits"]
                current_registration_year = item["_source"]["firstRegistrationYear"]
                if current_registration_year < 2015:
                    raise Exception(f'First registration year {current_registration_year} is earlier than 2015! Filtering failed.')
                elif old_price < current_price and index != 0:
                    raise Exception(f'The price of {index} element - {current_price} is higher than {index-1} element - {old_price}. Descending sorting failed.')
                else:
                    old_price = int(current_price)
        elif isinstance(v, dict):
            iterate_API(v)


def main():
    with requests.Session() as s:
        getPage = s.get(openURL, timeout=10)
        s.cookies = getPage.cookies
        queryData = s.post(searchURL, json=operationsPayload, timeout=10)
        iterate_API(queryData.json())


main()