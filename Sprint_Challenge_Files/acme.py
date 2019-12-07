<<<<<<< HEAD
"""
ACME Coorporation
"""
=======
"""ACME Coorporation"""
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116

import random
import numpy as np
import pandas as pd


class Product:
<<<<<<< HEAD
    def __init__(prod,name,price = 10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000,9999999)):
=======
    def __init__(prod,name,price = 10, weight=20, flammability=0.5, identifier=random.randint(1000000,9999999)):
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
        prod.name = name
        prod.price = price
        prod.weight = weight
        prod.flammability = flammability
<<<<<<< HEAD
        prod.identifier = identifier
        

    def stealability(Product):
        sl = price/weight
        
class Product(object):
    
    def __init__(self, name, price = 10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = 20
        self.flammability = 0.5
=======
        
        
"""class methods"""
    def stealability(Product):
        sl = price/weight
        
class Product(self):
    
    def __init__(self, name, price = 10, weight=20, flammability=0.5, identifier=random.randint(1000000,9999999))
    self.name = name
    self.price = price
    self.weight = 20
    self.flammability = 0.5
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
    
    def stealability(self):
        sl = self.price / self.weight
        if sl < .5:
            return "Not so stealable..."
        elif sl >= .5 and sl < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"
<<<<<<< HEAD

    def explode(self):
=======
        
        
"""2nd class methods"""

    def explode(Product):
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
        bm = flammability * weight
        
    def explode(self):
        bm = self.flammability * self.weight
        if bm < 10:
            return "...fizzle."
        elif bm >= 10 and bm < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"
        
        
        
<<<<<<< HEAD
"""
subclass
"""

class BoxingGlove(Product):
    def __init__(glove, name, price = 10, weight= 10, flammability=0.5,
                 identifier=random.randint(1000000,9999999)):
        glove.name = name
        glove.price = price
        glove.weight = weight
        glove.flammability = flammability
=======
"""subclass"""

class BoxingGlove(Product):
    def __init__(self, name, price = 10, weight=20, flammability=0.5, identifier=random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
        
    def stealability(self):
        sl = self.price / self.weight
        if sl < .5:
            return "Not so stealable..."
        elif sl >= .5 and sl < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"
        
        
    def explode(self):
        return "...it's a glove."
    
    def punch(self):
        qr = self.weight
        if qr < 5:
            return "That tickles."
        elif qr >= 5 and qr < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
               
        
    
<<<<<<< HEAD
  
=======
    
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
