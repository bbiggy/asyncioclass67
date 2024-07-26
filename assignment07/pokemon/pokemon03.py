import aiofiles
import asyncio
import json

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode = 'r') as f:
        contents = await f.read()

        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move ['move']['name'] for move in pokemon['moves']]

        print(f"Pokémon: {pokemon}")
        print(f"Moves: {moves}")

        async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode = 'w') as f:
            await f.write('\n'.join(moves))

asyncio.run(main())