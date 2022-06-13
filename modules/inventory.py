import csv
import os.path

#Create inventory class with attributes and object method - to use for methods in blockbuster class
class Inventory:
    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = int(id)
        self.title = str(title)
        self.rating = str(rating)
        self.release_year = int(release_year)
        self.copies_available = int(copies_available)

    @classmethod
    def objects(cls):
        movies = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, '../data/inventory.csv')

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append(Inventory(**dict(row)))

        return movies 

