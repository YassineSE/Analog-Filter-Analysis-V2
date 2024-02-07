import first_order
import second_order
import circuits
import scipy.signal as sig


b1 = second_order.BP(1,1000,0.1)
b1.plot_bode()