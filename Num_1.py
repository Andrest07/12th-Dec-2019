#initial dictionary.
inventory = { 'gold' : 500, 'pouch' : ['flint', 'twine', 'gemstone'], 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'] }

#adding pocket and its values.
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#sorting backpack
inventory['backpack'].sort()

#searching for dagger and deleting it
for i in range(len(inventory['backpack'])-1):
    if inventory['backpack'][i] == "dagger":
        del inventory['backpack'][i]

#adding gold
inventory['gold'] = inventory['gold'] + 50
print(inventory)

