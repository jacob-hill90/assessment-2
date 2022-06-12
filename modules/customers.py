import csv
import os.path

class Customer:
    def __init__(self, id, account_type, first_name, last_name, current_video_rentals = ''):
        self.id = int(id)
        self.account_type = str(account_type)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.current_video_rentals = str(current_video_rentals)

    @classmethod
    def objects(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, '../data/customers.csv')

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customer(**dict(row)))
        
        return customers 
