class PersonalFinanceManager:
    def __init__(self):
        self.income = 0.0
        self.expenses = []
        self.savings = 0.0
    
    def add_income(self, amount):
        self.income += amount
    
    def add_expense(self, category, amount):
        self.expenses.append((category, amount))
    
    def calculate_savings(self):
        total_expenses = sum(amount for category, amount in self.expenses)
        self.savings = self.income - total_expenses
    
    def show_summary(self):
        print(f"Income: ${self.income:.2f}")
        print("Expenses:")
        for category, amount in self.expenses:
            print(f"  {category}: ${amount:.2f}")
        print(f"Savings: ${self.savings:.2f}")

def main():
    finance_manager = PersonalFinanceManager()
    
    while True:
        print("\n=== Personal Finance Manager ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Savings")
        print("4. Show Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            finance_manager.add_income(amount)
            print(f"Income of ${amount:.2f} added successfully.")
        
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            finance_manager.add_expense(category, amount)
            print(f"Expense of ${amount:.2f} under '{category}' added successfully.")
        
        elif choice == '3':
            finance_manager.calculate_savings()
            print("Savings calculated.")
        
        elif choice == '4':
            finance_manager.show_summary()
        
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
