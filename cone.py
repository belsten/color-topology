import numpy as np
from scipy import interpolate


def cone_L(lmbda):
    """
    Interpolate the response of the L cone for a given wavelength lmbda.
    """
    xp = [350, 400, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 710, 750, 800]
    fp = [0, 0, 0.1, 0.3, 0.7, 0.95, 0.999, 0.9, 0.553, 0.18, 0.075, 0.001, 0, 0, 0]
    # alpha_cone = np.interp(lmbda, xp, fp)
    interp_cone = interpolate.interp1d(
        xp, fp, kind="quadratic", fill_value="extrapolate"
    )
    alpha_cone = np.clip(interp_cone(lmbda), a_min=0.001, a_max=1)
    return alpha_cone


def cone_M(lmbda):
    """
    Interpolate the response of the M cone for a given wavelength lmbda.
    """
    xp = [
        350,
        400,
        450,
        480,
        500,
        525,
        537,
        550,
        562,
        575,
        600,
        625,
        650,
        675,
        700,
        750,
    ]
    fp = [0, 0, 0.1, 0.235, 0.4, 0.9, 0.975, 1, 0.94, 0.8, 0.35, 0.1, 0.05, 0.001, 0, 0]
    # alpha_cone = np.interp(lmbda, xp, fp)
    interp_cone = interpolate.interp1d(
        xp, fp, kind="quadratic", fill_value="extrapolate"
    )
    alpha_cone = np.clip(interp_cone(lmbda), a_min=0.001, a_max=1)
    return alpha_cone


def cone_S(lmbda):
    """
    Interpolate the response of the S cone for a given wavelength lmbda.
    """
    xp = [300, 380, 400, 408, 425, 440, 458, 468, 475, 500, 512.5, 550, 600, 700]
    fp = [
        0.00001,
        0.0001,
        0.05,
        0.15,
        0.6,
        0.83,
        0.875,
        0.665,
        0.45,
        0.1,
        0.05,
        0.001,
        0.001,
        0.001,
    ]
    interp_cone = interpolate.interp1d(
        xp, fp, kind="quadratic", fill_value="extrapolate"
    )
    alpha_cone = np.clip(
        interp_cone(lmbda), a_min=0.001, a_max=1
    )  # np.interp(lmbda, xp, fp)
    return alpha_cone
