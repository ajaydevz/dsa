my_dict = {
    'apple':10,
    'banana':20,
    'orange':34
}

print(my_dict['apple'])

my_dict['grape'] = 65

print(my_dict)

my_dict['apple'] = 15

print(my_dict)

del my_dict['banana']

print(my_dict)

for k in my_dict:
    print(k)

for v in my_dict.values():
    print(v)

for k,v in my_dict.items():
    print(k,v)


