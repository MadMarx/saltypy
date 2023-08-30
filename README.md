# salty.py - Salty.PW Python implementation

This is a Python implementation of Salty.PW password hashing algorithm. With only 18 LOC relying only on standard libraries it's very easy to verify that it does exactly what it claims to do.

On Linux, add the following line to .bashrc and you can generate your passwords from command line straight to clipboard without ever displaying them:

```
alias salty='/path/to/saltypy/salty.py|xclip -r -selection c'
```

