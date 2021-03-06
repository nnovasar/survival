'''
environments
tundra, space, rainforest
desert, grassland, jungle, ocean, rainforest, space, tundra
'''

INSTANT_DEATH = -100
DEATH = -50
POOR = -20
NEUTRAL = 0
FAIR = 20
EXCEPTIONAL = 50

ENVIRONMENTS = ['desert', 'grassland', 'jungle', 'ocean', 'forest', 'tundra', 'arctic']

SKIN = {'fur': {'arctic': EXCEPTIONAL, 'desert': NEUTRAL, 'grassland': NEUTRAL, 'jungle': NEUTRAL, 'ocean': NEUTRAL, 'forest': NEUTRAL,'tundra':EXCEPTIONAL},
        'feathers': {'arctic': FAIR,'desert':NEUTRAL, 'grassland': NEUTRAL, 'jungle': NEUTRAL , 'ocean': NEUTRAL, 'forest': NEUTRAL,'tundra': NEUTRAL},
        'dry skin': {'arctic': DEATH,'desert': POOR, 'grassland':FAIR, 'jungle':POOR, 'ocean':POOR, 'forest':POOR,'tundra':DEATH},
        'amphibious': {'arctic': DEATH,'desert':DEATH, 'grassland':DEATH, 'jungle': EXCEPTIONAL, 'ocean': FAIR, 'forest': POOR,'tundra':DEATH},
        'dry scales': {'arctic':DEATH,'desert': EXCEPTIONAL, 'grassland':FAIR, 'jungle':FAIR, 'ocean': DEATH, 'forest': POOR,'tundra':DEATH},
        'wet scales': {'arctic':DEATH,'desert': DEATH, 'grassland':DEATH, 'jungle':FAIR, 'ocean': EXCEPTIONAL, 'forest':POOR,'tundra': DEATH}
              }


DIET = {'carnivore':{'arctic':FAIR,'desert':NEUTRAL, 'grassland':NEUTRAL, 'jungle':FAIR, 'ocean':NEUTRAL, 'forest':NEUTRAL,'tundra':NEUTRAL},
        'herbivore':{'arctic':POOR,'desert':NEUTRAL, 'grassland':FAIR, 'jungle':FAIR, 'ocean':NEUTRAL, 'forest':FAIR,'tundra':NEUTRAL},
        'omnivore':{'arctic':FAIR,'desert': NEUTRAL, 'grassland':FAIR, 'jungle':FAIR, 'ocean':NEUTRAL, 'forest':EXCEPTIONAL,'tundra':NEUTRAL}
        }


MOVE = {'running': {'arctic': FAIR,'desert': FAIR, 'grassland': EXCEPTIONAL, 'jungle': NEUTRAL, 'ocean': DEATH, 'forest': EXCEPTIONAL,'tundra': FAIR},
        'jumping':{'arctic': NEUTRAL,'desert': FAIR, 'grassland': EXCEPTIONAL, 'jungle': EXCEPTIONAL, 'ocean': DEATH, 'forest': POOR,'tundra': POOR},
        'climbing':{'arctic': DEATH,'desert': DEATH, 'grassland': DEATH, 'jungle': EXCEPTIONAL, 'ocean': DEATH, 'forest': FAIR,'tundra': DEATH},
        'flying':{'arctic': NEUTRAL,'desert': FAIR, 'grassland': FAIR, 'jungle': EXCEPTIONAL, 'ocean': NEUTRAL, 'forest': EXCEPTIONAL,'tundra': NEUTRAL},
        'swimming':{'arctic': DEATH,'desert': DEATH , 'grassland': DEATH, 'jungle': NEUTRAL, 'ocean': EXCEPTIONAL, 'forest': DEATH,'tundra':DEATH}
        }

BREATH = {'lungs':{'arctic':NEUTRAL,'desert':NEUTRAL , 'grassland':NEUTRAL, 'jungle':NEUTRAL, 'ocean': DEATH, 'forest':NEUTRAL,'tundra':NEUTRAL},
          'external gills':{'arctic': DEATH,'desert': DEATH, 'grassland':DEATH, 'jungle':EXCEPTIONAL, 'ocean':FAIR, 'forest':DEATH,'tundra':DEATH}, #amphibian
          'internal gills':{'arctic':DEATH,'desert':DEATH, 'grassland':DEATH, 'jungle':DEATH, 'ocean':EXCEPTIONAL, 'forest':DEATH,'tundra':DEATH}, #fish/aquatic
          'tracheae': {'arctic': NEUTRAL,'desert':NEUTRAL, 'grassland':NEUTRAL, 'jungle':NEUTRAL, 'ocean': DEATH, 'forest':NEUTRAL,'tundra':NEUTRAL} #bugs
          }

COLOR = {'black':{'arctic': POOR,'desert':NEUTRAL,'grassland':NEUTRAL,'jungle':NEUTRAL,'ocean':NEUTRAL,'forest':NEUTRAL,'tundra':POOR},
         'brown': {'arctic':POOR,'desert':FAIR,'grassland':FAIR,'jungle':FAIR,'ocean':NEUTRAL,'forest':FAIR,'tundra':FAIR},
         'white': {'arctic': EXCEPTIONAL,'desert':POOR,'grassland':POOR,'jungle':POOR,'ocean':POOR,'forest':POOR,'tundra':EXCEPTIONAL},
         'colorful': {'arctic':DEATH,'desert':POOR,'grassland':POOR,'jungle':NEUTRAL,'ocean':NEUTRAL,'forest':POOR,'tundra':DEATH},
         'stripes': {'arctic':POOR,'desert':FAIR,'grassland':NEUTRAL,'jungle':FAIR,'ocean':FAIR,'forest':NEUTRAL,'tundra':NEUTRAL},
        }

