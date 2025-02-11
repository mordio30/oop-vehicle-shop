class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, mileage):
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []
        CarManager.all_cars.append(self)

    def add_service(self, service):
        self._services.append(service)

    def update_mileage(self, mileage):
        if mileage >= self._mileage:
            self._mileage = mileage
        else:
            print("Mileage cannot be decreased.")

    def get_details(self):
        return (f"ID: {self._id}, Make: {self._make}, Model: {self._model}, "
                f"Year: {self._year}, Mileage: {self._mileage}, Services: {self._services}")

    @classmethod
    def view_all_cars(cls):
        return [car.get_details() for car in cls.all_cars]

    @classmethod
    def view_total_cars(cls):
        return cls.total_cars

    @classmethod
    def find_car_by_id(cls, car_id):
        for car in cls.all_cars:
            if car._id == car_id:
                return car
        return None


def main():
    while True:
        print("\n----  WELCOME  ----")
        print("1. Add a car")
        print("2. View all cars")
        print("3. View total number of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            mileage = int(input("Enter mileage: "))
            CarManager(make, model, year, mileage)
            print("Car added successfully!")
        
        elif choice == "2":
            cars = CarManager.view_all_cars()
            if cars:
                for car in cars:
                    print(car)
            else:
                print("No cars available.")

        elif choice == "3":
            print(f"Total number of cars: {CarManager.view_total_cars()}")
        
        elif choice == "4":
            car_id = int(input("Enter car ID: "))
            car = CarManager.find_car_by_id(car_id)
            if car:
                print(car.get_details())
            else:
                print("Car not found.")
        
        elif choice == "5":
            car_id = int(input("Enter car ID: "))
            car = CarManager.find_car_by_id(car_id)
            if car:
                service = input("Enter service performed: ")
                car.add_service(service)
                print("Service recorded successfully!")
            else:
                print("Car not found.")

        elif choice == "6":
            car_id = int(input("Enter car ID: "))
            car = CarManager.find_car_by_id(car_id)
            if car:
                mileage = int(input("Enter new mileage: "))
                car.update_mileage(mileage)
                print("Mileage updated successfully!")
            else:
                print("Car not found.")
        
        elif choice == "7":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
