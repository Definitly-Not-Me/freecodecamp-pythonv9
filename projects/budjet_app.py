from itertools import zip_longest
""" 
Build a Budget App

In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

    You should have a Category class that accepts a name as the argument.

    The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.

    The Category class should have the following methods:
        A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
        A withdraw method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
        A get_balance method that returns the current category balance based on ledger.
        A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
        A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.

    When a Category object is printed, it should:
        Display a title line of 30 characters with the category name centered between * characters.
        List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
        Show a final line Total: [balance], where [balance] should be replaced by the category total.

    Here is an example usage:

    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)

    And here is an example of the output:

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96

    You should have a function outside the Category class named create_spend_chart(categories) that returns a bar-chart string. To build the chart:
        Start with the title Percentage spent by category.
        Calculate percentages from withdrawals only and not from deposits. The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
        Label the y-axis from 100 down to 0 in steps of 10.
        Use o characters for the bars.
        Include a horizontal line two spaces past the last bar.
        Write category names vertically below the bar.

    This function will be tested with up to four categories.

    Make sure to match the spacing of the example output exactly:

    Percentage spent by category
    100|          
     90|          
     80|          
     70|          
     60| o        
     50| o        
     40| o        
     30| o        
     20| o  o     
     10| o  o  o  
      0| o  o  o  
        ----------
         F  C  A  
         o  l  u  
         o  o  t  
         d  t  o  
            h     
            i     
            n     
            g     

NOTE: open the browser console with F12 to see a more verbose output of the tests.
Tests:

    Waiting: 1. The deposit method should create a specific object in the ledger instance variable.
    Waiting: 2. Calling the deposit method with no description should create a blank description.
    Waiting: 3. The withdraw method should create a specific object in the ledger instance variable.
    Waiting: 4. Calling the withdraw method with no description should create a blank description.
    Waiting: 5. The withdraw method should return True if the withdrawal took place.
    Waiting: 6. Calling food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') should return a balance of 854.33.
    Waiting: 7. Calling the transfer method on a category object should create a specific ledger item in that category object.
    Waiting: 8. The transfer method should return True if the transfer took place.
    Waiting: 9. Calling transfer on a category object should reduce the balance in the category object.
    Waiting: 10. The transfer method should increase the balance of the category object passed as its argument.
    Waiting: 11. The transfer method should create a specific ledger item in the category object passed as its argument.
    Waiting: 12. The check_funds method should return False if the amount passed to the method is greater than the category balance.
    Waiting: 13. The check_funds method should return True if the amount passed to the method is not greater than the category balance.
    Waiting: 14. The withdraw method should return False if the withdrawal didn't take place.
    Waiting: 15. The transfer method should return False if the transfer didn't take place.
    Waiting: 16. Printing a Category instance should give a different string representation of the object.
    Waiting: 17. Title at the top of create_spend_chart chart should say Percentage spent by category.
    Waiting: 18. create_spend_chart chart should have correct percentages down the left side.
    Waiting: 19. The height of each bar on the create_spend_chart chart should be rounded down to the nearest 10.
    Waiting: 20. Each line in create_spend_chart chart should have the same length. Bars for different categories should be separated by two spaces, with additional two spaces after the final bar.
    Waiting: 21. create_spend_chart should correctly show horizontal line below the bars. Using three - characters for each category, and in total going two characters past the final bar.
    Waiting: 22. create_spend_chart chart should not have new line character at the end.
    Waiting: 23. create_spend_chart chart should have each category name written vertically below the bar. Each line should have the same length, each category should be separated by two spaces, with additional two spaces after the final category.
    Waiting: 24. create_spend_chart should print a different chart representation. Check that all spacing is exact. Open your browser console with F12 for more details.


"""

