#!/usr/bin/python3

import hashlib
import getpass


digitsStr='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_=!@#$%^&*()[]{}|;:,.<>/?`~ \\\'\"+-'

def base95(n):
    if n == 0:
        return '0'
    result = ''
    while n:
        result = digitsStr[int(n % 95)] + result
        n //= 95
    return result

def main():
    pw = getpass.getpass()
    h = hashlib.sha256(pw.encode('utf-8'))
    print(base95(int(h.hexdigest()[:16], 16)))


if __name__ == '__main__':
    main()
