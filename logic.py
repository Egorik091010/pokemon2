from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(200, 400)
        self.power = randint(30, 60)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"


    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    #Метод для атаки для противника
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            if randint(1, 5) == 3:
                return 'Покемон-волшебник применил щит в сражении'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return (f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n\n"
                    f"Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}")
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}"
    
    

    # Метод класса для получения информации
    def info(self):
        return (f"Имя твоего покеомона: {self.name}\n"
                f"Здоровье покеомона: {self.hp}\n"            
                f"Сила покеомона: {self.power}")

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
class Wizard(Pokemon):
    def attack(self, enemy):
        super_hp = randint(5,15)
        self.hp += super_hp
        result = super().attack(enemy)
        self.hp -= super_hp
        return result + f"\nБоец применил супер-атаку силой:{super_hp} "
    
    def info(self):
        return f"У тебя покемон волшебник"
    pass

class Fighter(Pokemon):
    #Метод атаки 
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "


    def info(self):
        return f"У тебя покемон боец"
    pass
    
