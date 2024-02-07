import numpy as np
import second_order


########## RC-RC Filters ###############

#LOWPASS
class LP_RC_RC(second_order.LP):
    def __init__(self, T0, w0, m):
        self.name = "Second Order Low Pass RC-RC Filter"
        self.T0 = T0
        self.w0 = w0
        self.m = m
        self.componants = {
            "R1" : 0,
            "R2" : 0,
            "C1" : 0,
            "C2" : 0
        }
    
    def calc_componants(self, **kwargs):
        
        if "R2" in kwargs and "C2" in kwargs and len(kwargs.keys()) == 2:
            self.componants["R2"] = kwargs["R2"]
            self.componants["C2"] = kwargs["C2"]
        
        else: 
            self.componants["R2"] = 18000
            self.componants["C2"] = 10**-8
        
        alpha1 = self.componants["R2"] * self.componants["C2"]  # = R2*C2
        alpha2 = 1 / (self.w0**2 * alpha1)   # = R1*C1
        alpha3 = (2*(self.m/self.w0)) - (alpha1 + alpha2)   # = C2*R1

        self.componants["R1"] = alpha3 / self.componants["C2"] 
        self.componants["C1"] = alpha2 / self.componants["R1"]


        return self.componants

#HIGHPASS
class HP_RC_RC(second_order.HP):
    def __init__(self, Too, w0, m):
        self.name = "Second Order High Pass RC-RC Filter"
        self.Too = Too
        self.w0 = w0
        self.m = m
        self.componants = {
            "R1" : 0,
            "R2" : 0,
            "C1" : 0,
            "C2" : 0
        }
    def calc_componants(self, **kwargs):
        
        if "R1" in kwargs and "C1" in kwargs and len(kwargs.keys()) == 2:
            self.componants["R1"] = kwargs["R1"]
            self.componants["C1"] = kwargs["C1"]
        
        else: 
            self.componants["R1"] = 22000
            self.componants["C1"] = 1.5*(10**-9)
        
        alpha1 = self.componants["R1"] * self.componants["C1"] # = R1*C1
        alpha2 = 1 / (self.w0**2 * alpha1)   # = R2*C2
        alpha3 = (2*self.m)/self.w0 - alpha1 - alpha2    # = R1*C2

        # comosents cherchés
        self.componants["C2"] = alpha3 / self.componants["R1"]
        self.componants["R2"] = alpha2 / self.componants["C2"]

        return self.componants

#BANDPASS
class BP_RC_RC(second_order.BP):
    def __init__(self, Tm, w0, m):
        self.name = "Second Order Low Pass RC-RC Filter"
        self.Tm = Tm
        self.w0 = w0
        self.m = m
        self.componants = {
            "R1" : 0,
            "R2" : 0,
            "C1" : 0,
            "C2" : 0
        } 
    
    def calc_componants(self, **kwargs):

        if "R1" in kwargs and "C1" in kwargs and len(kwargs.keys()) == 2:
            self.componants["R1"] = kwargs["R1"]
            self.componants["C1"] = kwargs["C1"]
        
        else: 
            self.componants["R1"] = 18000
            self.componants["C1"] = 4.7*(10**-9)

        alpha1 = self.componants["R1"] * self.componants["C1"] # = R1*C1
        alpha2 = 1 / (self.w0**2 * alpha1)   # = R2*C2
        alpha3 = (2*self.m/self.w0) - alpha1 - alpha2   # = R2*C1

        self.componants["R2"] = alpha3 / self.componants["C1"]
        self.componants["C2"] = alpha2 / self.componants["R2"]

        return self.componants

