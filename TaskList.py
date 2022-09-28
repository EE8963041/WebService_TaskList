import requests
import json
from datetime import datetime
from argparse import ArgumentParser
import sys



def GetTaskList():
    response_API = requests.get(' http://127.0.0.1:8000/Task')
    #print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    #print(parse_json)

    for d in parse_json:

        print('Task Name :'+str(d['TaskName']) + ' Due Date : '+str(d['ExpiryDate']))



def GetExpiryTaskList():
    response_API = requests.get('http://127.0.0.1:8000/Task')
    #print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    #print(parse_json)
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d")

    for d in parse_json:
        if(str(d['ExpiryDate'])==dt_string):

            print('Task Name :'+str(d['TaskName']) + ' Due Date : '+str(d['ExpiryDate']))
        
def GetDoneTaskList():
    response_API = requests.get('http://127.0.0.1:8000/Task')
    #print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    #print(parse_json)
    
    dontask=0
    for d in parse_json:
        if(str(d['TaskStatus'])=='1'):
            dontask=dontask+1

    print('Task Done : '+str(dontask))

def AddNewTask(tname,tdate):
    url = 'http://127.0.0.1:8000/Task'
    myobj = {"TaskName": tname,"ExpiryDate": tdate,}
    #print(myobj)

    x = requests.post(url, json = myobj)

    print(x.text)


if __name__ == "__main__":

    #GetTaskList()
    mode=''
    #for i in range(1, len(sys.argv)):
        #print('argument:', i, 'value:', sys.argv[i])

    mode=sys.argv[1]
    if(mode=='TaskList'):
        GetTaskList()
    elif(mode=='TaskDone'):
        GetDoneTaskList()        
    elif(mode=='ExpiryTask'):
        GetExpiryTaskList()
    elif(mode=='AddTask'):
        tname=str(sys.argv[2])
        tdate=str(sys.argv[3])
        print(tdate)
        AddNewTask(tname,tdate)
    
    #GetDoneTaskList()


    #python manage.py runserver


    #python TaskList.py AddTask name 2022-21-09
    #python TaskList.py TaskDone
    #python TaskList.py TaskList

    #python TaskList.py ExpiryTask
    #python TaskList.py AddTask CMDTask 2022-09-23
    

