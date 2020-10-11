import requests
import json

def get():
    requestst.get('http://httpbin.org/status/204').status_code

def post():
    url= 'http://httpbin.org/post'
    sendin = { 'x':'1', 'y':'2' }
    return requests.post(url, sendin)
