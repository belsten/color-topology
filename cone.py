import numpy as np
from scipy import interpolate


class cone():
    def __init__(self,fname):
        data = np.genfromtxt(fname, delimiter=',')
        data[np.isnan(data)] = 0.
        self.lmbda = data[:,0]
        self.L = data[:,1]
        self.M = data[:,2]
        self.S = data[:,3]

        
    def cone_L(self,querylmbda):
        """
        Interpolate the response of the L cone for a given wavelength lmbda.
        """
        alpha_cone = np.interp(querylmbda, self.lmbda, self.L)
        alpha_cone = np.clip(alpha_cone, a_min=0.0, a_max=1)
        return alpha_cone


    def cone_M(self,querylmbda):
        """
        Interpolate the response of the M cone for a given wavelength lmbda.
        """
        alpha_cone = np.interp(querylmbda, self.lmbda, self.M)
        alpha_cone = np.clip(alpha_cone, a_min=0.0, a_max=1)
        return alpha_cone


    def cone_S(self,querylmbda):
        """
        Interpolate the response of the S cone for a given wavelength lmbda.
        """
        alpha_cone = np.interp(querylmbda, self.lmbda, self.S)
        alpha_cone = np.clip(alpha_cone, a_min=0.0, a_max=1)
        return alpha_cone