class Category:
    """
    You should have a Category class that accepts a name as the argument.

    The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.
        
    """
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount :int, description: str = "")-> None:
        """
        A deposit method that accepts an amount and an optional description. 
        If no description is given, it should default to an empty string.
        The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
        """
        self.ledger.append({"amount": amount, "description": description})
        print(f"{amount} $ was deposited into your account !")

    def check_funds(self, amount) -> bool:
        """
        A check_funds method that accepts an amount and 
        returns False if it exceeds the balance or True otherwise. 
        This method must be used by both the withdraw and transfer methods.
        """
        total = self.get_balance()
        return amount <= total

    def withdraw(self, amount: int, description: str = "") -> bool:
        """
        A withdraw method that accepts an amount and an optional description (default to an empty string). 
        The method should store in ledger the amount passed in as a negative number, 
        and should return True if the withdrawal

        """
        is_valid :bool = self.check_funds(amount)
        if is_valid:
            print(f"The amount {amount}$ was retired from your Balance : {self.get_balance()} ")
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            print("Insufisant funds...\n Nice Try peasant >:)")
            return False

    def get_balance(self)-> int:
        """
        A get_balance method that returns the current category balance based on ledger.

        """
        Total: float = sum([dict["amount"] for dict in self.ledger ])

        return Total


    def transfer(self, amount: int, destination: object) -> bool:
        """
        A transfer method that accepts an amount and another Category instance, 
        withdraws the amount with description Transfer to [Destination], 
        deposits it into the other category with description Transfer from [Source], 
        where [Destination] and [Source] should be replaced by the name of destination and source categories. 
        The method should return True when the transfer is successful, and False otherwise.

        """
        succeeded = self.withdraw(amount, description = f"Transfer to {destination.name}")
        if succeeded:
            destination.deposit(amount, description = f"Transfer from {self.name}")
            print(f"{amount} was transfered from {self.name} to {destination.name} succesfully !")
            print(f"Actual Balance: {self.get_balance()}") 
            return True
        else:
            print(f"Your transaction failed ! Please check your balance")
            return False
        
    def __str__(self)-> str:
        """
            When a Category object is printed, it should:
            Display a title line of 30 characters with the category name centered 
            between * characters.
            List each ledger entry with up to 23 characters of its description left-aligned
            and the amount right-aligned (two decimal places, max 7 characters).
            Show a final line Total: [balance], where [balance] should be replaced by the category total.
        """
        res = self.name.center(30, "*") + "\n"
     
        for entry in self.ledger:
            res += f"{entry['description']:23.23}{entry['amount']:>7.2f}\n"
        res += f"Total: {self.get_balance():.2f}"
        
        return res


def create_spend_chart(categories: object)->str:
    """
You should have a function outside the Category class named create_spend_chart(categories) that returns a bar-chart string. To build the chart:
        Start with the title Percentage spent by category.
        Calculate percentages from withdrawals only and not from deposits. 
        The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
        Label the y-axis from 100 down to 0 in steps of 10.
        Use o characters for the bars.
        Include a horizontal line two spaces past the last bar.
        Write category names vertically below the bar.
    """
    title = "Percentage spent by category\n"
    spendings = {}
    for instance in categories:
        spendings[instance.name] = abs(sum(entry["amount"] for entry in instance.ledger if entry["amount"] < 0))
        print(f"spendings + {instance.name }'s spendings = {spendings}")
    total = sum(spendings.values())
    

    #Pourcentages
    if total != 0:   
        spendings = {k:(v/total)*100//10*10 for k,v in spendings.items()}


    #graph
    lignes =[]
    for i in range(100, -1, -10):
        row = "".join(["o  " if spendings[category]>= i else "   " for category in spendings ])
        lignes.append(f"{str(i).rjust(3)}| {row}")
    graph = title + "\n".join(lignes) + "\n"
    graph += "    "+ "-"*(3*len(spendings)) + "-\n"

    for letter in zip_longest(*spendings.keys(), fillvalue = " "):
        graph += "    "+ "  ".join(letter) + " \n"
        

    return graph.rstrip('\n')
        
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food) 
print(create_spend_chart([food,clothing]))    

