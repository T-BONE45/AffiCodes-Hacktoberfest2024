class ParkingArea:
    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.parked_vehicles = {}

    def park_vehicle(self, vehicle_number):
        if len(self.parked_vehicles) < self.num_slots:
            self.parked_vehicles[vehicle_number] = True
            print(f"Vehicle {vehicle_number} parked successfully.")
        else:
            print("Parking area is full. Cannot park vehicle.")

    def retrieve_vehicle(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            del self.parked_vehicles[vehicle_number]
            print(f"Vehicle {vehicle_number} retrieved successfully.")
        else:
            print("Vehicle not found in the parking area.")

    def check_availability(self):
        available_slots = self.num_slots - len(self.parked_vehicles)
        print(f"Available parking slots: {available_slots}")


def main():
    num_slots = int(input("Enter the number of parking slots: "))
    parking_area = ParkingArea(num_slots)

    while True:
        print("\n1. Park Vehicle")
        print("2. Retrieve Vehicle")
        print("3. Check Availability")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            vehicle_number = input("Enter vehicle number: ")
            parking_area.park_vehicle(vehicle_number)
        elif choice == 2:
            vehicle_number = input("Enter vehicle number: ")
            parking_area.retrieve_vehicle(vehicle_number)
        elif choice == 3:
            parking_area.check_availability()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
