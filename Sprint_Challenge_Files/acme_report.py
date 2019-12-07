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

        inventory.append(prod)
        return inventory


def inventory_report(inventory):
    from statistics import mean

    n_unique = len(set([x.name for x in inventory]))
    mean_price = mean([x.price for x in inventory])
    mean_weight = mean([x.weight for x in inventory])
    mean_flammability = mean([x.flammability for x in inventory])



    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {n_unique}')
    print(f'Average price: {mean_price}')
    print(f'Average weight: {mean_weight}')
    print(f'Average_flammability: {mean_flammability}')




if __name__ == '__main__':
    inventory_report(generate_products())
