from core import Filter
import numpy as np
import control as ctl

class Second_Order():
    
    def has_overshoot(self):
        return (self.m<1)

    def get_w_p(self):
        if self.has_overshoot():
            w_p = self.w0*np.sqrt(1-(self.m**2))
        else:
            w_p = None
        return w_p
    
    def has_resonance(self):
        return (self.m<(1/np.sqrt(2)))
    
    

class LP(Second_Order, Filter):

    def __init__(self, T0, w0, m):
        self.type = "Second Order Low Pass Filter"
        self.T0 = T0
        self.w0 = w0
        self.m = m
    
    def get_sys(self):
        num = np.array([self.T0])
        den = np.array([1/(self.w0 ** 2), 2*self.m/self.w0, 1])
        return ctl.tf(num,den)
    
    def get_type(self):
        return self.type
    
    def get_params(self):
        return {
            "type" : self.type,
            "w0" : self.w0,
            "gain_low" : self.T0,
            "Q" : 1/(2*self.m),
            "has_overshoot" : self.has_overshoot(),
            "has_resonance" : self.has_resonance(),
            "w_p" : self.get_w_p()
        }

class HP(Second_Order, Filter):

    def __init__(self, Too, w0, m):
        self.type = "Second Order High Pass Filter"
        self.Too = Too
        self.w0 = w0
        self.m = m
    
    def get_sys(self):
        num = np.array([self.Too*(1/(self.w0**2)),0,0])
        den = np.array([1/(self.w0 ** 2), 2*self.m/self.w0, 1])
        return ctl.tf(num,den)
    
    def get_type(self):
        return self.type
    
    def get_params(self):
        return {
            "type" : self.type,
            "w0" : self.w0,
            "gain_high" : self.Too,
            "Q" : 1/(2*self.m),
            "has_overshoot" : self.has_overshoot(),
            "has_resonance" : self.has_resonance(),
            "w_p" : self.get_w_p()
        }

class BP(Second_Order, Filter):

    def __init__(self, Tm, w0, m):
        self.type = "Second Order Band Pass Filter"
        self.Tm = Tm
        self.w0 = w0
        self.m = m
    
    def get_sys(self):
        Ti = 2*self.m*self.Tm
        num = np.array([0,Ti/self.w0,0])
        den = np.array([1/(self.w0 ** 2), 2*self.m/self.w0, 1])
        return ctl.tf(num,den)
    
    def get_type(self):
        return self.type
    
    def get_params(self):
        return {
            "type" : self.type,
            "w0" : self.w0,
            "gain_max" : self.Tm,
            "Q" : 1/(2*self.m),
            "has_overshoot" : self.has_overshoot(),
            "has_resonance" : self.has_resonance(),
            "w_p" : self.get_w_p(),
            "bandwith" : 2*self.m*self.w0
        }

class BS(Second_Order, Filter):

    def __init__(self, T0, w0, m):
        self.type = "Second Order Band Stop Filter"
        self.T0 = T0
        self.w0 = w0
        self.m = m
    
    def get_sys(self):
        num = np.array([self.T0 * (1/(self.w0**2)),0,self.T0])
        den = np.array([1/(self.w0 ** 2), 2*self.m/self.w0, 1])
        return ctl.tf(num,den)
    
    def get_type(self):
        return self.type
    
    def get_params(self):
        return {
            "type" : self.type,
            "w0" : self.w0,
            "gain_low" : self.T0,
            "Q" : 1/(2*self.m),
            "has_overshoot" : self.has_overshoot(),
            "has_resonance" : self.has_resonance(),
            "w_p" : self.get_w_p(),
            "bandwith" : 2*self.m*self.w0
        }
