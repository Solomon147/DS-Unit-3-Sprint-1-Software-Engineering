<<<<<<< HEAD
from acme import Product
from random import randint, sample, uniform
import numpy as np
import random 


def generate_products(num=30):
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap','???']
    
    inventory = []
    for i in range(num):
        run_name = (random.choice(ADJECTIVES)+ " " +random.choice(NOUNS))
        run_price = random.randint(5,100)
        run_weight = random.randint(5,100)
        run_flam = random.uniform(0.0,2.5)
        prod = Product(name=run_name, price = run_price, weight = run_weight,
                      flammability = run_flam)
=======
from acme import product
from random import randint, sample, uniform


def generate_products(num = 30):
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    
    
    inventory = []
    for i in range(num):
        run_name = name_1[random.randint(0,len(name_1))] + "" + name_2[random.randint(0,len(name_2))]
        run_price = random.randint(5,100)
        run_weight = random.randint(5,100)
        run_flam = random.randint(0,25)/10
        prod = Product(name=run_name, price=run_price, weight=run_weight,flammability=run_flam)
        
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
        
        inventory.append(prod)
        return inventory
    
<<<<<<< HEAD
    
=======
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
def inventory_report(inventory):
    from statistics import mean
    
    n_unique = len(set([x.name for x in inventory]))
    mean_price = mean([x.price for x in inventory])
    mean_weight = mean([x.weight for x in inventory])
    mean_flammability = mean([x.flammability for x in inventory])
    
<<<<<<< HEAD
    
=======
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {n_unique}')
    print(f'Average price: {mean_price}')
    print(f'Average weight: {mean_weight}')
<<<<<<< HEAD
    print(f'Average_flammability: {mean_flammability}')
    
    
=======
    print(f'Average flammability: {mean_flammability}')
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
    
    
if __name__ == '__main__':
    inventory_report(generate_products())
<<<<<<< HEAD
    
    
            
            
            
  
=======
        
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
        