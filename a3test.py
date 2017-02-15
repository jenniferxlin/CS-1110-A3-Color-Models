# a3test.py
# Jennifer Lin
# October 6, 2016
""" Unit Test for Assignment A3"""

import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71),
                              a3.complement_rgb(colormodel.RGB(250, 0, 71)))


def test_round():
    """Test function round (a3 version)"""
    cornelltest.assert_equals(130.6,   a3.round(130.59,1))
    cornelltest.assert_equals(130.5,   a3.round(130.54,1))
    cornelltest.assert_equals(100.0,   a3.round(100,1))
    cornelltest.assert_equals(100.6,   a3.round(100.55,1))
    cornelltest.assert_equals(99.57,   a3.round(99.566,2))
    cornelltest.assert_equals(99.99,   a3.round(99.99,2))
    cornelltest.assert_equals(100.0,   a3.round(99.995,2))
    cornelltest.assert_equals(22.00,   a3.round(21.99575,2))
    cornelltest.assert_equals(21.99,   a3.round(21.994,2))
    cornelltest.assert_equals(10.01,   a3.round(10.013567,2))
    cornelltest.assert_equals(10.0,    a3.round(10.000000005,2))
    cornelltest.assert_equals(10.0,    a3.round(9.9999,3))
    cornelltest.assert_equals(9.999,   a3.round(9.9993,3))
    cornelltest.assert_equals(1.355,   a3.round(1.3546,3))
    cornelltest.assert_equals(1.354,   a3.round(1.3544,3))
    cornelltest.assert_equals(0.046,   a3.round(.0456,3))
    cornelltest.assert_equals(0.045,   a3.round(.0453,3))
    cornelltest.assert_equals(0.006,   a3.round(.0056,3))
    cornelltest.assert_equals(0.001,   a3.round(.0013,3))
    cornelltest.assert_equals(0.0,     a3.round(.0004,3))
    cornelltest.assert_equals(0.001,   a3.round(.0009999,3))
    #Added test cases
    cornelltest.assert_equals(1.4,   a3.round(1.369,1))
    cornelltest.assert_equals(83.1,   a3.round(83.123,1))
    cornelltest.assert_equals(0.0,   a3.round(.02,1))
    cornelltest.assert_equals(3.0,   a3.round(2.9999999,2))
    cornelltest.assert_equals(3.0,   a3.round(2.9999999,3))
    cornelltest.assert_equals(100.909,   a3.round(100.9090909090,3))


def test_str5():
    """Test function str5"""
    cornelltest.assert_equals('130.6',  a3.str5(130.59))
    cornelltest.assert_equals('130.5',  a3.str5(130.54))
    cornelltest.assert_equals('100.0',  a3.str5(100))
    cornelltest.assert_equals('100.6',  a3.str5(100.55))
    cornelltest.assert_equals('99.57',  a3.str5(99.566))
    cornelltest.assert_equals('99.99',  a3.str5(99.99))
    cornelltest.assert_equals('100.0',  a3.str5(99.995))
    cornelltest.assert_equals('22.00',  a3.str5(21.99575))
    cornelltest.assert_equals('21.99',  a3.str5(21.994))
    cornelltest.assert_equals('10.01',  a3.str5(10.013567))
    cornelltest.assert_equals('10.00',  a3.str5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.str5(9.9999))
    cornelltest.assert_equals('9.999',  a3.str5(9.9993))
    cornelltest.assert_equals('1.355',  a3.str5(1.3546))
    cornelltest.assert_equals('1.354',  a3.str5(1.3544))
    cornelltest.assert_equals('0.046',  a3.str5(.0456))
    cornelltest.assert_equals('0.045',  a3.str5(.0453))
    cornelltest.assert_equals('0.006',  a3.str5(.0056))
    cornelltest.assert_equals('0.001',  a3.str5(.0013))
    cornelltest.assert_equals('0.000',  a3.str5(.0004))
    cornelltest.assert_equals('0.001',  a3.str5(.0009999))
    #Added test cases
    cornelltest.assert_equals('0.020',  a3.str5(.02))
    cornelltest.assert_equals('0.000',  a3.str5(0))
    cornelltest.assert_equals('1.000',  a3.str5(.9999999))


def test_str5_color():
    """Test the str5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                              a3.str5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8,
                                                           1.0)));
    cornelltest.assert_equals('(100.0, 0.225, 83.50, 0.000)',
                              a3.str5_cmyk(colormodel.CMYK(100.0, .2245, 83.5,
                                                           0.0)))
    cornelltest.assert_equals('(56.00, 0.000, 0.987)',
                              a3.str5_hsv(colormodel.HSV(55.999, 0.0,
                                                         0.9874234353442)));
    cornelltest.assert_equals('(250.4, 1.000, 0.488)',
                              a3.str5_hsv(colormodel.HSV(250.356, 1.0,
                                                         .4878325345)));
    

def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(1,3,9);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('88.89', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('66.67', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('96.47', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(50,80,45);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('37.50', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('43.75', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('68.63', a3.str5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(0.0, 0.0, 0.0, 1.2356);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(252, rgb.red)
    cornelltest.assert_equals(252, rgb.green)
    cornelltest.assert_equals(252, rgb.blue)
    
    cmyk = colormodel.CMYK(7.1254, 100.0, 25.569, .123456032934);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(237, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(190, rgb.blue)
    
    cmyk = colormodel.CMYK(63.409, 2.0000001, 100.0, 83.099);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(16, rgb.red)
    cornelltest.assert_equals(42, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    cmyk = colormodel.CMYK(100.0, 54.99999, 3.694286, 100.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    rgb = colormodel.RGB(255, 255, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(245, 87, 7);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('20.17', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.971', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.961', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(99, 33, 33);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.667', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.388', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(54, 2, 3);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('358.8', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.963', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.212', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(99, 100, 98);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('90.00', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.020', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.392', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(100, 1, 150);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('279.9', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.993', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.588', a3.str5(hsv.value))

    rgb = colormodel.RGB(0, 0, 0);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.000', a3.str5(hsv.value))
    

def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    hsv = colormodel.HSV(30.54, 1.0, 0.54321);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(139, rgb.red)
    cornelltest.assert_equals(71, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    hsv = colormodel.HSV(78.93, 0.33, 0.02);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(5, rgb.red)
    cornelltest.assert_equals(5, rgb.green)
    cornelltest.assert_equals(3, rgb.blue)
    
    hsv = colormodel.HSV(125.666, 0.666, 1.00);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(85, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(101, rgb.blue)
    
    hsv = colormodel.HSV(188.808, 0.001, .115);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(29, rgb.red)
    cornelltest.assert_equals(29, rgb.green)
    cornelltest.assert_equals(29, rgb.blue)
    
    hsv = colormodel.HSV(255.22812234, .5532354326, .834098765432);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(125, rgb.red)
    cornelltest.assert_equals(95, rgb.green)
    cornelltest.assert_equals(213, rgb.blue)
    
    hsv = colormodel.HSV(341.0928346, .4088, 0.9234);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(235, rgb.red)
    cornelltest.assert_equals(139, rgb.green)
    cornelltest.assert_equals(170, rgb.blue)
    
# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == "__main__":
    test_complement() 
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
