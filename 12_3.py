class UpgradeWeapon:
    def __init__(self, bad_weapon, dull_bent):
        self.bad_weapon = bad_weapon
        self.how_dull_and_bent = dull_bent

    def better_weapon(self):
        self.__upgrade()
        self.how_dull_and_bent = self.how_dull_and_bent + 1

    def __upgrade(self):
        if self.how_dull_and_bent <= 0:
            self.bad_weapon = 'It is an upgraded weapon!'
            print("It is upgraded a bit!")
        else:
            print("This weapon is already in good condition.")


knife = UpgradeWeapon('dull_knife', -3)
knife.better_weapon()
knife.better_weapon()
knife.better_weapon()
knife.better_weapon()
knife.better_weapon()
print(knife.how_dull_and_bent, knife.bad_weapon)
