import json
import requests
import datetime 

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
    array = dict_v['datestamp'].split('-')
    r_val = array[-1]
    array.remove(r_val) 
    array_2 = r_val.split(':')
    t_val = array_2[0]
    array_2.remove(t_val) 
    array_3 = t_val.split('T')
    for i in array_3:
        array.append(i)
    for i in array_2:
        array.append(i)
    array[-1] = array[-1][:-1]
    for i in range(len(array)):
        array[i] = int(array[i]) 
    if array[1] in [9, 4, 6, 11]:
        days_in_month = 30
    else:
        if array[1] == 2:
            days_in_month = 30
    t = datetime.datetime(array[0],array[1],array[2],array[3],array[4],array[5], 0)
    t2 = t + datetime.timedelta(0, int(dict_v['interval']))
    new_date = str(t2.year) + '-' + str(t2.month) + '-' + str(t2.day) + 'T' + str(t2.hour) + ':' + str(t2.minute) + ':' + str(t2.second) + 'Z'
    print new_date
    print dict_v
    data2 = {'token': token, 'datestamp': new_date}
    r = requests.post('http://challenge.code2040.org/api/dating/validate', json = data2)
    print r.text 
