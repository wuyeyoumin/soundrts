""""use integers to make sure that any computer will give the same results"""

import math
import sys

from .log import warning


PRECISION = 1000

# tables used to make sure that every computer gives the same results
_COS_TABLE = (1000, 999, 999, 998, 997, 996, 994, 992, 990, 987, 984, 981, 978, 974, 970, 965, 961, 956, 951, 945, 939, 933, 927, 920, 913, 906, 898, 891, 882, 874, 866, 857, 848, 838, 829, 819, 809, 798, 788, 777, 766, 754, 743, 731, 719, 707, 694, 681, 669, 656, 642, 629, 615, 601, 587, 573, 559, 544, 529, 515, 500, 484, 469, 453, 438, 422, 406, 390, 374, 358, 342, 325, 309, 292, 275, 258, 241, 224, 207, 190, 173, 156, 139, 121, 104, 87, 69, 52, 34, 17, 0, -17, -34, -52, -69, -87, -104, -121, -139, -156, -173, -190, -207, -224, -241, -258, -275, -292, -309, -325, -342, -358, -374, -390, -406, -422, -438, -453, -469, -484, -499, -515, -529, -544, -559, -573, -587, -601, -615, -629, -642, -656, -669, -681, -694, -707, -719, -731, -743, -754, -766, -777, -788, -798, -809, -819, -829, -838, -848, -857, -866, -874, -882, -891, -898, -906, -913, -920, -927, -933, -939, -945, -951, -956, -961, -965, -970, -974, -978, -981, -984, -987, -990, -992, -994, -996, -997, -998, -999, -999, -1000, -999, -999, -998, -997, -996, -994, -992, -990, -987, -984, -981, -978, -974, -970, -965, -961, -956, -951, -945, -939, -933, -927, -920, -913, -906, -898, -891, -882, -874, -866, -857, -848, -838, -829, -819, -809, -798, -788, -777, -766, -754, -743, -731, -719, -707, -694, -681, -669, -656, -642, -629, -615, -601, -587, -573, -559, -544, -529, -515, -500, -484, -469, -453, -438, -422, -406, -390, -374, -358, -342, -325, -309, -292, -275, -258, -241, -224, -207, -190, -173, -156, -139, -121, -104, -87, -69, -52, -34, -17, 0, 17, 34, 52, 69, 87, 104, 121, 139, 156, 173, 190, 207, 224, 241, 258, 275, 292, 309, 325, 342, 358, 374, 390, 406, 422, 438, 453, 469, 484, 500, 515, 529, 544, 559, 573, 587, 601, 615, 629, 642, 656, 669, 681, 694, 707, 719, 731, 743, 754, 766, 777, 788, 798, 809, 819, 829, 838, 848, 857, 866, 874, 882, 891, 898, 906, 913, 920, 927, 933, 939, 945, 951, 956, 961, 965, 970, 974, 978, 981, 984, 987, 990, 992, 994, 996, 997, 998, 999, 999)
_SIN_TABLE = (0, 17, 34, 52, 69, 87, 104, 121, 139, 156, 173, 190, 207, 224, 241, 258, 275, 292, 309, 325, 342, 358, 374, 390, 406, 422, 438, 453, 469, 484, 499, 515, 529, 544, 559, 573, 587, 601, 615, 629, 642, 656, 669, 681, 694, 707, 719, 731, 743, 754, 766, 777, 788, 798, 809, 819, 829, 838, 848, 857, 866, 874, 882, 891, 898, 906, 913, 920, 927, 933, 939, 945, 951, 956, 961, 965, 970, 974, 978, 981, 984, 987, 990, 992, 994, 996, 997, 998, 999, 999, 1000, 999, 999, 998, 997, 996, 994, 992, 990, 987, 984, 981, 978, 974, 970, 965, 961, 956, 951, 945, 939, 933, 927, 920, 913, 906, 898, 891, 882, 874, 866, 857, 848, 838, 829, 819, 809, 798, 788, 777, 766, 754, 743, 731, 719, 707, 694, 681, 669, 656, 642, 629, 615, 601, 587, 573, 559, 544, 529, 515, 499, 484, 469, 453, 438, 422, 406, 390, 374, 358, 342, 325, 309, 292, 275, 258, 241, 224, 207, 190, 173, 156, 139, 121, 104, 87, 69, 52, 34, 17, 0, -17, -34, -52, -69, -87, -104, -121, -139, -156, -173, -190, -207, -224, -241, -258, -275, -292, -309, -325, -342, -358, -374, -390, -406, -422, -438, -453, -469, -484, -500, -515, -529, -544, -559, -573, -587, -601, -615, -629, -642, -656, -669, -681, -694, -707, -719, -731, -743, -754, -766, -777, -788, -798, -809, -819, -829, -838, -848, -857, -866, -874, -882, -891, -898, -906, -913, -920, -927, -933, -939, -945, -951, -956, -961, -965, -970, -974, -978, -981, -984, -987, -990, -992, -994, -996, -997, -998, -999, -999, -1000, -999, -999, -998, -997, -996, -994, -992, -990, -987, -984, -981, -978, -974, -970, -965, -961, -956, -951, -945, -939, -933, -927, -920, -913, -906, -898, -891, -882, -874, -866, -857, -848, -838, -829, -819, -809, -798, -788, -777, -766, -754, -743, -731, -719, -707, -694, -681, -669, -656, -642, -629, -615, -601, -587, -573, -559, -544, -529, -515, -500, -484, -469, -453, -438, -422, -406, -390, -374, -358, -342, -325, -309, -292, -275, -258, -241, -224, -207, -190, -173, -156, -139, -121, -104, -87, -69, -52, -34, -17)
_ACOS_TABLE = {0: 90, 1: 89, 2: 88, 3: 88, 4: 87, 5: 87, 6: 86, 7: 85, 8: 85, 9: 84, 10: 84, 11: 83, 12: 83, 13: 82, 14: 81, 15: 81, 16: 80, 17: 80, 18: 79, 19: 79, 20: 78, 21: 77, 22: 77, 23: 76, 24: 76, 25: 75, 26: 74, 27: 74, 28: 73, 29: 73, 30: 72, 31: 71, 32: 71, 33: 70, 34: 70, 35: 69, 36: 68, 37: 68, 38: 67, 39: 67, 40: 66, 41: 65, 42: 65, 43: 64, 44: 63, 45: 63, 46: 62, 47: 61, 48: 61, 49: 60, 50: 59, 51: 59, 52: 58, 53: 57, 54: 57, 55: 56, 56: 55, 57: 55, 58: 54, 59: 53, 60: 53, 61: 52, 62: 51, 63: 50, 64: 50, 65: 49, 66: 48, 67: 47, 68: 47, 69: 46, 70: 45, 71: 44, 72: 43, 73: 43, 74: 42, 75: 41, 76: 40, 77: 39, 78: 38, 79: 37, 80: 36, 81: 35, 82: 34, 83: 33, 84: 32, 85: 31, 86: 30, 87: 29, 88: 28, 89: 27, 90: 25, 91: 24, 92: 23, 93: 21, 94: 19, 95: 18, 96: 16, 97: 14, 98: 11, 99: 8, 100: 0, -1: 90, -100: 180, -99: 171, -98: 168, -97: 165, -96: 163, -95: 161, -94: 160, -93: 158, -92: 156, -91: 155, -90: 154, -89: 152, -88: 151, -87: 150, -86: 149, -85: 148, -84: 147, -83: 146, -82: 145, -81: 144, -80: 143, -79: 142, -78: 141, -77: 140, -76: 139, -75: 138, -74: 137, -73: 136, -72: 136, -71: 135, -70: 134, -69: 133, -68: 132, -67: 132, -66: 131, -65: 130, -64: 129, -63: 129, -62: 128, -61: 127, -60: 126, -59: 126, -58: 125, -57: 124, -56: 124, -55: 123, -54: 122, -53: 122, -52: 121, -51: 120, -50: 120, -49: 119, -48: 118, -47: 118, -46: 117, -45: 116, -44: 116, -43: 115, -42: 114, -41: 114, -40: 113, -39: 112, -38: 112, -37: 111, -36: 111, -35: 110, -34: 109, -33: 109, -32: 108, -31: 108, -30: 107, -29: 106, -28: 106, -27: 105, -26: 105, -25: 104, -24: 103, -23: 103, -22: 102, -21: 102, -20: 101, -19: 100, -18: 100, -17: 99, -16: 99, -15: 98, -14: 98, -13: 97, -12: 96, -11: 96, -10: 95, -9: 95, -8: 94, -7: 94, -6: 93, -5: 92, -4: 92, -3: 91, -2: 91}


