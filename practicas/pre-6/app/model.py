from pickleshare import PickleShareDB

db = PickleShareDB('miBD')
db['users'] = []


def check_user(email, passw):
    for user in db['users']:
        if(user['email'] == email and user['pass'] == passw):
            return True
    return False

def check_user_exist(email):
    for user in db['users']:
        if(user['email'] == email):
            return True
    return False

def registrar(email, passw):
    if not check_user_exist(email):
        db['users'].append({'email' : email,
                            'pass'  : passw})
        return True
    else: 
        return False