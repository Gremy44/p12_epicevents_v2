import click
import os

class Print_hello:
    
    def __init__(self):
        pass

    def print_hello(self):
        self.cls()
        print('--- LOGIN ---')
        a = input('username : ')
        b = input('password : ')
        
    @staticmethod
    def cls():
        """
        - Clean console
        """
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    coucou = Print_hello()
    coucou.print_hello()
