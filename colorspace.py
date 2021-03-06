import numpy as np


def LMStoXYZ(LMS):
    """
    Convert LMS space to CIE XYZ
    parameters:
    LMS - scalar(3,n)
        LMS-cone activation values
    returns:
    XYZ - scalar (3,n)
        CIE-XYZ values
    """
    M = np.asarray([[1.91020,-1.11212,0.20191],
                    [0.37095, 0.62905,0.     ],
                    [0.     , 0.     ,1.     ]])
    '''
    M65 = np.asarray([[1.8657,-1.1329, 0.2206],
                     [0.35800,0.64070,-0.0004],
                     [0.     ,0.     , 1.0891]])
    '''
    return M@LMS


def XYZtoxyz(XYZ):
    """
    Convert XYZ space to CIE 1931 xyz (they're different...)
    parameters:
    XYZ - scalar(3,n)
        XYZ color values
    returns:
    xzy - scalar (3,n)
        CIE-XYZ values
    """
    mXYZ = np.mean(XYZ,axis=0)+1e-6
    
    x = XYZ[0,]/mXYZ
    y = XYZ[1,]/mXYZ
    z = 1-x-y
    return np.asarray([x,y,z])


def LMStoxyz(LMS):
    """
    Convert LMS space to CIE 1931 xyz
    parameters:
    LMS - scalar(3,n)
        LMS-cone activation values
    returns:
    xyz - scalar (3,n)
        CIE 1931 XYZ values
    """
    return XYZtoxyz(LMStoXYZ(LMS))
    
    
def sRGBtoXYZ(sRGB):
    """
    Convert sRGB space to XYZ
    parameters:
    sRGB - scalar(3,n)
        sRGB values
    returns:
    XYZ - scalar (3,n)
        XYZ values
    """
    M = np.array([[0.4124,0.3576,0.1805],
                  [0.2126,0.7152,0.0722],
                  [0.0193,0.1192,0.9595]])
    return M@sRGB


def sRGBtoxyz(sRGB):
    """
    Convert sRGB space to CIE 1931 xyz
    parameters:
    sRGB - scalar(3,n)
        sRGB values
    returns:
    xyz - scalar (3,n)
        CIE 1931 xyz
    """
    return XYZtoxyz(sRGBtoXYZ(sRGB))