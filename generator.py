import string
import itertools

def Main():
    num_of_characters = int(input('Please enter passsword characters : '))

    if num_of_characters < 0:
        print('please enter valid input')

    charaters = list(string.ascii_letters + string.digits + string.punctuation)

    file = open('passwords-length-' + str(num_of_characters) + '.txt','w')
    for passwrod in itertools.permutations(charaters, num_of_characters):
        file.write(''.join(passwrod) + '\n')

    file.close()

if __name__ == '__main__':
    Main()