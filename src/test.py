from scipy.signal import lti
import numpy as np
import control as ctl
from control_plotly import step,bode
from core import Filter
import first_order
import second_order

hp1 = first_order.HP(1,1000)
print(hp1.calc_componants("SPL"))