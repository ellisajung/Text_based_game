import random


class Player:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power

    def attack(self, other, attack_type):
        if attack_type == "normal":
            damage = random.randint(self.power - 2, self.power + 2)
            print(f"{self.name}의 일반 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        elif attack_type == "magic":
            if self.mp >= 5:
                damage = random.randint(self.power - 1, self.power + 5)
                self.mp -= 5
                print(f"{self.name}의 마법 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            else:
                print("마나가 부족합니다. 일반 공격을 사용합니다.")
                damage = random.randint(self.power - 2, self.power + 2)
                print(f"{self.name}의 일반 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        else:
            print("잘못된 공격 타입입니다.")
            damage = 0
        other.hp = max(other.hp - damage, 0)
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}")


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 3, self.power + 1)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