def make_tables():
    """generate the code above (to be copy-pasted into this module)"""
    cos_table = tuple(int(math.cos(math.radians(a)) * PRECISION)
                      for a in range(360))
    sin_table = tuple(int(math.sin(math.radians(a)) * PRECISION)
                      for a in range(360))
    acos_table = dict(((c, int(math.degrees(math.acos(c / 100.0))))
                       for c in range(-100, 101)))
    print "_COS_TABLE =", cos_table
    print "_SIN_TABLE =", sin_table
    print "_ACOS_TABLE =", acos_table


def to_int(s):
    """convert a string to an integer with PRECISION"""
    assert isinstance(s, str)  # don't convert twice!
    result = int(float(s) * PRECISION)
    if isinstance(result, long):
        warning("%s is a long integer (greater than %s).", result, sys.maxint)
    return result


def int_cos_1000(angle):
    """angle in degrees; result = cos(angle) * 1000"""
    assert isinstance(angle, int)
    return _COS_TABLE[angle % 360]


def int_sin_1000(angle):
    """angle in degrees; result = sin(angle) * 1000"""
    assert isinstance(angle, int)
    return _SIN_TABLE[angle % 360]


def square_of_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return dx * dx + dy * dy


def int_distance(x1, y1, x2, y2):
    return int_sqrt(square_of_distance(x1, y1, x2, y2))


def int_sqrt(x):
    """should return the same integer square root on any computer"""
    r = int(math.sqrt(x))
    while r * r > x:
        warning("sqrt(%s): removing 1 to %s" % (x, r))
        r -= 1
    while (r + 1) * (r + 1) < x:
        warning("sqrt(%s): adding 1 to %s" % (x, r))
        r += 1
    return r


def int_angle(x1, y1, x2, y2):
    """return the angle with the x-axis (in degrees)"""
    d = int_distance(x1, y1, x2, y2)
    if d == 0:
        return 0
    c = (x2 - x1) * 100 / d  # 100 for the table
    ac = _ACOS_TABLE[c]
    if y2 - y1 > 0:
        return ac
    else:
        return - ac
