from random import randint


class Gladiator:
    """ Information about gladiators """

    # created a init function so that it will create a gladiator
    def __init__(self, name, health, rage, damage_low, damage_high):
        """ (Gladiator, str, int, int, int, int) -> NoneType

        Creates a new Gladiator

        >>> gladiator = Gladiator('Josh', 100, 15, 10, 20)
        >>> gladiator.name 
        'Josh'
        >>> gladiator.health 
        100
        >>> gladiator.rage
        15
        >>> gladiator.damage_high
        20
        >>> gladiator.damage_low
        10
        """
        self.name = name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    # Created a __str__ function so that it will show the user the gladiators information
    def __str__(self):
        """ (Gladiator) -> str

        Return the information about the gladiators

        >>> gladiator = Gladiator('Josh', 100, 15, 10, 20)
        >>> str(gladiator)
        'Josh: 100 HP ||| 15 Rage ||| Low damage: 10 ||| High damage: 20'
        """
        return '{0}: {1} HP ||| {2} Rage ||| Low damage: {3} ||| High damage: {4}'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    # This function adds 30 to the rage since the gladiator pass
    def pass_rage(self):
        """(Gladiator) -> Nonetype
         
        updates the rage function if gladiator pass
        """
        self.rage += 30

    # This function is to attack the other gladiator
    def attack(self, other):
        """(Gladiator, other) -> NoneType

        Updates the gladiator after one of the gladiators attack
        """

        damage_dealt = randint(self.damage_low, self.damage_high)
        if randint(1, 100) <= self.rage:
            other.health -= (2 * damage_dealt)
            self.rage = 0
        else:
            other.health -= damage_dealt
            self.rage += 15

    # this function is to heal if the user want their gladiator to heal
    def heal(self):
        """(Gladiator) -> NoneType
        
        Updates the gladiators health when the user wants their gladiator to heal
        """
        if self.rage >= 10:
            self.rage = max(self.rage - 10, 0)
            self.health = min(self.health + 5, 200)

    #this function checks if the gladiator is dead
    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    #this function is to use a super punch
    def punch(self, other):
        """ (Gladiator, other) -> None

        Updates the gladiator after the super punch occurs
        """
        super_punch = self.damage_high
        other.health -= super_punch * 2
        self.health -= self.health * .5
        self.rage = 0

    #this function give the user the ability to super heal
    def super_heal(self):
        """(Gladiator) -> None

        Updates the gladiator if the user want to use the super heal
        """
        if self.health <= 100 and self.rage >= 30:
            self.health += 20
            self.rage = 0
            return True
        return False

    #this function is to take health away from aponent and adds it to your gladiator
    def healer(self, other):
        """(Gladiator, other) -> None

        takes health way from oponent and adds it to the gladiators health

        """
        if self.rage >= 40:
            other.health -= 15
            self.health += 15
            self.rage = 0

    #this function is to attack the oponent twice
    def barbarian(self, other):
        """(Gladiator, other) -> None
        the gladiator will attack the oponent twice
        """
        if self.rage >= 40:
            self.attack(other)
            self.attack(other)
            self.rage = 0

    #this function is if the user chooses the sword it will hit the oponent really hard
    def sword(self, other):
        """(Gladiator, other) -> None
        the gladiator will use the sword on the oponent and take 40 point from their health
        """
        if self.rage >= 50:
            other.health -= 40
            self.rage = 0

    def lance(self, other):
        """ (Gladiator, other) -> None
        The gladiator will use the lance on the oponent and take 35 point from their health
        """
        if self.rage >= 45:
            other.health -= 35
            self.rage = 0

    def bow_and_arrow(self, other):
        """(Gladiator, other) -> None
        The gladiator will use the lance on the oponent and take 30 points from their health
        """
        if self.rage >= 40:
            other.health -= 30
            self.rage = 0

    def knife(self, other):
        """(Gladiator, other) -> None
        The gladiator will use the lance on the oponent and take 25 points from their health
        """
        if self.rage >= 35:
            other.health -= 25
            self.rage = 0
