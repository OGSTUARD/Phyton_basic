>>> S = 'Spam'
#correo no deseado o solicitado
>>> S.find('pa')
#-1
>>> S
#'shrubbery'
>>> S.replace('pa', 'XYZ')
#'shrubbery'
>>> S
#'shrubbery'
>>> line = 'aaa,bbb,ccccc,dd'
>>> line.split(',')
#['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam'
>>> S.upper()
#'SPAM'
>>> S.isalpha() # Content tests: isalpha, isdigit, etc.
#True
>>> line = 'aaa,bbb,ccccc,dd\n'
>>> line.rstrip()
#'aaa,bbb,ccccc,dd'
>>> line.rstrip().split(',')
#['aaa', 'bbb', 'ccccc', 'dd']