class Item:
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return f"Weight: {self.weight} units"


class UniversalCharger(Item):
    def __init__(self, color, price, size, brand, weight):
        super().__init__(weight)
        self.color = color
        self.price = price
        self.size = size
        self.brand = brand
    
    def __str__(self):
        return f"Universal Charger - Color: {self.color}, Price: {self.price}, Size: {self.size}, Brand: {self.brand}, {super().__str__()}"


class Passport(Item):
    def __init__(self, color, cost, boughtFrom, weight):
        super().__init__(weight)
        self.color = color
        self.cost = cost
        self.boughtFrom = boughtFrom

    def __str__(self):
        return f"Passport - Color: {self.color}, Cost: {self.cost}, Bought From: {self.boughtFrom}, {super().__str__()}"
    
    
class Sunglasses(Item):
    def __init__(self, have_case, color, origin, weight):
        super().__init__(weight)
        self.have_case = have_case
        self.color = color
        self.origin = origin
    
    def __str__(self):
        return f"Sunglasses - Have Case: {self.have_case}, Color: {self.color}, Origin: {self.origin}, {super().__str__()}"
    
    
class Sneakers(Item):
    def __init__(self, brand, is_new, bought_from, weight):
        super().__init__(weight)
        self.brand = brand
        self.is_new = is_new
        self.bought_from = bought_from
    
    def __str__(self):
        return f"Sneakers - Brand: {self.brand}, New: {self.is_new}, Bought From: {self.bought_from}, {super().__str__()}"

class Smartphone(Item):
    def __init__(self, brand, os, storage, display, camera, materials, weight):
        super().__init__(weight)
        self.brand = brand
        self.os = os
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials
    
    def __str__(self):
        return f"Smartphone - Brand: {self.brand}, OS: {self.os}, Storage: {self.storage}, Display: {self.display}, Camera: {self.camera}, Materials: {', '.join(self.materials)}, {super().__str__()}"

class Laptop(Item):
    def __init__(self, brand, model, processor, storage, ram, weight):
        super().__init__(weight)
        self.brand = brand
        self.model = model
        self.processor = processor
        self.storage = storage
        self.ram = ram
    
    def __str__(self):
        return f"Laptop - Brand: {self.brand}, Model: {self.model}, Processor: {self.processor}, Storage: {self.storage}, RAM: {self.ram}, {super().__str__()}"


class Smartwatch(Item):
    def __init__(self, brand, model, color, features, weight):
        super().__init__(weight)
        self.brand = brand
        self.model = model
        self.color = color
        self.features = features
    
    def __str__(self):
        return f"Smartwatch - Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Features: {self.features}, {super().__str__()}"


class Campus(Item):
    def __init__(self, name, location, courses, students, weight):
        super().__init__(weight)
        self.name = name
        self.location = location
        self.courses = courses
        self.students = students
    
    def __str__(self):
        return f"Campus - Name: {self.name}, Location: {self.location}, Courses: {', '.join(self.courses)}, Students: {self.students}, {super().__str__()}"


def get_class(category):
    class_dict = {
        'charger': UniversalCharger,
        'passport': Passport,
        'sunglasses': Sunglasses,
        'sneakers': Sneakers,
        'smartphone': Smartphone,
        'laptop': Laptop,
        'smartwatch': Smartwatch,
        'campus': Campus
    }
    return class_dict.get(category.lower(), None)

def get_category(item):
    class_to_category = {
        UniversalCharger: 'Charger',
        Passport: 'Passport',
        Sunglasses: 'Sunglasses',
        Sneakers: 'Sneakers',
        Smartphone: 'Smartphone',
        Laptop: 'Laptop',
        Smartwatch: 'Smartwatch',
        Campus: 'Campus'
    }
    for class_type, category in class_to_category.items():
        if isinstance(item, class_type):
            return category
    return "Unknown Category"


