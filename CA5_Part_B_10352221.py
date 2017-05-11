#CA5 - Part B 'Calculator to handle lists'
#Student No: 10352221
#github: https://github.com/AndrewKennyDBS/programming_big_data_10352221.git
        
def add(first, second):                                                             #Function 1 - Addition
    return map(lambda x, y: x+y, first, second)
        
def subtract(first, second):                                                        #Function 2 - Subtraction
    return map(lambda x, y: x-y, first, second)
        
def multiply(first, second):                                                        #Function 3 - Multiplication
    return map(lambda x, y: x*y, first, second) 
        
def divide(first, second):                                                          #Function 4 - Division
    return map(lambda x, y: x/y, first, second) 
        
def exponent(first, second):                                                        #Function 5 - Exponent
    return map(lambda x, y: x ** y, first, second)

def miles_to_km(values):                                                            #Function 6 - Miles to Kilometre conversion
    return [ (float(x * 1.609)) for x in values ]
    
def km_to_miles(values):                                                            #Function 7 - Kilometre to Miles conversion
    return [ (float(x / 1.609)) for x in values ]
    
def mph_to_mps(values):                                                             #Function 8 - Miles per hour to Metres per second conversion
    return [ (float(x * 0.447)) for x in values ]
    
def mps_to_mph(values):                                                             #Function 9 - Metres per second to Miles per hour conversion
    return [ (float(x / 0.447)) for x in values ]
    
def mph_to_fps(values):                                                             #Function 10 - Miles per hour converts to Feet per second conversion
    return [ (float(x * 1.466)) for x in values ]
    
print "Add answer = ", add([47, 11, 42, 13], [37, 21, 22, 33])
print "Subtract answer = ", subtract([47, 11, 42, 13], [37, 21, 22, 33])
print "Multiply answer = ", multiply([3, 4, 5, 6], [4, 4, 5, 6]) 
print "Divide answer = ", divide([12, 9, 5, 12], [4, 4, 5, 6])
print "Exponent answer = ", exponent([12, 9, 5, 12], [4, 4, 5, 6])
print "Miles to Km Conversion = ", miles_to_km([1, 10, 100, 1000])
print "Km to Miles Conversion = ", km_to_miles([1, 10, 100, 1000])
print "MPH to MPS Conversion = ", mph_to_mps([1, 10, 100, 1000])
print "MPS to MPH Conversion = ", mps_to_mph([1, 10, 100, 1000])
print "MPH to FPS Conversion = ", mph_to_fps([1, 10, 100, 1000])