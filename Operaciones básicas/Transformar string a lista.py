>>> S = 'shrubbery'
>>> L = list(S)
>>> L
#['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
>>> L[1] = 'c'
>>> ''.join(L)
#'scrubbery'
>>> B = bytearray(b'spam')
>>> B.extend(b'eggs')
>>> B
#bytearray(b'spameggs')
>>> B.decode()
#'spameggs'