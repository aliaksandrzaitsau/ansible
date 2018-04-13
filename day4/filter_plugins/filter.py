class FilterModule(object):   
    def filters(self):
        return {
            'find': self.find,
        }
    def find(self, value, param=0):        
        number = 0
        result={}
        while number < 4:
            if int(value[number]["id"]) > param:
                result[value[number]["id"]]="id"
            number += 1
        return result
