dictionary = {
    'name' : 'Asier',
    'surname' : 'Marin',
    'age' : '18'
}

print(dictionary['name'])
print(dictionary.get('name', 'default'))

print(dictionary.items())

dictionary.update({

    # Add key subjects
    'subjects' : {
        'Sistemas Embebidos',
        'Sistemas Inteligentes'
    },

    # Update de key name
    'name' : 'Max Verstapen'
})

print(dictionary['name'])
print(dictionary.items())