class Reservation:
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children

class RestaurantReservationSystem:
    def __init__(self):
        self.reservations = []
        self.txt_file = "RESTAURANT_RESERVATION_SYSTEM.txt"

    def save_data(self):
        with open(self.txt_file, "a") as file:
            for idx, reservation in enumerate(self.reservations, start=1):
                file.write(
                    f"{idx} {reservation.date} {reservation.time} {reservation.name} {reservation.adults} {reservation.children}\n")

    def display_menu(self):
        print("\nSystem Menu")
        print("a. View all Reservations")
        print("b. Make Reservation")
        print("c. Delete Reservation")
        print("d. Generate Report")
        print("e. Exit")

    def view_reservations(self):
        if not self.reservations:
            print("--------------------------------")
            print("No reservations found.")
            print("--------------------------------")
        else:
            print("--------------------------------\nViewing Reservation...\n")
            print("# Date Time Name Adults Children")
            for idx, reservation in enumerate(self.reservations, start=1):
                print(f"{idx} {reservation.date} {reservation.time} {reservation.name} {reservation.adults} {reservation.children}")
            print("--------------------------------")
    def make_reservation(self):
        print("--------------------------------")
        print("Making Reservation...\n")
        name = input("Enter name: ")
        date = input("Enter date (e.g., Nov 10, 2020): ")
        time = input("Enter time (e.g., 10:00 am): ")
        adults = int(input("Enter number of adults: "))
        children = int(input("Enter number of children: "))
        reservation = Reservation(name, date, time, adults, children)
        self.reservations.append(reservation)
        print("\nReservation made successfully!")
        print("--------------------------------")

    def delete_reservation(self):
        try:
            print("--------------------------------")
            reservation_number = int(input("Enter reservation number to delete: "))
            if reservation_number < 1 or reservation_number > len(self.reservations):
                print("--------------------------------")
                print("Invalid reservation number.")
                print("--------------------------------")
            else:
                print("--------------------------------")
                del self.reservations[reservation_number - 1]
                print("Reservation deleted successfully!")
                print("--------------------------------")
        except ValueError:
            print("--------------------------------")
            print("Invalid input. Please enter a valid reservation number.")
            print("--------------------------------")

    def generate_report(self):
        print("--------------------------------\nGenerating Report...")
        print("# Date Time Name Adults Children Subtotal")
        total_adults = 0
        total_children = 0
        grand_total = 0
        for idx, reservation in enumerate(self.reservations, start=1):
            subtotal = (reservation.adults * 800) + (reservation.children * 500)
            total_adults += reservation.adults
            total_children += reservation.children
            grand_total += subtotal
            print(f"{idx} {reservation.date} {reservation.time} {reservation.name} {reservation.adults} {reservation.children} {subtotal:.2f}")
        print(f"Total number of adults: {total_adults}")
        print(f"Total number of children: {total_children}")
        print(f"Grand Total: PHP {grand_total:.2f}")
        print("--------------------------------")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip().lower()
            if choice == 'a':
                self.view_reservations()
            elif choice == 'b':
                self.make_reservation()
            elif choice == 'c':
                self.delete_reservation()
            elif choice == 'd':
                self.generate_report()
            elif choice == 'e':
                print("Thank you!")
                self.save_data()
                break
            else:
                print("Invalid choice. Please select a valid option.")


reservation_system = RestaurantReservationSystem()
reservation_system.run()
