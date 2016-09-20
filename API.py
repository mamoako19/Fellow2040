import json
import requests


token = '621832798146c18af38c708fbe9be2b4'
github = 'https://github.com/mamoako19/Fellow2040'

def step_1(): 
    json_string = {'token': token,
               'github':github}

    r = requests.post('http://challenge.code2040.org/api/register', json = json_string)
    print r.text 

def step_2():
    original_str = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': token}).text
    rev = original_str[::-1]
    r = requests.post('http://challenge.code2040.org/api/reverse/validate', json = {'token': token, 'string': rev})
    print r.text

def step_3():
    response = requests.post('http://challenge.code2040.org/api/haystack', data = {'token': token})
    dict_v = json.loads(response.text)
    index = dict_v["haystack"].index(dict_v["needle"])
    r = requests.post('http://challenge.code2040.org/api/haystack/validate', json = {'token': token, 'needle': index})
    print r.text

def step_4():
    response = requests.post('http://challenge.code2040.org/api/prefix', data = {'token': token})
    dict_v = json.loads(response.text)
    len_p = len(dict_v['prefix'])
    prefix = dict_v['prefix']
    array = [str(x) for x in dict_v['array'] if len(x) >= len_p and x[:len_p] != prefix]
    data2 = {'token': token, 'array': array}
    r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = data2)

    
def step_5():
    response = requests.post('http://challenge.code2040.org/api/dating', data = {'token': token})
    dict_v = json.loads(response.text)
    print dict_v


step_5() 
