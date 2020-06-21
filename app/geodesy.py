import math

def grav_normal(lat):
    gamma = 978.0327*(1+(0.0053024*(math.sin(math.radians(lat))**2))-0.0000058*(math.sin(2*math.radians(lat))**2))
    return gamma

