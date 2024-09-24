import csv
from datetime import datetime
from tkinter import Tk, filedialog
from prettytable import PrettyTable

# Hide Tkinter GUI window for file dialog
root = Tk()
root.withdraw()

# Display welcome message
def display_start_message():
    print("Welcome to BillBuddy - A simple tool to manage shared expenses.")
    print("1. Choose from an existing CSV file")
    print("2. Start from the beginning")

# Function to ask for CSV file and validate it
def load_csv():
    file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        print(f"Loading CSV file from: {file_path}")
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Check the headers
            if headers == ['Person', 'Expense Description', 'Amount Paid', 'Date & Time', 'Total by Person', 'Settlement']:
                print("Valid CSV file format!")
                display_table(file_path)
                return file_path
            else:
                print("Invalid CSV file format. Please check your file.")
                return None
    else:
        print("No file selected.")
        return None

# Calculate the total expenses and settlement
def calculate_totals(file_path):
    payments = {}
    total_expense = 0
    num_people = 0
    people_totals = {}

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            person, occasion, amount, timestamp, _, _ = row
            amount = round(float(amount), 2)
            total_expense += amount
            if person in people_totals:
                people_totals[person] += amount
            else:
                people_totals[person] = amount

    num_people = len(people_totals)
    per_person_share = round(total_expense / num_people, 2) if num_people > 0 else 0

    for person, total in people_totals.items():
        payments[person] = {
            "total": round(total, 2),
            "settlement": round(total - per_person_share, 2)
        }

    return payments, total_expense, per_person_share

# Display the current data in the CSV with total per person and settlement
def display_table(file_path):
    payments, total_expense, per_person_share = calculate_totals(file_path)
    
    table = PrettyTable()
    table.field_names = ['Person', 'Expense Description', 'Amount Paid', 'Date & Time', 'Total by Person', 'Settlement']

    last_person = None  # Used to merge duplicate names
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            person, occasion, amount, timestamp, _, _ = row
            total_by_person = payments[person]['total']
            settlement = payments[person]['settlement']
            if person == last_person:
                table.add_row(['', occasion, f"{float(amount):.2f}", timestamp, '', ''])
            else:
                table.add_row([person, occasion, f"{float(amount):.2f}", timestamp, total_by_person, settlement])
                last_person = person

    print(f"\nGross Total: {total_expense:.2f}")
    print(f"Per Person Share: {per_person_share:.2f}")
    print(table)

# Add new payment to the CSV and update the total and settlement
def add_payment(file_path):
    print("Choose a person from the following:")
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        people = sorted(set(row[0] for row in reader))  # Sort the names alphabetically

    for i, person in enumerate(people, start=1):
        print(f"{i}. {person}")

    while True:
        try:
            person_choice = int(input("Select a person by number: ")) - 1
            if person_choice < 0 or person_choice >= len(people):
                raise ValueError("Invalid choice. Please select a valid number.")
            person = people[person_choice]
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    occasion = input("What was the payment for? ")
    while True:
        try:
            price = float(input("How much was the payment? "))
            if price < 0:
                raise ValueError("Amount cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid amount.")

    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
    
    updated_rows = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        updated_rows.append(headers)
        payment_added = False

        for row in reader:
            if row[0] == person and not payment_added:
                updated_rows.append([person, occasion, price, timestamp, '', ''])  # Add new payment
                payment_added = True
            updated_rows.append(row)

    # If person not found, append to end
    if not payment_added:
        updated_rows.append([person, occasion, price, timestamp, '', ''])

    # Overwrite the CSV file with updated totals
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    update_csv_totals(file_path)
    display_table(file_path)  # Display updated data
    print("Payment added and totals updated successfully!")

# Add new person to the CSV
def add_person(file_path):
    name = input("Enter the name of the new person: ")
    
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, 'None', 0, datetime.now().strftime("%m/%d/%Y %H:%M"), 0, 0])
    
    update_csv_totals(file_path)
    display_table(file_path)  # Display updated data
    print(f"{name} added successfully and totals updated!")

# Create new CSV file from scratch
def create_csv():
    trip_name = input("Enter the trip name: ").strip().replace(" ", "_")
    file_path = filedialog.asksaveasfilename(title="Save CSV file", defaultextension=".csv", initialfile=f"{trip_name}.csv")
    
    if file_path:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Person', 'Expense Description', 'Amount Paid', 'Date & Time', 'Total by Person', 'Settlement'])
        
        print(f"New CSV file created: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return None

# Update totals in CSV after every change
def update_csv_totals(file_path):
    payments, total_expense, per_person_share = calculate_totals(file_path)
    
    updated_rows = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        updated_rows.append(headers)
        for row in reader:
            person, occasion, amount, timestamp, _, _ = row
            total_by_person = payments[person]['total']
            settlement = payments[person]['settlement']
            updated_rows.append([person, occasion, amount, timestamp, total_by_person, settlement])
    
    # Overwrite the CSV file with updated totals
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

# Main program loop
def main():
    display_start_message()
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        file_path = load_csv()
        if file_path:
            while True:
                display_table(file_path)  # Always display data after load
                print("\nOptions:")
                print("1. Add new payment")
                print("2. Add new person")
                print("3. Update and exit")
                option = input("Choose an option: ")
                
                if option == '1':
                    add_payment(file_path)
                elif option == '2':
                    add_person(file_path)
                elif option == '3':
                    print("Saving changes and exiting...")
                    break
    elif choice == '2':
        file_path = create_csv()
        if file_path:
            num_people = int(input("How many people are traveling? "))
            people = [input(f"Enter name for person {i+1}: ") for i in range(num_people)]
            
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                for person in people:
                    writer.writerow([person, 'None', 0, datetime.now().strftime("%m/%d/%Y %H:%M"), 0, 0])
            
            display_table(file_path)
            while True:
                print("\nOptions:")
                print("1. Add new payment")
                print("2. Add new person")
                print("3. Update and exit")
                option = input("Choose an option: ")
                
                if option == '1':
                    add_payment(file_path)
                elif option == '2':
                    add_person(file_path)
                elif option == '3':
                    print("Saving changes and exiting...")
                    break
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
