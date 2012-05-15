# aarbon@cns_unit451:~# /usr/local/WordNet-FINAL/bin/wn koi
# No information available for noun koi
# No information available for verb koi
# No information available for adj koi
# No information available for adv koi

# aarbon@cns_unit451:~# wget https://en.wikipedia.org/wiki/Koi
# --0001-05-14 14:53:12--  https://en.wikipedia.org/wiki/Koi
# Resolving en.wikipedia.org... 208.80.154.225
# Connecting to en.wikipedia.org|208.80.154.225|:443... connected.
# HTTP request sent, awaiting response... 200 OK
# Length: 95953 (94K) [text/html]
# Saving to: `Koi'
# 100%[======================================>] 95,953       527K/s   in 0.2s  # 0001-05-14 14:53:13 (527 KB/s) - `Koi' saved [95953/95953]

# aarbon@cns_unit451:~# cat Koi | python striphtml.py | python extract_meaning.py
# warning: unsupported character set, language redaction enabled

# Koi (REDACTED, Japanese:REDACTED]) or more specifically nishikigoi (REDACTED, literally "brocaded carp"), are ornamental varieties of domesticated common carp (Cyprinus carpio) that are kept for decorative purposes in outdoor koi ponds or water gardens.
# Koi varieties are distinguished by coloration, patterning, and scalation. Some of the major colors are white, black, red, yellow, blue, and cream. 


class Koi(object):

    def ___init__(self,color,pattern,scalation):
        self.color = color
        self.pattern = pattern
        self.scalation = scalation

    def swim(self):
        # still nothing to swim in yet,
        # WHO THE FUCKING HELL IS RESPONSIBLE FOR IMPLEMENTING WATER?!
        #    WITHOUT IT THIS THING IS MORE USELESS THAN THE GOOSE.....
        raise NotImplementedException()

    def look_decorative(self,garden):
        # DO I HAVE TO DO EVERYTHING MY FUCKING SELF AROUND HERE?!

        class WaterGarden():
            
            def __init(self):
                self.things_inside_me = []

            # this thing doesn't even exist in /wn 
            # There isn't even a 
            # aarbon@cns_unit451:~# /usr/local/WordNet-FINAL/bin/wn word 
            #        => language unit, linguistic unit
            #   for this 'thing' in the database, so why use 
            #   a real verb for what it does...
            def ornamentationism(self, thing):
                self.things_inside_me.append(thing)
                
        
        wg = WaterGarden(); wg.ornamentationism(garden);
        return wg;

