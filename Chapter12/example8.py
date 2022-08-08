import threading
import time
from typing import Type


class Spouse(threading.Thread):
    def __init__(self, name, partner):
        threading.Thread.__init__(self)
        self.name = name
        self.partner: 'Spouse' = partner
        self.hungry = True

    def run(self):
        while self.hungry:
            print("{0} is hungry and wants to eat".format(self.name))

            if self.partner.hungry:
                print("{0} is waiting for their partner to eat first...".format(self.name))
            else:
                with fork:
                    print("{0} has started eating.".format(self.name))
                    time.sleep(5)

                    print("{0} is now full".format(self.name))
                    self.hungry = False


fork = threading.Lock()

partner1 = Spouse('Wife', None)
partner2 = Spouse('Husband', partner1)
partner1.partner = partner2

partner1.start()
partner2.start()

partner1.join()
partner2.join()

print("Finished.")