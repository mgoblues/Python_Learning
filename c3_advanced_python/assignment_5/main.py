from flask import Flask
from flask import request
from json import dumps, loads
from pymongo import MongoClient
from mongo_lib import m_find_object, m_update_object, m_remove_object



app = Flask(__name__)

@app.route('/<oid>', methods=['GET'])
def h_findObject(oid):
    #DB lookup code goes here
    return dumps({'oid': oid, 'attr': 'object_data'})

@app.route('/<oid>', methods=['POST', 'PUT'])
def h_updateObject(oid):
#DB Update/Upsert code goes here
    print('Parameters (using form.items):')
    request.get_data() #gives request, need json_loads
    # write primary key into object
    # use set item on a dict []
    # write them in to mongo with primary key
    # need update object on mongo library
    return "ok"


if __name__ == '__main__':
    app.testing = True
    with app.test_client() as c:
        get_resp = c.get('/blah')
        print('get status: {}'.format(get_resp.status))
        print('get response: {}'.format(get_resp.get_data()))
        c.post('/blah', data='{"attr": "My Object data"}')
        post_resp = c.post('/blah')

# connect to mongo database
