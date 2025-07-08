#[in] 511.68 334.0 298
#[out] 티버: 피해량 593.7
# AP * 0.65 + 400
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print(f'티버: 피해량 {ability_power * 0.65 + 400}') 
        
##################################
health, mana, ability_power = map(float, input().split())

x = Annie(health, mana, ability_power)
x.tibbers()
