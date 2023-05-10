from expenses import Expense
import datetime
import calendar

# creating main functions here so that when the file runs- all these functions run as well
def main():
    print(f" 🎯 Running Expense Tracker!")
 
    # creating a variable to store csv file name 
    expense_file_path = "expenses.csv"

    # get an input from the user for their budget in this month
    budget = float(input("Enter your this months budget : "))

    # This function is to - Get user input for expense
    # for that create a function 
    expense = get_user_expense()    # this function will return user expense which he has entered below and this "return" will be stored in "expense" variable


    # This function is to - write their expense to file
    save_expense_to_file(expense, expense_file_path)
    
    # This function is to - Read file and sumarize expenses.
    sumarize_expenses(expense_file_path, budget)



def get_user_expense():
    print(f" 🎯 Getting User expense")
    # get all the necessary inputs from the user
    expense_name = input("Enter expense name - ")
    expense_amount = float(input("Enter expense amount - "))
    print(f"you have entered {expense_name}, {expense_amount}")
    # let user select the category of the expense
    expense_categories = [
        "🍔 Food", "🏠 Home", "💻 Work", "🎭 Fun", "Ⓜ️ Misc"
    ]

    while True:
        # display the categorys available to choose from
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1},  {category_name}")    # +1 is done because list indexing starts from 0
        
        value_range = f"1 - {len(expense_categories)}"       # presenting the value range to choose from 
        
        # store the category in a variable and subtract it from 1 to get the programming index
        selected_index = int(input(f"Enter a category number from range {value_range}: ")) - 1

        # solving a possible test case if the user enters input out of the range
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)    #creating an object called "expense" to store the info

            return new_expense    
        else:
            print("The number entered is invalid please enter a number from the range!")
        break


def save_expense_to_file(expense : Expense, expense_file_path):
    print(f" 🎯 Saving User expense : {expense} to {expense_file_path}")
    with open(expense_file_path, "a", newline='', encoding='utf-8') as f:       # utf-8 is used because open() does not support unicode character encoding. Therefore specifying the utf-8 encoding
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def sumarize_expenses(expense_file_path, budget):
    # get the current date
    now = datetime.datetime.now()

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Now calculate the remaining days 
    remaining_days = days_in_month - now.day

    print("\n")
    print(f" 🎯 Summarizing User expense")
    # creating an empty list "expenses" to store objects created using the "Expense" class.
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()       # reading all the lines in the csv
        for line in lines:
            stripped_line = line.strip()       #removing the white spaces which might be leading and trailing
            expense_name, expense_amount, expense_category = stripped_line.split(",")      # splitting all the variables using split function by using "," and returns a list and stores it in the variables as mentioned above
            line_expenses = Expense(name = expense_name, amount = float(expense_amount), category = expense_category)     
            # print(line_expenses)
            expenses.append(line_expenses)

    # now calculate the total amounts by category        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category   # this "expense" variable created here will a ccess the list "expenses" where all the line by line expense are appended into the list
        # The "expense" object here is from the class "Expense", and we are trying to access the "category" instance of that object. Hence, "expense.category"
        if key in amount_by_category:
            amount_by_category[key] += expense.amount      # we are using the actual "expense" object and not the variable "expense_amount"
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses by Category 📈")
    for key, amount in amount_by_category.items():
        print(f"  {key} : $ {amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent:.2f} this month")
    remaining_budegt = budget - total_spent
    if(remaining_budegt < 0):
        print(red(f"💸 You've exceeded your this month's budget of 💲 {budget:.2f} by: 💲 {total_spent - budget}"))
    else :
        print(green(f"💸 Your remaining budget is 💲{remaining_budegt:.2f}"))
        print(green(f"Remaining days in the current month:  {remaining_days}"))
        
        daily_budget = remaining_budegt / remaining_days
        print(green(f"👉 Budget per day : ${daily_budget:.2f}"))




# Now if I have to make the amounts to stand out and showcase them in colour then I can do that by using this function
def green(text) :
    return f"\033[92m{text}\033[0m"
def red(text) :
    return f"\033[91m{text}\033[0m"

   

if __name__ == "__main__":
    main()