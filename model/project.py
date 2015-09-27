__author__ = '1'
from sys import maxsize

class Project:
    def __init__(self, name = None, description = None, id = None):
        self.name = name
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id,self.name,self.description)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize