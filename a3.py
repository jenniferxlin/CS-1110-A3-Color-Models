# a3.py
# Jennifer Lin
# October 6, 2016
# Mia and Meghan suggested ways for how to write some of my code.
""" Functions for Assignment A3"""

import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object"""
    
    return colormodel.RGB((255-rgb.red), (255-rgb.green), (255-rgb.blue))


def round(number, places):
    """Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3"""
    
    #Cast number to float
    num = float(number)
    
    #Shift number of digits (places) to the left
    shift = num * (10**places)
    
    #Add 0.5 to this number and convert to int 
    right = int (shift + 0.5)
    
    #Shift the same number of digits back to the right to make new rounded  
    return right/(10.0**places)
    

def str5(value):
    """ Returns: value as a string, but expand or round to be exactly 5
    characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360."""
    
    # Cast value to float
    dec_value = float(value)
    
    # Mia (mvb43) suggested focusing on places after decimal rather than
    # casting to string immediately
    #If no digit or single digit in front decimal 
    if 0 <= dec_value < 10:
        a = str(round(dec_value,3))
        
    #If there are 2 digits in front of decimal 
    elif 10 <= dec_value < 100:
        a = str(round(dec_value,2))
        
    #If there are 3 digits in front of decimal
    else:
        a = str(round(dec_value,1))
    #End of Mia's suggestion
    
    # Meghan (mc2254) explained this concept of how to add zeros if rounded
    # number is not five characters
    b = a + '00000'
    return b[:5]


def str5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces
    after the commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object."""
    
    #Attributes of cmyk rounded and reduced to 5 characters
    a = str5(cmyk.cyan)

    b = str5(cmyk.magenta)
    
    c = str5(cmyk.yellow)
    
    d = str5(cmyk.black)
    
    return '(' + a + ', ' + b + ', ' + c + ', ' + d + ')'


def str5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object."""
    
    #Attributes of hsv rounded and reduced to 5 characters
    a = str5(hsv.hue)
    
    b = str5(hsv.saturation)
    
    c = str5(hsv.value)
    
    return '(' + a + ', ' + b + ', ' + c + ')'


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object"""
    
    # Divide all rgb values by 255.0 to change range from 0..255.0 to 0..1.0
    r = rgb.red / 255.0
    g = rgb.green / 255.0
    b = rgb.blue / 255.0
    
    #Subtract all rgb values from 1
    c = 1 - r
    m = 1 - g
    y = 1 - b
    
    #Change all CMYK values to 0 except black
    if c == 1 and m == 1 and y == 1: 
        return colormodel.CMYK(0.0,0.0,0.0,1.0*100.0)
    else:
        k = min(c,m,y)
        cy = ((c-k)/(1-k))*100.0
        mag = ((m-k)/(1-k))*100.0
        yell = ((y-k)/(1-k))*100.0
        return colormodel.CMYK(cy,mag,yell,k*100.0)


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object."""
    
    # Divide all rgb values by 100 to change range from 0..100.0 to 0..1.0
    c = cmyk.cyan / 100
    m = cmyk.magenta / 100
    y = cmyk.yellow / 100
    k = cmyk.black / 100
    
    #Cmyk to rgb conversion formulas
    r = ((1-c)*(1-k))*255
    g = ((1-m)*(1-k))*255
    b = ((1-y)*(1-k))*255
    
    #Round numbers to convert values to int
    r1 = int(round(r,0))
    g1 = int(round(g,0))
    b1 = int(round(b,0))
    
    #Return rgb values
    return colormodel.RGB(r1,g1,b1)
    
    
def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object"""

    # Divide all rgb values by 255.0 to change range from 0..255.0 to 0..1.0 
    r = rgb.red / 255.0
    g = rgb.green / 255.0
    b = rgb.blue / 255.0
    
    #Minimum and maximum of rgb values
    MAX = max(r,g,b)
    MIN = min (r,g,b)
    
    if MAX == MIN:
        h = 0
    elif MAX == r and g >= b:
        h = 60.0 * (g - b) / (MAX - MIN)
    elif MAX == r and g < b:
        h = 60.0 * (g - b) / (MAX - MIN) + 360.0
    elif MAX == g:
        h = 60.0 * (b - r) / (MAX - MIN) + 120.0
    elif MAX == b:
        h = 60.0 * (r - g) / (MAX - MIN) + 240.0
    
    if MAX == 0:
        s = 0
    else:
        s = 1 - MIN/MAX
        
    v = MAX
    
    return colormodel.HSV(h,s,v)
    

def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object."""
    
    #Attributes of hsv
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    
    #Computed values for conversion
    hi = math.floor(h/60) 
    f = h/60 - hi
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    
    if hi == 0:
        r = v
        g = t
        b = p
    elif hi == 1:
        r = q
        g = v
        b = p
    elif hi == 2:
        r = p
        g = v
        b = t
    elif hi == 3:
        r = p
        g = q
        b = v
    elif hi == 4:
        r = t
        g = p
        b = v
    elif hi == 5:
        r = v
        g = p
        b = q
    
    #Round numbers to convert values to int
    r1 = int(round(r*255.0,0))
    g1 = int(round(g*255.0,0))
    b1 = int(round(b*255.0,0))
    
    return colormodel.RGB(r1,g1,b1)
    