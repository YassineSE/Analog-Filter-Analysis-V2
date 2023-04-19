from scipy.signal import lti
import numpy as np
import control as ctl
from control_plotly import step,bode
from core import Filter
import first_order

hp1 = first_order.HP(10,2000)
print(hp1.get_type())