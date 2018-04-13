#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'find': self.find,
        }
    def find(self):
        return int(value) + int(param)
