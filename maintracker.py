

def main():
    print("hello world")
    #get user expense track
    user_get_expense()
    #save expense file
    save_file_expense()
    #summarize expense
    summarize_expense()
    
def user_get_expense():
    print("getting expense...")
    name = input(" যা কিনেছেন তার নাম লিখুন: ")
    amount = int(input("দাম: "))
    expense_category = [
        "🍔Food",
        "🏥Work",
        "💸Pocket Money",
        "📋Bills or Utilities"
    ]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f"  {i + 1}.{category_name}")

        value_range = f"[1 - {len(expense_category)}]"
        selected_index = input("Enter your choice {value_range}: ")
        break

def save_file_expense():
    print("saving file...")

def summarize_expense():
    print("summarizing...")

if __name__ == "__main__":
    main()
 