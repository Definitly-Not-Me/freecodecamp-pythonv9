###Projet 1


    Python Certification
    Build a Budget App

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

### Project 2

    Python Certification
    Build a Polygon Area Calculator

Build a Polygon Area Calculator

In this project, you will use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit its methods and attributes.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

    You should create a Rectangle class.

    When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:
        set_width: Sets the width of the rectangle.
        set_height: Sets the height of the rectangle.
        get_area: Returns area (width×height).
        get_perimeter: Returns perimeter 2(width+height).
        get_diagonal: Returns diagonal √width2+height2.
        get_picture: Returns a string that represents the shape using lines of *. The number of lines should be equal to the height and the number of * in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: Too big for picture..
        get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

    If an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10).

    You should create a Square class that subclasses Rectangle.

    When a Square object is created, it should be initialized with a single side length. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

    The Square class should contain the following methods:
        set_width: Overrides the set_width method from the Rectangle class. It should set the width and height to the side length.
        set_height: Overrides the set_height method from the Rectangle class. It should set the width and height to the side length.
        set_side: Sets the height and width of the square equal to the side length.

    The Square class should be able to access the Rectangle class methods.

    If an instance of a Square is represented as a string, it should look like: Square(side=9).

Usage example

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

That code should return:

50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8

Tests:

    Waiting: 1. You should have a Rectangle class.
    Waiting: 2. You should have a Square class.
    Waiting: 3. The Square class should be a subclass of the Rectangle class.
    Waiting: 4. The Square class should be a distinct class from the Rectangle class.
    Waiting: 5. A square object should be an instance of the Square class and the Rectangle class.
    Waiting: 6. The string representation of Rectangle(3, 6) should be Rectangle(width=3, height=6).
    Waiting: 7. The string representation of Square(5) should be Square(side=5).
    Waiting: 8. Rectangle(3, 6).get_area() should return 18.
    Waiting: 9. Square(5).get_area() should return 25.
    Waiting: 10. Rectangle(3, 6).get_perimeter() should return 18.
    Waiting: 11. Square(5).get_perimeter() should return 20.
    Waiting: 12. Rectangle(3, 6).get_diagonal() should return 6.708203932499369.
    Waiting: 13. Square(5).get_diagonal() should return 7.0710678118654755.
    Waiting: 14. An instance of the Rectangle class should have a different string representation after setting new values.
    Waiting: 15. An instance of the Square class should have a different string representation after setting new values by using .set_side().
    Waiting: 16. An instance of the Square class should have a different string representation after setting new values by using .set_width() or set_height().
    Waiting: 17. The .get_picture() method should return a different string representation of a Rectangle instance.
    Waiting: 18. The .get_picture() method should return a different string representation of a Square instance.
    Waiting: 19. The .get_picture() method should return the string Too big for picture. if the width or height attributes are larger than 50.
    Waiting: 20. Rectangle(15,10).get_amount_inside(Square(5)) should return 6.
    Waiting: 21. Rectangle(4,8).get_amount_inside(Rectangle(3, 6)) should return 1.
    Waiting: 22. Rectangle(2,3).get_amount_inside(Rectangle(3, 6)) should return 0.

                              
### Project 3

    Python Certification
    Build a Hash Table

Build a Hash Table

In this lab, you will build a hash table from scratch. A hash table is a data structure that stores key-value pairs. A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.

For the purpose of this lab, the hashing function will be simple: it will sum the Unicode values of each character in the key. The hash value will then be used as the actual key to store the associated value. The same hash value would also be used to retrieve and delete the value associated with the key.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

    You should define a class named HashTable with a collection attribute initialized to an empty dictionary when a new instance of HashTable is created. The collection dictionary should store key-value pairs based on the hashed value of the key.

    The HashTable class should have four instance methods: hash, add, remove, and lookup.

    The hash method should:
        Take a string as a parameter.
        Return a hashed value computed as the sum of the Unicode (ASCII) values of each character in the string. You can use the ord function for this computation.

    The add method should:
        Take two arguments representing a key-value pair, and compute the hash of the key.
        Use the computed hash value as a key to store a dictionary containing the key-value pair inside the collection dictionary.
        If multiple keys produce the same hash value, their key-value pairs should be stored in the existing nested dictionary under the same hash value.

    The remove method should:
        Take a key as its argument and compute its hash.
        Confirm if the key exists in the collection.
        Remove the corresponding key-value pair from the hash table.
        If the key does not exist in the collection, it should not raise an error or remove anything.

    The lookup method should:
        Take a key as its argument.
        Compute the hash of the key, and return the corresponding value stored inside the hash table.
        If the key does not exist in the collection, it should return None.

Tests:

    Waiting: 1. You should define a HashTable class.
    Waiting: 2. When a new instance of the HashTable class is created, its collection attribute should be initialized to an empty dictionary.
    Waiting: 3. The HashTable class should have a hash method.
    Waiting: 4. The hash method should take a string as a parameter.
    Waiting: 5. The hash method should take a string as its argument and return the sum of the Unicode values of each character in the string.
    Waiting: 6. The HashTable class should have an add method.
    Waiting: 7. The add method should take a key and value as parameters.
    Waiting: 8. The HashTable class should have a remove method.
    Waiting: 9. The remove method should take a key as a parameter.
    Waiting: 10. When you try to remove a key that does not exist in the collection, it should not raise an error or remove anything.
    Waiting: 11. If multiple keys hash to the same index, the remove method should only delete the specific key-value pair and not the entire dictionary at that index.
    Waiting: 12. The HashTable class should have a lookup method.
    Waiting: 13. The lookup method should take a key as the parameter.
    Waiting: 14. HashTable().hash('golf') should return 424.
    Waiting: 15. HashTable().add('golf', 'sport') should add the key-value pair to the collection at key 424.
    Waiting: 16. HashTable().add('dear', 'friend') and HashTable().add('read', 'book') should add both the key-value pairs to the collection at index 412 as a nested dictionary.
    Waiting: 17. When a key exists in the hash table, the remove() method should remove the given key and its corresponding value from the collection.
    Waiting: 18. When the 'golf', 'sport' key-value pair exists in the hash table, HashTable().lookup('golf') should return sport.
    Waiting: 19. When the 'golf', 'sport' key-value pair does not exist in the collection, HashTable().lookup('golf') should return None.
    Waiting: 20. When the 'fcc' key exists in the collection, HashTable().lookup('cfc') should return None.
    Waiting: 21. When you add ('rose', 'flower') to the hash table, its collection attribute should look like this: { 441: { 'rose': 'flower' }}.
    Waiting: 22. When you add a key that hashes to the same value as an existing key, like fcc and cfc, the collection should look like this: { 300: { 'fcc': 'coding', 'cfc':  'chemical' }}.



