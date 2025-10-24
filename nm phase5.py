import csv
import os
FEEDBACK_FILE = 'feedbacks.csv'
def initialize_feedback_file():
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Rating', 'Comments'])
def submit_feedback():
    print("\n--- Submit Feedback ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    while True:
        try:
            rating = int(input("Rate us (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    comments = input("Enter your comments: ")
    with open(FEEDBACK_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, rating, comments])
    print("Feedback submitted successfully!")
def view_feedback():
    print("\n--- View Feedback ---")
    try:
        with open(FEEDBACK_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                print(f"\nName: {row[0]}")
                print(f"Email: {row[1]}")
                print(f"Rating: {row[2]}")
                print(f"Comments: {row[3]}")
                print("-" * 30)
    except FileNotFoundError:
        print("No feedbacks found.")
def main():
    initialize_feedback_file()
    while True:
        print("\n=== Feedback Collection System ===")
        print("1. Submit Feedback")
        print("2. View Feedback (Admin)")
        print("3. Exit")  
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            submit_feedback()
        elif choice == '2':
            password = input("Enter admin password: ")
            if password == "admin123":
                view_feedback()
            else:
                print("Incorrect password!")
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == '__main__':
    main()

