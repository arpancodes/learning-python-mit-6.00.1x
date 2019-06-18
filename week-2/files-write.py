nameHandler = open('names.txt', 'w')

for i in range(2):
    name = input('Enter Name: ')
    nameHandler.write(name + '\n')

nameHandler.close()
