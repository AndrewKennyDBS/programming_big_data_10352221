#CA5 - Part B Tests
#Student No: 10352221
#github: https://github.com/AndrewKennyDBS/programming_big_data_10352221.git

import unittest

from CA5_Part_B_10352221 import add, subtract, multiply, divide, exponent, miles_to_km, km_to_miles, mph_to_mps, mph_to_fps

def setUp(self):
        self.calc = CA5_Part_B_10352221()
        
def test_calculator_add_method(self):                                                   # 1. Testing Addition
        result = self.calc.add(1, 1)
        self.assertEqual(2, result)             # 1 + 1 = 2
        result = self.calc.add(1,2)     
        self.assertEqual(3, result)             # 1 + 2 = 3
        result = self.calc.add(1, -1)
        self.assertEqual(0, result)             # 1 + (-1) = 0
        
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.add, 'two', 0)
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        
def test_calculator_subtract_method(self):                                              
        result = self.calc.subtract(1, 1)
        self.assertEqual(0, result)             # 1 - 1 = 0
        result = self.calc.subtract(1,2)
        self.assertEqual(-1, result)            # 1 - 2 = -1
        result = self.calc.subtract(1, -1)
        self.assertEqual(2, result)             

        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 0)
        self.assertRaises(ValueError, self.calc.subtract, 2, 'three')
        
def test_calculator_multiply_method(self):                                              # 3. Testing Mulitiplication
        result = self.calc.multiply(1, 1)      
        self.assertEqual(1, result)             # 1 x 1 = 1
        result = self.calc.multiply(1,2)
        self.assertEqual(2, result)             # 1 x 2 = 2
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)            # 2 x -2 = -4
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)             # 2 x 0 = 0
        
        self.assertRaises(ValueError, self.calc.multiply, 'two', 'three')
        self.assertRaises(ValueError, self.calc.multiply, 'two', 0)
        self.assertRaises(ValueError, self.calc.multiply, 2, 'three')

def test_calculator_divide_method(self):                                                # 4. Testing Division
        result = self.calc.divide(1, 1)
        self.assertEqual(1, result)             # 1 / 1 = 1
        result = self.calc.divide(2,1)
        self.assertEqual(2, result)             # 2 / 1 = 2
        result = self.calc.divide(1, -1)
        self.assertEqual(-1, result)            # 1 / -1 = -1
        result = self.calc.divide(1, 2)
        self.assertEqual(0.5, result)           # 1 / 2 = 0.5
        result = self.calc.divide(1, 0)
        self.assertEqual('NaN', result)         # 1 / 0 = NaN
        
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 0)
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')

def test_calculator_exponent_method(self):                                              # 5. Testing Exponent
        result = self.calc.exponent(1, 1)
        self.assertEqual(1, result)             # 1 ** 1 = 1
        result = self.calc.exponent(2, 2)       
        self.assertEqual(4, result)             # 2 ** 2 = 4
        result = self.calc.exponent(2,4)
        self.assertEqual(16, result)            # 2 ** 4 = 16
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)          # 2 ** -2 = 0.25
        
        self.assertRaises(ValueError, self.calc.exponent, 'two', 'three')
        self.assertRaises(ValueError, self.calc.exponent, 'two', 0)
        self.assertRaises(ValueError, self.calc.exponent, 2, 'three')
        
def test_miles_to_km(self):                                                             # 6. Testing Miles to Kilometres Conversion
        result = self.conversion.miles_to_km(1)
        self.assertEqual(1.609, result)             #1 mile = 1.609 kilometres
        result = self.conversion.miles_to_km(10)
        self.assertEqual(16.09, result)             #10 miles = 16.09 kilometres
        
        self.assertRaises(ValueError, self.conversion.miles_to_km, 'two')
      
def test_km_to_miles(self):                                                                  # 7. Testing Kilometres to Miles Conversion
        result = self.conversion.km_to_miles(1.609)
        self.assertEqual(1, result)                 #1.609 kilometres = 1 mile
        result = self.conversion.km_to_miles(16.09)
        self.assertEqual(10, result)                #16.09 kilometres = 10 miles
        
        self.assertRaises(ValueError, self.conversion.km_to_miles, 'two')

def test_mph_to_mps(self):                                                                  # 8. Testing Miles per hour to Metres per second
        result = self.conversion.mph_to_mps(1)
        self.assertEqual(0.447, result)                 #1 mph = 0.447 mps
        result = self.conversion.mph_to_mps(10)
        self.assertEqual(4.47, result)                #10 mph = 4.47 mps
        
        self.assertRaises(ValueError, self.conversion.mph_to_mps, 'two')
    
def test_mps_to_mph(self):                                                                  # 9. Testing Metres per second to Miles per hour
        result = self.conversion.mps_to_mph(0.447)
        self.assertEqual(1, result)                 #0.447 mps = 1 mph
        result = self.conversion.mps_to_mph(4.47)
        self.assertEqual(10, result)                #4.47 mps = 10 mph
        
        self.assertRaises(ValueError, self.conversion.mps_to_mph, 'two')
        
def test_mph_to_fps(self):                                                                  # 10. Testing Miles per hour to Feet per second
        result = self.conversion.mph_to_fps(1)
        self.assertEqual(1.466, result)                 #1 mph = 1.466 fps
        result = self.conversion.mph_to_fps(10)
        self.assertEqual(14.66, result)                #10 mph = 14.66 fps
        
        self.assertRaises(ValueError, self.conversion.mph_to_fps, 'two')   

        
if __name__ == '__main__':
    unittest.main()