""" This is a simple password generator. The geberated password is minimun 8 character long and contains at least 
2 capital letters, at least 2 small letters,  at least two digits, and at least two special characters."""

import random


def password_generator(n_characters):
    # Generates password - min 2 small letters, 2 capital letters, 2 digits, 
    # and 2 special characters
    
    password = []
    
    # ASCII 97-122
    password.append(chr(random.randint(97, 123)))
    password.append(chr(random.randint(97, 123)))
    # ASCII 65-90
    password.append(chr(random.randint(65, 91)))
    password.append(chr(random.randint(65, 91)))
    # ASCII 30-39
    password.append(chr(random.randint(48, 58)))
    password.append(chr(random.randint(48, 58)))
    # dict for special charatcres
    # generate a key, but use char(value)
    special_values = list(range(32, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))
    special_keys = list(range(len(special_values)))
    tuples = [(key, value) for i, (key, value) in enumerate(zip(special_keys, special_values))]
    special_dict = dict(tuples)
    password.append(chr(special_dict[random.randint(0, len(special_values))]))
    password.append(chr(special_dict[random.randint(0, len(special_values))]))

    if n_characters > 8:
        temp = random.sample(range(32, 127), n_characters - 8)
        for elem in temp:
            password.append(chr(elem))
  
    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    # my_n_characters = int(input('Number of characters: '))
    my_n_characters = 20
    my_password = password_generator(my_n_characters)
    print(my_password)
    
