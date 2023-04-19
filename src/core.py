#Importing basic libraries
from scipy.signal import lti
import numpy as np
import control as ctl
from control_plotly import step,bode,pzmap


class Filter():
    #Main Class for all filters

    def __init__(self, name="filter"):
        self.name = name
    
    def get_sys(self):
        return ctl.tf([1], [1,1])
    
    def get_params(self):
        return {}
    
    def get_type(self):
        return "Filter"

    def plot_bode(self):
        p = self.get_params()
        params = "".join([str(i) + " : " + str(j) + ", " for i,j in zip(p.keys(), p.values())])
        sys = self.get_sys()
        fig = bode(sys)
        fig.update_layout(title=dict(text=params, font=dict(size=20)))
        fig.show()
    
    def plot_step(self):
        p = self.get_params()
        params = "".join([str(i) + " : " + str(j) + ", " for i,j in zip(p.keys(), p.values())])
        sys = self.get_sys()
        fig = step(sys)
        fig.update_layout(title=dict(text=params, font=dict(size=20)))
        fig.show()

    def plot_poles(self):
        p = self.get_params()
        params = "".join([str(i) + " : " + str(j) + ", " for i,j in zip(p.keys(), p.values())])
        sys = self.get_sys()
        fig = pzmap(sys)
        fig.update_layout(title=dict(text=params, font=dict(size=20)))
        fig.show()

    def calc_componants(self, type):
        import second_order
        import first_order
        
        if isinstance(self, second_order.Second_Order):
            if isinstance(self, second_order.HP):
                
                params = self.get_params()
                Too = params["gain_high"]
                w0 = params["w0"]
                m = 1/(2 * params["Q"])
                
                if type == "RC_RC":
                    return {"R1":0,"R2":0,"C1":0,"C2":0}
                
                elif type == "RLC":
                    R = 1000
                    L = R/(2*w0*m)
                    C = 1/(L*(w0**2))
                    return {"R":R,"L":L,"C":C}
                
                elif type == "Rauch":
                    C1 = 10 **-9
                    C2 = 2.2 * 10**(-8)
                    C3 = 3.3 * 10**(-9)
                    # On cherche maintenant R1 et R2
                    R1 = (2*m) / ((C1+C2+C3)*w0) 
                    R2 = 1 / ((w0**2)*R1*C2*C3)
                    return {"R1":R1,"R2":R2,"C1":C1,"C2":C2,"C3":C3} 
                
                elif type == "SK":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                else:
                    return {}
                
            elif isinstance(self, second_order.LP):
                params = self.get_params()
                T0 = params["gain_low"]
                w0 = params["w0"]
                m = 1/(2 * params["Q"])
                
                if type == "RC_RC":
                    return {"R1":0,"R2":0,"C1":0,"C2":0}
                
                elif type == "RLC":
                    return {"R":0,"L":0,"C":0}
                
                elif type == "Rauch":
                    return {"R1":0,"R2":0,"C1":0,"C2":0,"C3":0} 
                
                elif type == "SK":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                else:
                    return {}
                
                
            elif isinstance(self, second_order.BP):
                params = self.get_params()
                Tm = params["gain_max"]
                w0 = params["w0"]
                m = 1/(2 * params["Q"])
                
                if type == "RC_RC":
                    return {"R1":0,"R2":0,"C1":0,"C2":0}
                
                elif type == "RLC1":
                    return {"R":0,"L":0,"C":0}
                
                elif type == "RLC2":
                    return {"R":0,"L":0,"C":0}
                
                elif type == "Rauch1":
                    return {"R1":0,"R2":0,"C1":0,"C2":0,"C3":0} 
                
                elif type == "Rauch2":
                    return {"R1":0,"R2":0,"C1":0,"C2":0,"C3":0} 
                
                elif type == "SK":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                else:
                    return {}
            
            elif isinstance(self, second_order.BS):
                params = self.get_params()
                T0 = params["gain_max"]
                w0 = params["w0"]
                m = 1/(2 * params["Q"])
                
                if type == "RC_RC":
                    return {"R1":0,"R2":0,"C1":0,"C2":0}
                
                elif type == "RLC1":
                    return {"R":0,"L":0,"C":0}
                
                elif type == "RLC2":
                    return {"R":0,"L":0,"C":0}
                
                elif type == "Rauch1":
                    return {"R1":0,"R2":0,"C1":0,"C2":0,"C3":0} 
                
                elif type == "Rauch2":
                    return {"R1":0,"R2":0,"C1":0,"C2":0,"C3":0} 
                
                elif type == "SK":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                
                elif type == "TwinT":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                
                elif type == "BrigedT":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                
                elif type == "MulFeed":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                
                elif type == "Biquad":
                    return {"R1":0,"R2":0,"R3":0,"R4":0,"C1":0,"C2":0}
                
                else:
                    return {}
            else:
                return {}
        
        elif isinstance(self, first_order.First_Order):
            if isinstance(self, first_order.HP):
                if type == "RC":
                    return {"R": 0, "C":0}
                elif type == "RL":
                    return {"R": 0, "L":0}
                elif type == "SPC":
                    return {"R1":0,"R2":0,"C":0}
                elif type == "SPL":
                    return {"R1":0,"R2":0,"L":0}
            
            if isinstance(self, first_order.LP):
                if type == "RC":
                    return {"R": 0, "C":0}
                elif type == "RL":
                    return {"R": 0, "L":0}
                elif type == "SPC":
                    return {"R1":0,"R2":0,"C":0}
                elif type == "SPL":
                    return {"R1":0,"R2":0,"L":0}
        
        else:
            return {}
         