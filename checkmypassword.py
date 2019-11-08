import requests
import hashlib

def request_api_data(query_char: str)->str:
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check and try again')
    return res

def pwned_api_check(password: str):
    sha1password = hashlib.sha1(password.encode('utf-8'))
    #Save 5 chars of the password and in tail remaining chars
    first5_chars, tail = sha1password[:5],sha1password[5:]
    response = request_api_data(first5_chars)
    print(first5_chars,tail)
    return response

#request_api_data('123')
pwned_api_check('123')
