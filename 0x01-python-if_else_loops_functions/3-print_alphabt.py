#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) not in ['e', 'q']:
        print(chr(char_code), end='')
