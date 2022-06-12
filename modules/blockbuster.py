from modules.customers import Customer
from modules.inventory import Inventory
import csv
import os

class Blockbuster:
    def __init__(self, name):
        self.name = name
        self.customers = Customer.objects()
        self.inventory = Inventory.objects()

    def view_inventory(self):
        print()
        for i, movie in enumerate(self.inventory):
            print(f'{movie.id} {movie.title} Rated: {movie.rating} Released: {movie.release_year} In-Stock: {movie.copies_available}')

    def view_customer_rentals(self):
        cust_id = int(input('\nEnter customer ID: '))
        
        for i, customer in enumerate(self.customers):
            if cust_id == customer.id:
                if customer.current_video_rentals != '':
                    print(f'\n{customer.first_name} {customer.last_name} Rentals: ')
                    for j in customer.current_video_rentals.split('/'):
                        print(j)
                if customer.current_video_rentals == '':
                    print(f'\n{customer.first_name} {customer.last_name} Has No Rentals At The Moment')

    def list_customers(self):
        print()
        for i, customer in enumerate(self.customers):
            print(f'{customer.id}. {customer.first_name} {customer.last_name}')

    def add_customer(self):
        customer_data = {}
        customer_data['first_name'] = input("Enter first name: ")
        customer_data['last_name'] = input("Enter last name: ")
        customer_data['account_type'] = input("Enter account type (sx, px, sf, pf): ")
        customer_data['id'] = input("Enter unique id: ") 
        
        new_customer = Customer(**customer_data)
        self.customers.append(new_customer)

    def rent_video(self):
        movie_title = str(input('\nEnter Movie Title: '))
        for i, movie in enumerate(self.inventory):
            if movie_title == movie.title and movie.copies_available == 0:
                print("\nOut of Stock")
                return
        
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
        
    
       
            

    
