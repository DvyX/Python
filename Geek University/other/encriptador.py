
e = input()
descripto = []
while True:
    cripto = input()
    j = 0

    if e == '1':
        for i in cripto:
            if i == '1':
                descripto += '0'
            elif i == '2':
                descripto += '9'
            elif i == '3':
                descripto += '8'
            elif i == '4':
                descripto += '7'
            elif i == '5':
                descripto += '6'
            elif i == '6':
                descripto += '5'
            elif i == '7':
                descripto += '4'
            elif i == '8':
                descripto += '3'
            elif i == '9':
                descripto += '2'
            elif i == '0':
                descripto += '1'

            elif i == 'q':
                descripto += 'a'
            elif i == 'w':
                descripto += 'b'
            elif i == 'e':
                descripto += 'c'
            elif i == 'r':
                descripto += 'd'
            elif i == 't':
                descripto += 'e'
            elif i == 'y':
                descripto += 'f'
            elif i == 'u':
                descripto += 'g'
            elif i == 'i':
                descripto += 'h'
            elif i == 'o':
                descripto += 'i'
            elif i == 'p':
                descripto += 'j'
            elif i == 'a':
                descripto += 'k'
            elif i == 's':
                descripto += 'l'
            elif i == 'd':
                descripto += 'm'
            elif i == 'f':
                descripto += 'n'
            elif i == 'g':
                descripto += 'o'
            elif i == 'h':
                descripto += 'p'
            elif i == 'j':
                descripto += 'q'
            elif i == 'k':
                descripto += 'r'
            elif i == 'l':
                descripto += 's'
            elif i == 'ç':
                descripto += 't'
            elif i == 'z':
                descripto += 'u'
            elif i == 'x':
                descripto += 'v'
            elif i == 'c':
                descripto += 'w'
            elif i == 'v':
                descripto += 'x'
            elif i == 'b':
                descripto += 'y'
            elif i == 'n':
                descripto += 'z'
            elif i == 'm':
                descripto += 'ç'

            elif i == 'Q':
                descripto += 'A'
            elif i == 'W':
                descripto += 'B'
            elif i == 'E':
                descripto += 'C'
            elif i == 'R':
                descripto += 'D'
            elif i == 'T':
                descripto += 'E'
            elif i == 'Y':
                descripto += 'F'
            elif i == 'U':
                descripto += 'G'
            elif i == 'I':
                descripto += 'H'
            elif i == 'O':
                descripto += 'I'
            elif i == 'P':
                descripto += 'J'
            elif i == 'A':
                descripto += 'K'
            elif i == 'S':
                descripto += 'L'
            elif i == 'D':
                descripto += 'M'
            elif i == 'F':
                descripto += 'N'
            elif i == 'G':
                descripto += 'O'
            elif i == 'H':
                descripto += 'P'
            elif i == 'J':
                descripto += 'Q'
            elif i == 'K':
                descripto += 'R'
            elif i == 'L':
                descripto += 'S'
            elif i == 'Ç':
                descripto += 'T'
            elif i == 'Z':
                descripto += 'U'
            elif i == 'X':
                descripto += 'V'
            elif i == 'C':
                descripto += 'W'
            elif i == 'V':
                descripto += 'X'
            elif i == 'B':
                descripto += 'Y'
            elif i == 'N':
                descripto += 'Z'
            elif i == 'M':
                descripto += 'Ç'

            elif i == '|':
                descripto += '\\'
            elif i == '/':
                descripto += '|'
            elif i == '\\':
                descripto += '/'
            elif i == '<':
                descripto += '.'
            elif i == '>':
                descripto += ','
            elif i == '.':
                descripto += '>'
            elif i == ',':
                descripto += '<'
            elif i == ')':
                descripto += '!'
            elif i == '(':
                descripto += '@'
            elif i == '*':
                descripto += '#'
            elif i == '&':
                descripto += '$'
            elif i == '¨':
                descripto += '%'
            elif i == '%':
                descripto += '¨'
            elif i == '$':
                descripto += '&'
            elif i == '#':
                descripto += '*'
            elif i == '@':
                descripto += '('
            elif i == '!':
                descripto += ')'
            elif i == '+':
                descripto += '_'
            elif i == '-':
                descripto += '='
            elif i == '=':
                descripto += '+'
            elif i == '_':
                descripto += '-'
            elif i == ']':
                descripto += '{'
            elif i == '[':
                descripto += ']'
            elif i == '{':
                descripto += '}'
            elif i == ']':
                descripto += '['
            elif i == '?':
                descripto += ':'
            elif i == ';':
                descripto += '?'
            elif i == '?':
                descripto += ';'
            elif i == ' ':
                descripto += ' '

            else:
                print(f'   Caractere {cripto[j]} não registrado    ')
            j += 1

    else:
        for i in cripto:
            if i == '1':
                descripto += '0'
            elif i == '2':
                descripto += '9'
            elif i == '3':
                descripto += '8'
            elif i == '4':
                descripto += '7'
            elif i == '5':
                descripto += '6'
            elif i == '6':
                descripto += '5'
            elif i == '7':
                descripto += '4'
            elif i == '8':
                descripto += '3'
            elif i == '9':
                descripto += '2'
            elif i == '0':
                descripto += '1'

            elif i == 'a':
                descripto += 'q'
            elif i == 'b':
                descripto += 'w'
            elif i == 'c':
                descripto += 'e'
            elif i == 'd':
                descripto += 'r'
            elif i == 'e':
                descripto += 't'
            elif i == 'f':
                descripto += 'y'
            elif i == 'g':
                descripto += 'u'
            elif i == 'h':
                descripto += 'i'
            elif i == 'i':
                descripto += 'o'
            elif i == 'j':
                descripto += 'p'
            elif i == 'k':
                descripto += 'a'
            elif i == 'l':
                descripto += 's'
            elif i == 'm':
                descripto += 'd'
            elif i == 'n':
                descripto += 'f'
            elif i == 'o':
                descripto += 'g'
            elif i == 'p':
                descripto += 'h'
            elif i == 'q':
                descripto += 'j'
            elif i == 'r':
                descripto += 'k'
            elif i == 's':
                descripto += 'l'
            elif i == 't':
                descripto += 'ç'
            elif i == 'u':
                descripto += 'z'
            elif i == 'v':
                descripto += 'x'
            elif i == 'w':
                descripto += 'c'
            elif i == 'x':
                descripto += 'v'
            elif i == 'y':
                descripto += 'b'
            elif i == 'z':
                descripto += 'n'
            elif i == 'ç':
                descripto += 'm'

            elif i == 'A':
                descripto += 'Q'
            elif i == 'B':
                descripto += 'W'
            elif i == 'C':
                descripto += 'E'
            elif i == 'D':
                descripto += 'R'
            elif i == 'E':
                descripto += 'T'
            elif i == 'F':
                descripto += 'Y'
            elif i == 'G':
                descripto += 'U'
            elif i == 'H':
                descripto += 'I'
            elif i == 'I':
                descripto += 'O'
            elif i == 'J':
                descripto += 'P'
            elif i == 'K':
                descripto += 'A'
            elif i == 'L':
                descripto += 'S'
            elif i == 'M':
                descripto += 'D'
            elif i == 'N':
                descripto += 'F'
            elif i == 'O':
                descripto += 'G'
            elif i == 'P':
                descripto += 'H'
            elif i == 'Q':
                descripto += 'J'
            elif i == 'R':
                descripto += 'K'
            elif i == 'S':
                descripto += 'L'
            elif i == 'T':
                descripto += 'Ç'
            elif i == 'U':
                descripto += 'Z'
            elif i == 'V':
                descripto += 'X'
            elif i == 'W':
                descripto += 'C'
            elif i == 'X':
                descripto += 'V'
            elif i == 'Y':
                descripto += 'B'
            elif i == 'Z':
                descripto += 'N'
            elif i == 'Ç':
                descripto += 'M'

            elif i == '\\':
                descripto += '|'
            elif i == '|':
                descripto += '/'
            elif i == '/':
                descripto += '\\'
            elif i == '.':
                descripto += '<'
            elif i == ',':
                descripto += '>'
            elif i == '>':
                descripto += '.'
            elif i == '<':
                descripto += ','
            elif i == '!':
                descripto += ')'
            elif i == '@':
                descripto += '('
            elif i == '#':
                descripto += '*'
            elif i == '$':
                descripto += '&'
            elif i == '%':
                descripto += '¨'
            elif i == '¨':
                descripto += '%'
            elif i == '&':
                descripto += '$'
            elif i == '*':
                descripto += '#'
            elif i == '(':
                descripto += '@'
            elif i == ')':
                descripto += '!'
            elif i == '_':
                descripto += '+'
            elif i == '=':
                descripto += '-'
            elif i == '+':
                descripto += '='
            elif i == '-':
                descripto += '_'
            elif i == '{':
                descripto += ']'
            elif i == ']':
                descripto += '['
            elif i == '}':
                descripto += '{'
            elif i == '[':
                descripto += '}'
            elif i == ':':
                descripto += '?'
            elif i == '?':
                descripto += ';'
            elif i == ';':
                descripto += '?'
            elif i == ' ':
                descripto += ' '

            else:
                print(f'   Caractere {cripto[j]} não registrado    ')
            j += 1

    if cripto == 'stop':
        break
    descripto.append('\n')
for i in descripto:
    print(i, end='')
        
        
        
        
        





