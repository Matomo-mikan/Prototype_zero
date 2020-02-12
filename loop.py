#!usr/bin/env python

''' Author: Matomo
    Purpose: It asks user's name, and it repeats what's told by input.
      It iterates until the input says "bye" or space.
'''

name = input('what is your name? >')
print('{}, hello'.format(name))
prompt = name + ' > '
while 1:
    answer = input(prompt)
    if answer == 'bye':
        print('bye bye')
        break
    elif not answer:
        print('......')
        break
    print('[{}], I see. '.format(answer))
