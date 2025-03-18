import json
import requests


pokemon1 = input("Bienvenido a tu buscador de pokemones. Ingresa el nombre de un pokemon: ")
response1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon1}")

pokemon2 = input("Ingresa otro pokemon: ")
response2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon2}")

# Convertir a JSON
data_pokemon1 = response1.json()
data_pokemon2 = response2.json()

print(f"Su pokemon 1 elejido es  {data_pokemon1['name']}. Su tipo es: ")

for type_poke in data_pokemon1['types']:
    print(f"⋆.˚ {type_poke['type']['name']}")

print("Sus habilidades son: ")
for ability_poke in data_pokemon1['abilities']:
    print(f"➢ {ability_poke['ability']['name']}")


print("Sus estadisticas son: ")
for stats_poke in data_pokemon1['stats']:
    print(f"🔥 {stats_poke['stat']['name']}: {stats_poke['base_stat']}")

attack1 = next(stat["base_stat"] for stat in data_pokemon1["stats"] if stat["stat"]["name"] == "attack")


print(f"Su pokemon 2 elejido es  {data_pokemon2['name']}. Su tipo es: ")

for type_poke in data_pokemon2['types']:
    print(f"⋆.˚ {type_poke['type']['name']}")

print("Sus habilidades son: ")
for ability_poke in data_pokemon2['abilities']:
    print(f"➢ {ability_poke['ability']['name']}")


print("Sus estadisticas son: ")
for stats_poke in data_pokemon2['stats']:
    print(f"🔥 {stats_poke['stat']['name']}: {stats_poke['base_stat']}")
attack2 = next(stat["base_stat"] for stat in data_pokemon1["stats"] if stat["stat"]["name"] == "attack")


if attack2 > attack1:
    print(f"El pokemon {pokemon2} es mas fuerte que {pokemon1}")

else:
    print(f"El pokemon {pokemon1} es mas fuerte que {pokemon2}")