# ninja_belts = {'crystal': 'red', 'ryu': 'black'}

# # print(ninja_belts['crystal'])  # red

# print(list(ninja_belts.keys()))  # ['crystal', 'ryu']
# print(list(ninja_belts.values()))  # ['red', 'black']

# ninja_belts['yoshi'] = 'red'  # {'crystal': 'red', 'ryu': 'black', 'yoshi': 'red'}

# print(ninja_belts)

# ----------------------------------------------

def belt_count(dictionary):
  belts = list(dictionary.values())
  for belt in set(belts):
    num = belts.count(belt)
    print(f'There are {num} {belt} belts')


# def ninja_intro(dictionary):
#   for key, val in dictionary.items():
#     print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
  ninja_name = input('enter a ninja name: ')
  ninja_belt = input('enter a belt color: ')
  ninja_belts[ninja_name] = ninja_belt

  another = input('add another? (y/n) ')
  if another == 'y':
    continue
  else:
    break

# ninja_intro(ninja_belts)

belt_count(ninja_belts)