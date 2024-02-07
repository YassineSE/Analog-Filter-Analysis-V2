from core import Filter
import numpy as np
import scipy.signal as sig

class First_Order():
    pass

class LP(First_Order, Filter):

    def __init__(self, T0, w0):
        self.type = "First Order Low Pass Filter"
        self.T0 = T0
        self.w0 = w0
    
    def get_sys(self):
        num = np.array([self.T0])
        den = np.array([1/self.w0, 1])
        return sig.lti(num,den)

    def get_params(self):
        return {
            "type" : self.type,
            "gain_low" : self.T0,
            "tau" : 1/self.w0
        }
    
    def get_type(self):
        return self.type
    


class HP(First_Order, Filter):

    def __init__(self, Too, w0):
        self.type = "First Order High Pass Filter"
        self.Too = Too
        self.w0 = w0
    
    def get_sys(self):
        num = np.array([self.Too,0])
        den = np.array([1/self.w0, 1])
        return sig.lti(num,den)
    
    def get_params(self):
        return {
            "type" : self.type,
            "gain_high" : self.Too,
            "tau" : 1/self.w0
        }
    def get_type(self):
        return self.type