class Bag:
    def __init__(self):
        self.items = []
        self.total_weight = 0

    def add_item(self, item):
        if len(self.items) < 6 and self.total_weight + item.weight <= 80:
            self.items.append(item)
            self.total_weight += item.weight
            print("Item added successfully.")
        else:
            print("Cannot add item to the bag due to weight/item limits.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_weight -= item.weight
            print("Item removed successfully.")
        else:
            print("Item not found in the bag.")

    def print_all_items(self):
        i = 0
        for item in self.items:
            print(f"{i + 1}.{item}")
            i+=1

# CLI Item Entry
print("Welcome to the Bag Packing Game!")
bag = Bag()

while True:
    choice = input("1-add an item\n"
                   "2-print all items\n"
                   "3-print items from category\n"
                   "4-print all items by category\n"
                   "5-remove an item\n"
                   "q-quit\n"
                   "Enter your choice: \n")

    if choice == '1':
        
        item_type = input("Enter item type: ")
        if item_type == 'charger':
            color = input("Enter color: ")
            price = int(input("Enter price: "))
            size = input("Enter size: ")
            brand = input("Enter brand: ")
            weight = int(input("Enter weight: "))
            charger = UniversalCharger(color, price, size, brand, weight)
            bag.add_item(charger)
            
        elif item_type == 'passport':
            color = input("Enter color: ")
            cost = int(input("Enter cost: "))
            bought_from = input("Enter bought from: ")
            weight = int(input("Enter weight: "))
            passport = Passport(color, cost, bought_from, weight)
            bag.add_item(passport)
            
        elif item_type == 'sunglasses':
            have_case = input("Does it have a case? (yes/no): ")
            color = input("Enter color: ")
            origin = input("Enter origin: ")
            weight = int(input("Enter weight: "))
            sunglasses = Sunglasses(have_case, color, origin, weight)
            bag.add_item(sunglasses)
            
        elif item_type == 'sneakers':
            brand = input("Enter brand: ")
            is_new = input("Is it new? (true/false): ").lower() == 'true'
            bought_from = input("Bought from: ")
            weight = int(input("Enter weight: "))
            sneakers = Sneakers(brand, is_new, bought_from, weight)
            bag.add_item(sneakers)
            
        elif item_type == 'smartphone':
            brand = input("Enter Brand: ")
            os = input("Enter Operating System: ")
            storage = input("Enter Storage: ")
            display = input("Enter Display type: ")
            camera = input("Enter Camera type: ")
            materials = input("Enter materials (separated by comma): ").split(', ')
            weight = int(input("Enter weight: "))
            smartphone = Smartphone(brand, os, storage, display, camera, materials, weight)
            bag.add_item(smartphone)
            
        elif item_type == 'laptop':
            brand = input("Enter Brand: ")
            processor = input("Enter Processor: ")
            ram = input("Enter RAM: ")
            storage = input("Enter Storage: ")
            graphics = input("Enter Graphics: ")
            weight = int(input("Enter weight: "))
            laptop = Laptop(brand, processor, ram, storage, graphics, weight)
            bag.add_item(laptop)
            
        elif item_type == 'smartwatch':
            brand = input("Enter Brand: ")
            display = input("Enter Display: ")
            battery_life = input("Enter Battery Life: ")
            fitness_features = input("Enter Fitness Features: ")
            connectivity = input("Enter Connectivity: ")
            weight = int(input("Enter weight: "))
            smartwatch = Smartwatch(brand, display, battery_life, fitness_features, connectivity, weight)
            bag.add_item(smartwatch)
            
        elif item_type == 'campus':
            brand = input("Enter Brand: ")
            accuracy = input("Enter Accuracy: ")
            price = int(input("Enter Price: "))
            materials = input("Enter Materials (separated by comma): ").split(', ')
            weight = int(input("Enter weight: "))
            campus = Campus(brand, accuracy, price, materials, weight)
            bag.add_item(campus)

        else:
            print("Invalid item type!")

    elif choice == '2':
        print("Printing all items in the bag:")
        bag.print_all_items()
        
            
            
    elif choice == '3':
        category = input("Enter the category to print items from: ")
        
        filtered_items = [item for item in bag.items if isinstance(item, get_class(category))]
        
        if filtered_items:
            for i, item in enumerate(filtered_items):
                print(f"{i + 1}. {item}")
        else:
            print("No items found in the specified category.")
    

   
    elif choice == '4':
        category_dict = {}

        for item in bag.items:
            category = get_category(item)
            if category in category_dict:
                category_dict[category].append(item)
            else:
                category_dict[category] = [item]
    
        for category, items in category_dict.items():
            print(f"Category: {category}")
            for i, item in enumerate(items):
                print(f"{i + 1}. {item}")
            print("\n")
        
    elif choice == '5':
        bag.print_all_items()
        item_index = int(input("Enter the index of the item to remove: "))
        if item_index <= len(bag.items):
            bag.remove_item(bag.items[item_index - 1])
        else:
            print("Invalid item index!")
    
    elif choice == 'q':
        print("Exiting the game.")
        break
            
    else:
        print("Invalid choice. Please try again.")
        


        
