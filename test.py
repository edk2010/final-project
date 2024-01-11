import json


data = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]
def add_user(data,user_name):
    new_user = {}
    #employee = 'new5'

    new_user['id'] = len(data) + 1
    new_user['name'] = user_name
    data.append(new_user)
    print(data)
    return True


operation = 'add_user'
user_name = 'test4'
user_id = 3

match operation:
    case "check_id":
        message = 'check_id'
        
    case "check_name":
        message = 'check_name'
    case "add_user":
        result = add_user(data, user_name)
        if result:
            message = f'new user: {user_name} added succesfuly'
        else:
            message = f'something went wrong'
    case "remove":
        message = 'remove'
    case _ :
        message = "You do not have any acce"
            
    
def get_user_by_user_id(data, user_id):
    return next((e for e in data if e['id'] == user_id), None)  

def get_user_by_user_name(data,user_name):
 return next((e for e in data if e['name'] == user_name), None)
   
print(get_user_by_user_name(data,user_name))



def delete_user(data,user_id):
 #global employees
    user = get_user_by_user_id(data,user_id)
    if user is None:
        return None

    data = [e for e in data if e['id'] != int(user_id)]
    return data

data=delete_user(data,3)
add_user(data,"vova")

#print(data)