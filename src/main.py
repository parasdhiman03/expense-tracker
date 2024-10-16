from expense_tracker import ExpenseTracker
from ui import display_menu

def main():
    tracker = ExpenseTracker()
    while True:
        choice = display_menu()
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.view_category_summary()
        elif choice == '4':
            tracker.view_monthly_summary()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
