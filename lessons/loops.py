# FOR LOOPS
# ninjas = ['james', 'sara', 'lucas', 'pattie']

# # for ninja in ninjas:
# #   print(ninja)

# # for ninja in ninjas[1:3]:
# #   print(ninja)

# for ninja in ninjas:
#   if ninja == 'lucas':
#     print(f'{ninja} - black belt')
#     break  #break out of the loop
#   else: 
#     print(ninja)


# --------------------------------------

# WHILE LOOPS
age = 25
num = 0

while num < age:
  if num == 0:
    num += 1
    continue
  if num % 2 == 0:
    print(num)
  if num > 10:
    break
  num += 1