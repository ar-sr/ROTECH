

import os
import json


employee_data={'count':0,"employee_list":[]}








def create():
    ID=int(input("enter the ID"))
    name=input("enter the name:")
    age=int(input("enter the age:"))
    phn=int(input("enter the phone number:"))
    exp=int(input("enter the year of experience:"))
    grade=input("enter the grade:")
    
    
    
    employee_data["count"]+=1
    employee_data["employee_list"].append ({'ID':id,'name':name,'age':age,'phn':phn,'exp':exp,'grade':grade})
    
    
    

with open("employee.json",'w') as file:
     json.dump(employee_data,file,indent=4)
    








def read():
    val=input("enter the name:")
    if os.path.exists('employee.json'):
        with open('employee.json','r+') as file:
                    employee_data=json.load(file)
                    

    
    
    for emp in employee_data['employee_list']:
        if emp['name']==val:
            for key,value in emp.items():
                print(key,value)
        
            









while True:
    options=int(input("enter the prompt:"))
    
    
    
    if options==1:
        create()
    elif options==2:
        read()
    elif options==3:
        print("have a nice day!")
        break