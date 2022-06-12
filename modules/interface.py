from modules.blockbuster import Blockbuster

blockbuster = Blockbuster('The last Blockbuster')

def interface():
    while True:
        print('\n---------Blockbuster-1.0--------')
        print('1. View Inventory              |')
        print('2. View Customer Rented Videos |')
        print('3. View All Customers          |')
        print('4. Add New Customer            |')
        print('5. Rent Video                  |')
        print('6. Return Video                |')
        print('0. Exit                        |')
        print('--------------------------------\n')
        
        option = int(input('Please Enter Option: '))

        if option == 1:
            blockbuster.view_inventory()
        
        elif option == 2:
            blockbuster.list_customers()
            blockbuster.view_customer_rentals()
        
        elif option == 3:
            blockbuster.list_customers()

        elif option == 4:
            blockbuster.add_customer()
            
        elif option == 5:
            blockbuster.view_inventory()
            blockbuster.rent_video()
        
        elif option == 6:
            blockbuster.view_inventory()
            blockbuster.return_video()

        elif option == 0:
            exit()

        else:
            print('\nInvalid input')
        
        interface()
