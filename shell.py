import core


def intro_gladiator(gladiator_1, gladiator_2):
    print('Our first Gladiator is:\n\n \t' + str(gladiator_1) +
          '!\n\nOur second Gladiator is:\n\n \t' + str(gladiator_2) + '!\n\n')


def Gladiator_one():
    return input('\tGladiator One. type in your name: ')


def Gladiator_two():
    return input('\tGladiator two. type in your name: ')


def gladiator_choice(n):
    s = '''\nGladiator {}... What would you like to do?\n
    \t-1. attack\n
    \t-2. pass\n
    \t-3. quit\n
    \t-4. heal\n
    \t-5. super heal\n
    \t-6. power punch\n
    \t-7. helper (only if rage is greater than 40)\n
    \t-8. Weapons\n 
    '''.format(n)
    return input(s)


def gladiator_1_and_2_choice(a, b, c, d, e):
    if a == '1' or a.lower() == 'one':
        b.attack(c)
        if c.is_dead():
            print('Gladiator ' + d + '!! WINS!!!')
            exit()
    elif a == '2' or a.lower() == 'two':
        b.pass_rage()
        print('Gladiator ' + d + '. passes.\n')
    elif a == '3' or a.lower() == 'three':
        print('Gladiator ' + e + '! WINS!! by default.')
        exit()
    elif a == '4' or a.lower() == 'four':
        b.heal()
    elif a == '5' or a.lower() == 'five':
        if b.super_heal():
            print('Gladiator ' + d + '. You have succesfully super heal.\n')
        else:
            print(
                'Sorry you do not have enough rage. You need 30 or more rage')
    elif a == '6' or a.lower() == 'six':
        b.punch(c)
        if c.is_dead():
            print('Gladiator ' + d + '!! WINS!!!')
            exit()
    elif a == '7' or a.lower() == 'seven':
        helper(b, c)
        if c.is_dead():
            print('Gladiator ' + d + '!! WINS!!!')
            exit()
    elif a == '8' or a.lower() == 'eight':
        weapon_inventory(b, c)
        if c.is_dead():
            print('Gladiator ' + d + '!! WINS!!!')
            exit()


def helper(b, c):
    choice = input('''Which helper would you like to choose to help you? 
    -1. Barbarian (Does Double attack on your oponent)
    -2. Healer (takes health away from your oponent and adds it to yours\n''')
    if choice == '1' or choice.lower() == 'one':
        b.barbarian(c)
    elif choice == '2' or choice.lower() == 'two':
        b.healer(c)


def weapon_inventory(b, c):
    choice = input(''' Which weapon would you like to use?
    \t-1. sword (need to have 50 percent of rage)\n
    \t-2. lance (need to have 45 percent of rage)\n
    \t-3. bow and arrows ( need to have 40 percent of rage)\n
    \t-4. knife (need to have 35 percent of rage\n''')
    if choice == '1' or choice.lower() == 'one':
        b.sword(c)
    elif choice == '2' or choice.lower() == 'two':
        b.lance(c)
    elif choice == '3' or choice.lower() == 'three':
        b.bow_and_arrow(c)
    elif choice == '4' or choice.lower() == 'four':
        b.knife(c)


def main():
    print("""              .-.
              | |____________________________________________________
 _ _ _ _ _ _ _| |                                                  .'`.
|_|_|_|_|_|_|_| | WELCOME TO GLADIATORS WAR!!--------------------.'****>
`.            | |_______________________________________________.'***.'
  `.        .'| |                                               `**'
    `-.___.'  `-' WHERE ONLY ONE GETS TO WALK AWAY ALIVE!!!    .'*`.
                                                               `._.' .
                                                               .   .'*`.
                                                             .'*`. `._.'\n
        Gladiator 1 has a low damage: 12 and high damage: 20\n
        Gladiator 2 has a low damage: 5 and high damage: 30\n\n
        CHOOSE WISELY!!\n
                            ,--.                       ,--.
                          _',|| )                     ( \\ |
            ,.,,.,-----""' "--v-.___                   `_\\.'--,..__
            |,"---.--''/       /,.__"")`-:|._________-"'     (--..__'/--.
                      /     ,."'    ""-'-"|'  _.,-"_.'-"\     \     ` '""
                   _ )____---------------(|--"_|--'      '__   \_
                _,' |  .''''""---.        '""'       ,---'''.   /".
            _,-'  ." \/,,..---/_ /                   | -|.._____|  \_
          ,-\,.'''            \ (                    |"")       "-,  \_
      _ .".--"                ( :                    | (           '. "\_
    ,- ,."                    ; !                    ; |             \,_ `.
___(_(."       ctr -------....L_">        _________.-/_J                '\_')
                                                     """
          "            ---------- "
          "")
    name = Gladiator_one()
    name_2 = Gladiator_two()
    gladiator_1 = core.Gladiator(name, 200, 0, 12, 20)
    gladiator_2 = core.Gladiator(name_2, 200, 0, 5, 30)
    intro_gladiator(gladiator_1, gladiator_2)
    while True:
        choice = gladiator_choice(name)
        gladiator_1_and_2_choice(choice, gladiator_1, gladiator_2, name,
                                 name_2)
        print(str(gladiator_1))
        print(str(gladiator_2))
        choice = gladiator_choice(name_2)
        gladiator_1_and_2_choice(choice, gladiator_2, gladiator_1, name_2,
                                 name)
        print(str(gladiator_1))
        print(str(gladiator_2))


if __name__ == '__main__':
    main()