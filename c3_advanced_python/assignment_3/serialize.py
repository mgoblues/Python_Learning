from json import loads, dumps


class MySerializer(object):

    @classmethod
    def deserialize(cls, jsonstr):
        ## load from json to dict
        ## initialize object, return
        # Class method, no instead of self, use cls
        # class item, obj is string rep in json of object.
        # call json.loads to convert from string to dict object
        # use initializer to return back class (serialize?)
        # load into dictionary, and initialize through class
        # return obstantiation

        dict_as_obj = loads(jsonstr)
        return cls(**dict_as_obj)

    def serialize(self):
        # need to: convert from dict to json
        # refer to the dict: use json.dump to transfer
        # dict to string(json)
        # iterate over self.my_attrs
        # get attrs, set into dictoinary
        # return dumps(dictionary)
        serialized_dict = {}
        # creating empty dictionary for values to be added to
        for keys, values in self.items:
            serialized_dict[key] = value
            #adding key - value pairs for all items in dicts
        #Now have created new dictionary
        return dumps(serialized_dict)

            # dump the new dictionary
            # want to get attrs from self (name of attr = k)
            # put that into dictionary

