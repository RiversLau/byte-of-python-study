class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Initializing {})'.format(self.name))

        Robot.population += 1

    def die(self):
        print('{} is being destroyed.'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} is the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working.'.format(Robot.population))

    def say_hi(self):
        print('Greetings, my master call me {}'.format(self.name))

    @classmethod
    def how_many(cls):
        print('We have {:d} robots.'.format(Robot.population))


droid = Robot('Tommy')
droid.say_hi()
Robot.how_many()

droid1 = Robot('Patty')
droid1.say_hi()
Robot.how_many()

print('\nRobots are do some work.')
print("\nRobots have finished their work, let's destroy them")

droid.die()
droid1.die()
Robot.how_many()