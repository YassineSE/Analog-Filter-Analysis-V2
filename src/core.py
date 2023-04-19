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
