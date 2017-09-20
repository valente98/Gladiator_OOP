import core


def test_to_see_if_Gladiator_is_a_type():
    assert isinstance(core.Gladiator, type)


def test_Gladiator_init_is_implemented():
    gladiator = core.Gladiator('Josh', 1, 2, 3, 4)
    assert gladiator.name == 'Josh'
    assert gladiator.health == 1
    assert gladiator.rage == 2
    assert gladiator.damage_low == 3
    assert gladiator.damage_high == 4


def test_Gladiator_str_is_implemented():
    gladiator = core.Gladiator('Josh', 1, 2, 3, 4)
    assert str(
        gladiator
    ) == 'Josh: 1 HP ||| 2 Rage ||| Low damage: 3 ||| High damage: 4'


def test_pass_rage():
    gladiator = core.Gladiator('Josh', 1, 2, 3, 4)
    assert gladiator.pass_rage() == None
    assert gladiator.rage == 32


def test_attack():
    gladiator_1 = core.Gladiator('Josh', 100, 0, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 70, 0, 10, 10)
    assert gladiator_1.attack(gladiator_2) == None
    assert gladiator_1.rage == 15
    assert gladiator_2.health == 60
    gladiator_1 = core.Gladiator('Josh', 100, 100, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 70, 100, 10, 10)
    assert gladiator_1.attack(gladiator_2) == None
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 50


def test_heal():
    gladiator_1 = core.Gladiator('Josh', 85, 20, 10, 10)
    assert gladiator_1.heal() == None
    assert gladiator_1.rage == 10
    assert gladiator_1.health == 90


def test_is_dead():
    gladiator_1 = core.Gladiator('Josh', 85, 20, 10, 10)
    assert gladiator_1.is_dead() == False
    gladiator_1 = core.Gladiator('Josh', 0, 20, 10, 10)
    assert gladiator_1.is_dead() == True


def test_punch():
    gladiator_1 = core.Gladiator('Josh', 100, 20, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 25, 20, 10, 10)
    assert gladiator_1.punch(gladiator_2) == None
    assert gladiator_1.rage == 0
    assert gladiator_1.health == 50
    assert gladiator_2.health == 5


def test_super_heal():
    gladiator_1 = core.Gladiator('Tom', 25, 40, 10, 10)
    assert gladiator_1.super_heal() == True
    assert gladiator_1.health == 45
    assert gladiator_1.rage == 0
    gladiator_1 = core.Gladiator('Tom', 25, 20, 10, 10)
    assert gladiator_1.super_heal() == False


def test_barbarian():
    gladiator_1 = core.Gladiator('Tom', 25, 45, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 45, 45, 10, 10)
    assert gladiator_1.barbarian(gladiator_1) == None
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 45


def test_healer():
    gladiator_1 = core.Gladiator('Tom', 25, 45, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 45, 45, 10, 10)
    assert gladiator_1.healer(gladiator_2) == None
    assert gladiator_1.health == 40
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 30


def test_sword():
    gladiator_1 = core.Gladiator('Tom', 25, 50, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 45, 45, 10, 10)
    assert gladiator_1.sword(gladiator_2) == None
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 5


def test_lance():
    gladiator_1 = core.Gladiator('Tom', 25, 45, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 45, 45, 10, 10)
    assert gladiator_1.lance(gladiator_2) == None
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 10


def test_bow_and_arrow():
    gladiator_1 = core.Gladiator('Tom', 25, 45, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 45, 45, 10, 10)
    assert gladiator_1.bow_and_arrow(gladiator_2) == None
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 15


def test_knife():
    gladiator_1 = core.Gladiator('Tom', 25, 45, 10, 10)
    gladiator_2 = core.Gladiator('Tom', 45, 45, 10, 10)
    assert gladiator_1.knife(gladiator_2) == None
    assert gladiator_1.rage == 0
    assert gladiator_2.health == 20