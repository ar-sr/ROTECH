import json 
import os

employee_data={'count':0,"employee_list":[]}


def add():
    
    name=input("enter the name:")
    age=int(input("enter the age:"))
    
    
    
    employee_data["count"]+=1
    
    
    employee_data["employee_list"].append({'name':name,'age':age})
    
    
    with open("employee.json",'w') as file:
        json.dump(employee_data,file,indent=4)
        
        
        
def get():
            val=input("enter the name:")
            
            if os.path.exists('employee.json'):
                
                with open('employee.json','r+') as file:
                    employee_data=json.load(file)
                    
                    
                    
            for emp in employee_data['employee_list']:
                if emp['name']==val:
                    for key,value in emp.items():
                        print(key,value)
                





while True:
    value=int(input("enter the prompt:"))
    
    
    if value==1:
        add()
    elif value==2:
        get()
    else:
        break
