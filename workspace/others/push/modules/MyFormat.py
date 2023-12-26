import os
import glob
 

class MyFormat:
    
    def space(path):
        with open(path, 'r', encoding="utf-8") as file:
            contents = file.read()


        while '  ' in contents:
            contents = contents.replace('  ', ' ')
             

        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(path, 'w', encoding="utf-8") as file:
            file.write(contents)
    
    def latex_contents(path):
        with open(path, 'r', encoding="utf-8") as file:
            contents = file.read()

        contents = contents.replace('\n', '\n\n\n\n\n')

        while '  ' in contents:
            contents = contents.replace('  ', ' ')
            
        while '( ' in contents:
            contents = contents.replace('( ', '(')
        while ' )' in contents:
            contents = contents.replace(' )', ')')
        while '[ ' in contents:
            contents = contents.replace('[ ', '[')
        while ' ]' in contents:
            contents = contents.replace(' ]', ']')
        while '{ ' in contents:
            contents = contents.replace('{ ', '{')
        while ' }' in contents:
            contents = contents.replace(' }', '}')

        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(path, 'w', encoding="utf-8") as file:
            file.write(contents)
    
    def latex_main(path):
        with open(path, 'r', encoding="utf-8") as file:
            contents = file.read()


        while '  ' in contents:
            contents = contents.replace('  ', ' ')
            
        while '( ' in contents:
            contents = contents.replace('( ', '(')
        while ' )' in contents:
            contents = contents.replace(' )', ')')
        while '[ ' in contents:
            contents = contents.replace('[ ', '[')
        while ' ]' in contents:
            contents = contents.replace(' ]', ']')
        while '{ ' in contents:
            contents = contents.replace('{ ', '{')
        while ' }' in contents:
            contents = contents.replace(' }', '}')

        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(path, 'w', encoding="utf-8") as file:
            file.write(contents)