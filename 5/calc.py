import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

def get_map(lines, key):
    start = False
    map = []
    for line in lines:
        if start:
            if line == '\n':
                break
            map.append([int(i) for i in line.split(' ')])
        if key in line:
            start = True
    return map
    
def my_map(maps, val):
    for map in maps:
        if map[1] <= val < map[1]+map[2]:
            return map[0] + (val-map[1])
    return val



seeds = lines[0].split(': ')[1]
seeds = [int(i) for i in seeds.split(' ')]
arr = np.array(seeds)
arr = arr.reshape((-1,2))


# seeder = []
# for ranger in arr:
#     print('first')
#     seeder.extend(np.arange(ranger[0], ranger[0]+ranger[1]))

# print('seeds are ready')

# seeds = seeder

seed_to_soil_map = get_map(lines, 'seed-to-soil')
soil_to_fertilizer_map = get_map(lines, 'soil-to-fertilizer')
fertilizer_to_water_map = get_map(lines, 'fertilizer-to-water')
water_to_light_map = get_map(lines, 'water-to-light')
light_to_temperature_map = get_map(lines, 'light-to-temperature')
temperature_to_humidity_map = get_map(lines, 'temperature-to-humidity')
humidity_to_location_map = get_map(lines, 'humidity-to-location')



min_loc = 1e9
min_seed = -1

for ranger in arr:
    seeds = np.arange(ranger[0], ranger[0]+ranger[1])
    print('first')
    for index, seed in enumerate(seeds):
        print(len(seeds), ' -- ', index)
        soil = my_map(seed_to_soil_map, seed)
        fertilizer = my_map(soil_to_fertilizer_map, soil)
        water = my_map(fertilizer_to_water_map, fertilizer)
        light = my_map(water_to_light_map, water)
        temp = my_map(light_to_temperature_map, light)
        humindity = my_map(temperature_to_humidity_map, temp)
        location = my_map(humidity_to_location_map, humindity)
        if location < min_loc:
            min_loc = location
            min_seed = seed

print(min_loc)
print(min_seed)


