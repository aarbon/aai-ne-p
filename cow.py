# TODO flesh out object model:
# cattle, cows, kine, oxen, Bos taurus
#        => bovine
#            => bovid
#                => ruminant
#                    => even-toed ungulate, artiodactyl, artiodactyl mammal
#                        => ungulate, hoofed mammal
#                            => placental, placental mammal, eutherian, eutherian mammal
#                                => mammal, mammalian
#                                    => vertebrate, craniate
#                                        => chordate
#                                            => animal, animate being, beast, brute, creature, fauna
#                                                => organism, being
#                                                    => living thing, animate thing
#                                                        => whole, unit
#                                                            => object, physical object
#                                                                => physical entity
#                                                                    => entity


# cow
#  3. A domesticated bovine of either sex or any age.
class Cow(object):
    
    def move(self,direction):
        # dull and slow-moving and stolid;
        MOVEMENT_SPEED = 1;
        # a cow can't go anywhere without a home
        # TODO: write physics model

    def make_sound(self):
        # Sense 1
        # cow, moo-cow
        print "Moo!"

    def eat(self, food):
        # 1. ruminant -- (any of various cud-chewing hoofed mammals having a stomach divided into four (occasionally three) compartments)
        while food is not None:
            self.chew(food)
        
    def chew(self,food):
        # TODO: write physics model
        #     do some chewing
        #     swallow
        # TODO: write biological model
        #     stomach.put(food)
        @ How many ruminations does it take to get to the center of 
        #       a mouthful of grass as a function of it's volume?

        return None
        


#
# # ./wn cow -synsn
# Sense 1
# cow, moo-cow
#       => cattle, cows, kine, oxen, Bos taurus
# # ./wn cattle -synsn
# cattle, cows, kine, oxen, Bos taurus
#       => bovine
# 2. bovine -- (dull and slow-moving and stolid; like an ox; "showed a bovine apathy")
