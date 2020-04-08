import random
import time
import keyboard

rate_of_correction = 90

class Plane:
    def __init__(self, start=10):
        self.start = start

    def turbu(self):
        self.start = random.gauss(0,2*rate_of_correction)
        return self.start


class Corrector:
    def __init__(self):
        self.rate_of_correction = 1

    def correct(self, plane):
        if plane > 0:
            plane -= self.rate_of_correction
            return plane
        elif plane < 0:
            plane += self.rate_of_correction
            return plane
        else:
            pass

Asia = Plane()
Asia.turbu()
corect = Corrector()

print('''Press and hold 's' to stop \n''')

if __name__ == "__main__":
    while True:
        time.sleep(2)
        if keyboard.is_pressed ('s'):
            print ('\n You stopped the program')
            break
        print('Plane angle after turbulence: ',Asia.start)
        print("Applaying corrector")
        after = corect.correct(Asia.start)
        Asia.start = after
        print('Plane angle after correct: ', Asia.start)
        print('\n')
