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
    print(f'Average flammability: {mean_flammability}')
    
    
if __name__ == '__main__':
    inventory_report(generate_products())
        
        