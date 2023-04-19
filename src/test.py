from scipy.signal import lti
import numpy as np
import control as ctl
from control_plotly import step,bode
from core import Filter
import first_order
import second_order

hp2 = second_order.BS(10,2000,0.1)
print(issubclass(second_order.BP, Filter))

