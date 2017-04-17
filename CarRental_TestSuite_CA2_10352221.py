import unittest

from Aungier_Car_Rental_CA2_10352221 import Fleet, PetrolCar, DieselCar, ElectricCar, HybridCar, CarRental

class TestCar(unittest.TestCase):

    def test_car_engine(self):
        self.fleet = Fleet()
        self.assertEqual('', self.fleet.getCarEngineType())
        self.fleet.setEngine('Hydrogen')
        self.assertEqual('Hydrogen', self.fleet.getCarEngineType())
        
    def test_stock_count(self):
        self.fleet = Fleet()
        self.assertEqual(0, self.fleet.getCarStockCount())
        self.fleet.setStock(23)
        self.assertEqual(23, self.fleet.getCarStockCount())
        		
    def test_petrol_car_stock(self):
		petrol_car = PetrolCar()
		self.assertEqual(20, petrol_car.getPetrolStock())
		petrol_car.setPetrolStock(14)
		self.assertEqual(14, petrol_car.getPetrolStock())
        
    def test_diesel_car_stock(self):
		diesel_car = DieselCar()
		self.assertEqual(8, diesel_car.getDieselStock())
		diesel_car.setDieselStock(4)
		self.assertEqual(4, diesel_car.getDieselStock())
        
    def test_electric_car_stock(self):
		electric_car = ElectricCar()
		self.assertEqual(4, electric_car.getElectricStock())
		electric_car.setElectricStock(2)
		self.assertEqual(2, electric_car.getElectricStock())
        
    def test_hybrid_car_stock(self):
		hybrid_car = HybridCar()
		self.assertEqual(8, hybrid_car.getHybridStock())
		hybrid_car.setHybridStock(20)
		self.assertEqual(20, hybrid_car.getHybridStock())
        
    def test_car_rental(self):
        car_rental = CarRental()
        self.assertEqual(40, car_rental.getRentalPool())

        car_rental.rentCar(5)
        self.assertEqual(35, car_rental.getRentalPool())
        
        car_rental.returnCar(3)
        self.assertEqual(38, car_rental.getRentalPool())
        
        car_rental.stockControl(50)
        car_rental.stockControl(30)
        
if __name__ == '__main__':
    unittest.main()