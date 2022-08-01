# Author: Fransiskus Agapa

#########################################################################
# main class has names that are shared among the shapes
# subclasses that are inherited from main class have access to main class
# subclasses can use the variable names that are created in main class
#########################################################################

class SharedName:                              # main / parent class

    def __init__(self, base, height, radius):
        self.base = base
        self.height = height
        self.radius = radius


class Prism(SharedName):  # sub / child class

    def __init__(self, base, height, radius):
        super().__init__(base, height, radius)  # since it's defined in main class - it won't need to be defined again

    def volume(self):
        return self.base * self.height


class Sphere(SharedName):                       # sub / child class

    def __init__(self, base, height, radius, pi_val):
        super().__init__(base, height, radius)
        self.pi_val = pi_val

    def volume(self):
        return (4 / 3) * self.pi_val * self.radius * self.radius * self.radius


class Pyramid(SharedName):                     # sub / child class

    def __init__(self, base, height, radius):
        super().__init__(base, height, radius)

    def volume(self):
        return (1 / 3) * self.base * self.height


class RightCircularCone(SharedName):           # sub / child class

    def __init__(self, base, height, radius, pi_val):
        super().__init__(base, height, radius)
        self.pi_val = pi_val

    def volume(self):
        return (1 / 3) * self.pi_val * self.radius * self.radius * self.height


class Square(SharedName):

    def __init__(self, base, height, radius, length, width):
        super().__init__(base, height, radius)
        self.length = length
        self.width = width

    def volume(self):
        return (1 / 3) * self.length * self.width * self.height


print("\n== Volume of Shape ==")
print("1. Prism")
print("2. Sphere")
print("3. Pyramid")
print("4. Right Circular Cone")
print("5. Square")
print("e. Exit")
choice = input("choice: ").lower()              # make user input to lower case - easier to put while-loop condition

place_holder = 0                                # not all shapes will use the shared name in main class, this is used to hold position of unused variable name
pi_value = 3.1428                               # some shapes need pi value to computer its volume

while choice != 'e':
    if choice == '1':
        print("\n[ Prism ]\n")
        try:                                    # just in case user input is not digit
            print("Input the base: ", end=" ")  # end=" " - is used to put prompt and user input in one line
            p_base = int(input())
            print("Input the height: ", end=" ")
            p_height = int(input())
            prism = Prism(p_base, p_height, place_holder)
            print("\n[ The volume of prism: " + str(prism.volume()) + " ]")
        except ValueError:
            print("\n[ invalid input - Digit only ]")

    elif choice == '2':
        print("\n[ Sphere ]\n")
        try:
            print("Input the radius (half of diameter): ", end=" ")
            s_rad = int(input())
            sphere = Sphere(place_holder, place_holder, s_rad, pi_value)
            print("\n[ The volume of sphere: " + str(sphere.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    elif choice == '3':
        print("\n[ Pyramid ]\n")
        try:                                     # WHAT IF YOU PUT IMAGE HERE ?
            print("Input the base: ", end=" ")
            py_base = int(input())
            print("Input the height: ", end=" ")
            py_height = int(input())
            pyramid = Pyramid(py_base, py_height, place_holder)
            print("\n[ The volume of pyramid: " + str(pyramid.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    elif choice == '4':
        print("\n[ Right Circular Cone ]\n")
        try:
            print("Input the radius (half of diameter): ", end=" ")
            rcc_radius = int(input())
            print("Input the height: ", end=" ")
            rcc_height = int(input())
            right_circular_cone = RightCircularCone(place_holder, rcc_height, rcc_radius, pi_value)
            print("\n[ The volume of right circular cone: " + str(right_circular_cone.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    elif choice == '5':
        print("\n[ Square ]\n")
        try:
            print("Input the length: ", end=" ")
            s_len = int(input())
            print("Input the width: ", end=" ")
            s_wid = int(input())
            print("input the height: ", end=" ")
            s_height = int(input())
            square = Square(place_holder, s_height, place_holder, s_len, s_wid)
            print("\n[ The volume of square: " + str(square.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Volume of Shape ==")
    print("1. Prism")
    print("2. Sphere")
    print("3. Pyramid")
    print("4. Right Circular Cone")
    print("5. Square")
    print("e. Exit")
    choice = input("choice: ").lower()           # make user input to lower case - easier to put while-loop condition

print("\n== Exit Program ==")
