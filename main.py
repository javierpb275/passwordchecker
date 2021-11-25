import requests

if __name__ == '__main__':
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA' #hashed password
    res = requests.get(url)
    print(res)#<Response [200]>