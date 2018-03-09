from pymongo import MongoClient

client = MongoClient()

mongo_collection = client.mongo_database.mongo_collection
# This is the database

# this is the collection

# primary key = a

def find_object(primary_key):
    '''finds and return an object matching the primary key.
    retruns None if not found '''
    output = mongo_collection.find_one({'a': primary_key})
    return output

def update_object(new_object):
    '''Updates and object if it exists, inserts if it does not.
    upsert perhaps?
    '''
    # find primary key from new object
    # provide upsert command using primary key (new object)
    primary_key = new_object['a']
    obj_search = {'a': primary_key}
    mongo_collection.update(obj_search, new_object, upsert=True)
    return None


def remove_object(primary_key):
    '''Deletes the object matching primary_key
    Retruns True if deleted, False if not found.'''
    # deleting primary key from mongo_collection and checking to see if del
    del_result = mongo_collection.delete_one({'a': primary_key})
    # returns True or false
    return (del_result.deleted_count > 0)

# primary key is _a
# key name is a

