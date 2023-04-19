#Importing basic libraries
from scipy.signal import lti
import numpy as np
import control as ctl
from control_plotly import step,bode

class Filter():
    #Main Class for all filters

    def __init__(self, name="filter"):
        self.name = name
    
    def get_sys(self):
        return ctl.tf([1], [1,1])
    
    def get_params(self):
        return {}
    
    def get_type(self):
        return "abc"

    def plot_bode(self):
        title = self.get_type()
        sys = self.get_sys()
        fig = bode(sys)
        fig.update_layout(title=dict(text=title, font=dict(size=20)))
        fig.show()
    
    def plot_step(self):
        sys = self.get_sys()
        fig = step(sys)
        fig.show()

