import requests
import hashlib

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Erorr fetching: {res.status_code}", "check api and try again.")
    return res

def password_api_check(password):


# request_api_data("password123")