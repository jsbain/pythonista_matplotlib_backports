import matplotlib
from . import animation 
import sys
matplotlib.animation=animation
sys.modules['matplotlib.animation']=animation
