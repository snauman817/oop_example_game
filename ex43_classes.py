prompt = '> '

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        self.scene_map.opening_scene()


class Death(Scene):

    def enter(self):
        print("You have died. Better luck next time.")

class CentralCorridor(Scene):

    def enter(self):
        print("You are in the central corridor of this space ship.")
        print("A Gothon stands before you!")

        choice = input(prompt)

        if 'joke' in choice:
            print("The Gothon laughs uncontrollably, allowing you to pass")
            self.finish()
        else:
            print("The Gothon does not find you funny and kills you.")
            Death().enter()

    def finish(self):
        print(" ")
        print("-" * 10)
        print(" ")
        print("You can go to the following rooms:")
        print("\t1. Laser Weapon Armory")

        choose = input(prompt)

        print(" ")
        print("-" * 10)
        print(" ")

        if choose == "1":
            LaserWeaponArmory().enter()

class LaserWeaponArmory(Scene):

    def enter(self):
        print("You find yourself in an armory, and there is a big bomb in a vault.")
        print("You plan on blowing up the ship before leaving, but you need the keycode to get in.")

        choice = input(prompt)

        if choice == "1234":
            print("The doors open. Wait, was it really that easy!?")
            print("You take the bomb before heading back, over the still laughing Gothon, and make your way to the bridge.")

            print(" ")
            print("-" * 10)
            print(" ")

            TheBridge().enter()
        else:
            print("That wasn't the right password. Try again.")

            print(" ")
            print("-" * 10)
            print(" ")

            LaserWeaponArmory().enter()


class TheBridge(Scene):
    
    def enter(self):
        print("You arrive at the bridge, on the way to the escape pod, and a Gothon stands in your way.")
        print("He looks ready to charge.")

        choice = input(prompt)

        if "bomb" in choice:
            print("You plant the bomb as the Gothon charges you. You duck right under his legs and are able to run past, bomb planted.")

            print(" ")
            print("-" * 10)
            print(" ")

            EscapePod().enter()
        else:
            print("The Gothon charges into you with so much force that the bomb explodes in your hands.")
            Death().enter()

class EscapePod(Scene):

    def enter(self):
        print("You are greeted with the Escape Pod room, only to find out that there are a bunch of escape pods.")
        print("Your choices are:")
        print("\tA Pinstriped Escape Pod")
        print("\tA worn out, old-looking Escape Pod")
        print("\tA highlighter-yellow Escape Pod")

        choice = input()

        if "pinstripe" in choice:
            print("This escape pod, even though it looks clean, actually malfunctions as you're about to take off.")
            Death().enter()
        elif "old" in choice or "worn" in choice:
            print("You hop in the old escape pod, and exit the space ship. As the pod ejects, though, the outer shell begins breaking apart, and you die out in space.")
            Death().enter()
        else:
            print("You hop in the yellow escape pod and take off. You watch as the space station explodes behind you.")
            print("Congratulations! You won!")

class Map(object):

    def __init__(self, start_scene, other_scenes):
        self.start_scene = start_scene
        self.other_scenes = other_scenes

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        self.start_scene.enter()

central_corridor = CentralCorridor()
death = Death()
central_corridor = CentralCorridor()
armory = LaserWeaponArmory()
bridge = TheBridge()
pod = EscapePod()

a_map = Map(central_corridor, {'central_corridor' : central_corridor, 'armory' : armory, 'bridge' : bridge, 'pod' : pod, 'death' : death})
a_game = Engine(a_map)
a_game.play()

