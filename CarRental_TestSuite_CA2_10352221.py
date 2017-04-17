#CA2 - Car Dealership "Aungier Car Rental" - Test Suite
#Student Number: 10352221
#https://github.com/AndrewKennyDBS/programming_big_data_10352221.git

import unittest

from Aungier_Car_Rental_CA2_10352221 import Fleet, PetrolCar, DieselCar, ElectricCar, HybridCar, CarRental

class TestCar(unittest.TestCase):                                               # Test the fleet functionality

    def test_car_engine(self):                                                  # Testing Car Engine Type
        self.fleet = Fleet()
        self.assertEqual('', self.fleet.getCarEngineType())
        self.fleet.setEngine('Hydrogen')
        self.assertEqual('Hydrogen', self.fleet.getCarEngineType())
        
    def test_stock_count(self):                                                 # Testing Fleet Stock Count
        self.fleet = Fleet()
        self.assertEqual(0, self.fleet.getCarStockCount())
        self.fleet.setStock(23)
        self.assertEqual(23, self.fleet.getCarStockCount())
        		
    def test_petrol_car_stock(self):                                            # Testing Petrol Car Stock Count
		petrol_car = PetrolCar()
		self.assertEqual(20, petrol_car.getPetrolStock())
		petrol_car.setPetrolStock(14)
		self.assertEqual(14, petrol_car.getPetrolStock())
        
    def test_diesel_car_stock(self):                                            # Testing Diesel Car Stock Count
		diesel_car = DieselCar()
		self.assertEqual(8, diesel_car.getDieselStock())
		diesel_car.setDieselStock(4)
		self.assertEqual(4, diesel_car.getDieselStock())
        
    def test_electric_car_stock(self):                                          # Testing Electric Car Stock Count
		electric_car = ElectricCar()
		self.assertEqual(4, electric_car.getElectricStock())
		electric_car.setElectricStock(2)
		self.assertEqual(2, electric_car.getElectricStock())
        
    def test_hybrid_car_stock(self):                                            # Testing Hybrid Car Stock Count
		hybrid_car = HybridCar()
		self.assertEqual(8, hybrid_car.getHybridStock())
		hybrid_car.setHybridStock(20)
		self.assertEqual(20, hybrid_car.getHybridStock())
        
    def test_car_rental(self):                                                  # Testing the Car Rental
        car_rental = CarRental()
        self.assertEqual(40, car_rental.getRentalPool())                        

        car_rental.rentCar(5)                                                   # Testing Rent Car
        self.assertEqual(35, car_rental.getRentalPool())
        
        car_rental.returnCar(3)
        self.assertEqual(38, car_rental.getRentalPool())                        # Testing Return Car
        
        car_rental.stockControl(50)                                             # Testing Stock Control
        car_rental.stockControl(30)     
        
if __name__ == '__main__':
    unittest.main()