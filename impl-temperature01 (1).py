import re

class PhysicalInfo(object):
    
    def set_date(self, date):  
       pass
        
    def set_name(self, name):
        pass
    
    def set_gender(self, gender):
        pass
    
    def set_height(self, height):
        pass

    def set_temperature(self, temperature):
        #if not isinstance(temperature, float):
        #    raise ValueError("temperature should be a float")
        if temperature < 95 or temperature > 104:
            raise ValueError("temperature should be a float between 95 and 104")
        self.temperature = temperature
