class Fleet(object):											    
    
    def __init__(self):
        self.__engine = ''
        self.__stock = 0

    def getCarEngineType(self):
        return self.__engine
        
    def setEngine(self, engine):
        self.__engine = engine

    def getCarStockCount(self):
        return self.__stock
        
    def setStock(self, stock):
        self.__stock = stock

class PetrolCar(Fleet):
    def __init__(self):
		Fleet.__init__(self)
		self.__engine = 'petrol'
		self.__stock = 20
        
    def getPetrolStock(self):
		return self.__stock
        
    def setPetrolStock (self, PetrolStock):
        self.__stock = PetrolStock
               
class DieselCar(Fleet):
    def __init__(self):
		Fleet.__init__(self)
		self.__engine = 'diesel'
		self.__stock = 8
        
    def getDieselStock(self):
		return self.__stock
        
    def setDieselStock (self, DieselStock):
        self.__stock = DieselStock
         
class ElectricCar(Fleet):
    def __init__(self):
		Fleet.__init__(self)
		self.__engine = 'electric'
		self.__stock = 4
        
    def getElectricStock(self):
		return self.__stock
        
    def setElectricStock (self, ElectricStock):
        self.__stock = ElectricStock
               
class HybridCar(Fleet):
    def __init__(self):
		Fleet.__init__(self)
		self.__engine = 'hybrid'
		self.__stock = 8
        
    def getHybridStock(self):
		return self.__stock
        
    def setHybridStock (self, HybridStock):
        self.__stock = HybridStock
               
class CarRental(object):											    
    
    def __init__(self):
        self.__cars = []
        self.__rentalPool = 40

    def getRentalPool(self):
        return self.__rentalPool
        
    def rentCar(self, numCars):
        self.__rentalPool -= numCars
        print('Total Cars Available: ' + str(self.__rentalPool))

    def returnCar(self, numCars):
        self.__rentalPool += numCars
        print('Total Cars Available: ' + str(self.__rentalPool))   
      
    def stockControl(self, numCars):
        if self.__rentalPool < numCars:
            print 'SORRY nothing to rent. Please try again.'
            return
        while self.__rentalPool > numCars:
            print('Total Cars Available: ' + str(self.__rentalPool)) 
            return