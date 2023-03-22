>>> dir(S) # S es un string
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(S.replace)
#Help on built-in function replace:

#replace(old, new, count=-1, /) method of builtins.str instance
    #Return a copy with all occurrences of substring old replaced by new.
    
      #count
        #Maximum number of occurrences to replace.
        #-1 (the default value) means replace all occurrences.
    
    #If the optional argument count is given, only the first count occurrences are
    #replaced.
>>> S = 'A\nB\tC'
>>> len(S)
#5
>>> ord('\n')
#10
>>> S = 'A\0B\0C'
>>> len(S)
#5
>>> S
#'A\x00B\x00C'
>>> msg = """
aaaaaaaaaaaaa
Strings | 105bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc
"""
>>> msg
#'\naaaaaaaaaaaaa\nStrings | 105bbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\ncccccccccccccc\n'