from modules.customers import Customer
from modules.inventory import Inventory
import csv
import os

class Blockbuster:
    def __init__(self, name):
        self.name = name
        self.customers = Customer.objects()
        self.inventory = Inventory.objects()

#Option 1 to view stores current inventory
    def view_inventory(self):
        print()
        for i, movie in enumerate(self.inventory):
            print(f'{movie.id} {movie.title} Rated: {movie.rating} Released: {movie.release_year} In-Stock: {movie.copies_available}')

#Option 2 to print customer/id and choose which customers rentals to view
    def view_customer_rentals(self):
        try:
            cust_id = int(input('\nEnter customer ID: '))
            for i, customer in enumerate(self.customers):
                if cust_id == customer.id:
                    if customer.current_video_rentals != '':
                        print(f'\n{customer.first_name} {customer.last_name} Rentals: ')
                        for j in customer.current_video_rentals.split('/'):
                            if j != '':
                                print(j)
                    if customer.current_video_rentals == '':
                        print(f'\n{customer.first_name} {customer.last_name} Has No Rentals At The Moment')
        except:
            print('\nInvalid Input')

# Option 3 to view all current customers and id numbers
    def list_customers(self):
        print()
        for i, customer in enumerate(self.customers):
            print(f'{customer.id}. {customer.first_name} {customer.last_name}')

#Option 4 to instantiate new customer
    def add_customer(self):
        customer_data = {}
        customer_data['first_name'] = input("Enter first name: ")
        customer_data['last_name'] = input("Enter last name: ")
        customer_data['account_type'] = input("Enter account type (sx, px, sf, pf): ")
        if customer_data['account_type'] == 'sx' or customer_data['account_type'] == 'px' or customer_data['account_type'] == 'sf' or customer_data['account_type'] == 'pf' :
            customer_data['id'] = int(input("Enter unique id: "))
            for i, customer in enumerate(self.customers):
                if customer_data['id'] == customer.id:
                    print('\nCustomer with ID already exists')
                    return
        else:
            print('\nInvalid Account Type')
            return
        
        new_customer = Customer(**customer_data)
        self.customers.append(new_customer)

#Option 5 to rent video based on account type and availability. Input movie title then customer ID
    def rent_video(self):
        movie_title = str(input('\nEnter Movie Title: '))
        for i, movie in enumerate(self.inventory):
            if movie_title == movie.title and movie.copies_available == 0:
                print("\nOut of Stock")
                return
    
    #If customers account type is 'sx' only one video can be rented at a time
        cust_id = int(input('Enter Customer ID: '))
        for i, customer in enumerate(self.customers):
            if cust_id == customer.id and customer.account_type == 'sx':
                if customer.current_video_rentals != '':
                    print("\nUh Oh, Exceeds Rental Limit For This Customer")
                if customer.current_video_rentals == '':
                    print('\nVideo Rented Sucessfully')
                    customer.current_video_rentals += f'{movie_title}'
                    for i, movie in enumerate(self.inventory):
                        if movie_title == movie.title:
                            movie.copies_available -= 1
    
    #If customers account type is 'px' three videos can be rented at a time 
            if cust_id == customer.id and customer.account_type == 'px':
                if len(customer.current_video_rentals.split('/')) >= 3:
                    print("\nUh Oh, Exceeds Rental Limit For This Customer")
                if len(customer.current_video_rentals.split('/')) < 3:
                    print('\nVideo Rented Sucessfully')
                    if(customer.current_video_rentals) == '':
                        customer.current_video_rentals += f'{movie_title}'
                    else: customer.current_video_rentals += f'/{movie_title}'
                    for i, movie in enumerate(self.inventory):
                        if movie_title == movie.title:
                            movie.copies_available -= 1

    #If a customers account type is 'sf' one video can be rented at a time and no ratings of R
            if cust_id == customer.id and customer.account_type == 'sf':
                if customer.current_video_rentals != '':
                    print("\nUh Oh, Exceeds Rental Limit For This Customer")
                for i, movie in enumerate(self.inventory):
                    if movie_title == movie.title:
                        if movie.rating == 'R':
                            print('\nFamily Account Cannot Rent R Movies')
                            return
                if customer.current_video_rentals == '':
                    print('\nVideo Rented Sucessfully')
                    if(customer.current_video_rentals) == '':
                        customer.current_video_rentals += f'{movie_title}'
                    else: customer.current_video_rentals += f'/{movie_title}'
                    for i, movie in enumerate(self.inventory):
                        if movie_title == movie.title:
                            movie.copies_available -= 1

    #If a customers account type is 'pf' three videos can be rented at a time and no ratings of R
            if cust_id == customer.id and customer.account_type == 'pf':
                if len(customer.current_video_rentals.split('/')) >= 3:
                    print("\nUh Oh, Exceeds Rental Limit For This Customer")
                for i, movie in enumerate(self.inventory):
                    if movie_title == movie.title:
                        if movie.rating == 'R':
                            print('\nFamily Account Cannot Rent R Movies')
                            return
                if len(customer.current_video_rentals.split('/')) < 3:
                    print('\nVideo Rented Sucessfully')
                    if(customer.current_video_rentals) == '':
                        customer.current_video_rentals += f'{movie_title}'
                    else: customer.current_video_rentals += f'/{movie_title}'
                    for i, movie in enumerate(self.inventory):
                        if movie_title == movie.title:
                            movie.copies_available -= 1
        
#Option 6 return video with title and customer ID
    def return_video(self):
        movie_title = str(input('\nEnter Movie Title: '))
        cust_id = int(input('Enter Customer ID: '))
        for i, customer in enumerate(self.customers):
            if cust_id == customer.id:
                if movie_title in customer.current_video_rentals:
                    print('\nVideo Return Successful')
                    if len(customer.current_video_rentals.split('/')) > 1:
                        customer.current_video_rentals = customer.current_video_rentals.replace(f'{movie_title}/', '')
                    if len(customer.current_video_rentals.split('/')) == 1:
                        customer.current_video_rentals = customer.current_video_rentals.replace(movie_title, '')
                    for i, movie in enumerate(self.inventory):
                        if movie_title == movie.title:
                            movie.copies_available += 1
