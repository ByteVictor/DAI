from pickleshare import PickleShareDB

db = PickleShareDB('miBD')
db['user'] = {'email' : 'admin@admin.com',
              'pass'  : '1234'}
db['user_pass'] = {'pass' : '1234'}