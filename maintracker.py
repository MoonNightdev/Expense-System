from expense import Expense


def main():
    #get user expense track
    get_user_expense()
    #save expense file
    save_file_expense()
    #summarize expense
    summarize_expense()
    
def get_user_expense():  # sourcery skip: inline-immediately-returned-variable
    
    # Get the expense details from the user
    name = input("Enter the name of the expense: ")
    
    while True:
        try:
            amount = int(input("Enter the amount of the expense: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
    
    expense_categories = {
        1: "🍔 Food",
        2: "🏥 Work",
        3: "💸 Pocket Money",
        4: "📋 Bills or Utilities"
    }
    
    # Display expense categories to the user
    print("Select a category: ")
    for index, category_name in expense_categories.items():
        print(f"  {index}. {category_name}")
    
    while True:
        selected_index = input("Enter the number corresponding to the category: ")
        try:
            selected_index = int(selected_index)
            if selected_index in expense_categories:
                category = expense_categories[selected_index]
                selected_categories = expense_categories[selected_index]
                new_expense = Expense(
                    name=name, amount=amount, category=category
                    )
                    
                return new_expense
                
            else:
                print("Invalid input. Please enter a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a valid category number.")
    
    return name, amount, category
def save_file_expense():
    print("saving file...")

def summarize_expense():
    print("summarizing...")

if __name__ == "__main__":
    main() 

