import os

def show_menu():
    print("\n=== Medicine Schedule Tracker ===")
    print("1. Add a new medicine")
    print("2. View schedule")
    print("3. Exit")

def add_medicine():
    name = input("Enter medicine name: ")
    dose = input("Enter dose (e.g. 500mg): ")
    time = input("Enter time (e.g. 8 AM, after lunch): ")

    with open("med_schedule.txt", "a") as file:
        file.write(f"{name} | {dose} | {time}\n")

    print("Medicine added successfully!")

def view_schedule():
    if not os.path.exists("med_schedule.txt"):
        print("No medicines added yet.")
        return

    print("\n--- Your Medicine Schedule ---")
    with open("med_schedule.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No medicines scheduled.")
        else:
            for i, line in enumerate(lines, 1):
                name, dose, time = line.strip().split(" | ")
                print(f"{i}. {name} - {dose} at {time}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            view_schedule()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
