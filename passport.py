class Passport:
    def __init__(self, passport_number, name, dob, nationality, expiration_date):
        self.passport_number = passport_number
        self.name = name
        self.dob = dob
        self.nationality = nationality
        self.expiration_date = expiration_date

    def display_details(self):
        print(f"Passport Number: {self.passport_number}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Nationality: {self.nationality}")
        print(f"Expiration Date: {self.expiration_date}")


class InternationalPassport(Passport):
    def __init__(self, passport_number, name, dob, nationality, expiration_date, visa_country):
        super().__init__(passport_number, name, dob, nationality, expiration_date)
        self.visa_country = visa_country

    def display_details(self):
        super().display_details()
        print(f"Visa Country: {self.visa_country}")


class PassportSystem:
    def __init__(self):
        self.passports = []

    def add_passport(self, passport):
        self.passports.append(passport)

    def find_passport(self, passport_number):
        for passport in self.passports:
            if passport.passport_number == passport_number:
                return passport
        return None

    def update_passport(self, passport_number, new_passport):
        passport = self.find_passport(passport_number)
        if passport:
            index = self.passports.index(passport)
            self.passports[index] = new_passport

    def delete_passport(self, passport_number):
        passport = self.find_passport(passport_number)
        if passport:
            self.passports.remove(passport)

    def view_all_passports(self):
        for index, passport in enumerate(self.passports, start=1):
            print(f"\nPassport {index}:")
            passport.display_details()
            

# Creating passport system
passport_system = PassportSystem()

# Menu-driven application loop
while True:
    print("\nPassport Management System")
    print("1. Add Passport")
    print("2. Update Passport")
    print("3. Delete Passport")
    print("4. View All Passports")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        passport_number = input("Enter Passport Number: ")
        name = input("Enter Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        nationality = input("Enter Nationality: ")
        expiration_date = input("Enter Expiration Date (YYYY-MM-DD): ")
        visa_country = input("Enter Visa Country (only for International Passport): ")
        passport = Passport(passport_number, name, dob, nationality, expiration_date)
        if visa_country:
            passport = InternationalPassport(passport_number, name, dob, nationality, expiration_date, visa_country)
        passport_system.add_passport(passport)
        print("Passport added successfully.")

    elif choice == '2':
        passport_number = input("Enter Passport Number to update: ")
        passport = passport_system.find_passport(passport_number)
        if passport:
            name = input("Enter new Name: ")
            dob = input("Enter new Date of Birth (YYYY-MM-DD): ")
            nationality = input("Enter new Nationality: ")
            expiration_date = input("Enter new Expiration Date (YYYY-MM-DD): ")
            if isinstance(passport, InternationalPassport):
                visa_country = input("Enter new Visa Country: ")
                new_passport = InternationalPassport(passport_number, name, dob, nationality, expiration_date, visa_country)
            else:
                new_passport = Passport(passport_number, name, dob, nationality, expiration_date)
            passport_system.update_passport(passport_number, new_passport)
            print("Passport updated successfully.")
        else:
            print("Passport not found.")

    elif choice == '3':
        passport_number = input("Enter Passport Number to delete: ")
        passport = passport_system.find_passport(passport_number)
        if passport:
            passport_system.delete_passport(passport_number)
            print("Passport deleted successfully.")
        else:
            print("Passport not found.")

    elif choice == '4':
        passport_system.view_all_passports()

    elif choice == '5':
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
