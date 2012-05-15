# Geese are waterfowl belonging to the tribe Anserini of the family Anatidae. 
# This tribe comprises the genera Anser (the grey geese), Branta (the black geese) and Chen (the white geese). 
# A number of other birds, mostly related to the shelducks, have "goose" as part of their name. 
# More distantly related members of the Anatidae family are swans, 
#      most of which are larger than true geese, and ducks, which are smaller.

# They are strong swimmers with medium to large bodies. 
# They have historically been an important food source, and 
#      continue to be hunted as game, or raised as poultry for meat and eggs. 
# The domestic duck is sometimes kept as a pet.

from copy import deepcopy

class Goose(object):

    def move(self):
        self.swim()

    # 1. (12) swim -- (travel through water; "We had to swim for 20 minutes to reach the shore"; "a big fish was swimming in the tank")
    def swim(self):
        # nothing to swim in yet
        raise NotImplementedException()

    # 1. (2) pet -- (a domesticated animal kept for companionship or amusement)
    def act_like_pet(self):
        self.act_amusing()

    def act_amusing(self):
        self.make_sound()

    def make_sound(self):
        print "Honk!"

    #  1. (29) food, nutrient -- (any substance that can be metabolized by an animal to give energy and build tissue)
    def act_like_food(self):
        old_self = deepcopy(self)
        return self.extract_nutrients(old_self)

    def extract_nutrients(self):
        # Where do you find the nutrients on a goose?
        raise NotImplementedException()
        

