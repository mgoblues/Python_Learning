#Enable accessing items by attribute
# set attribute, assert that equald from square brackets


class YourDict(dict):

    def __setattr__(self, attr, value):
        self[attr] = value

    def __getattr__(self, attr):
        try:
            return self[attr]
        except:
            raise AttributeError()


