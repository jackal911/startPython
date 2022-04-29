class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))
        

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]"\
            .format(self.name, location, self.damage))
        
# 마린
class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, 1, 5)
        
    # 스팀팩 : 일정 시간 동안 이동 및 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
            
# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False # 시즈모드 개발여부
    
    def __init__(self):
        super().__init__("탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True        
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))
        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
    
class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)