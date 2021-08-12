from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"


    def release_pokemon(self, pokemon_name: str):
        for pokemon_obj in self.pokemon:
            if pokemon_obj.name == pokemon_name:
                self.pokemon.remove(pokemon_obj)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"


    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\n"f"Pokemon count {len(self.pokemon)}\n"
        for pok_obj in self.pokemon:
            res += f"- {pok_obj.pokemon_details()}\n"
        return res


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
