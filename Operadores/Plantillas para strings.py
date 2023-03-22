>>> '%s, eggs, and %s' % ('spam', 'SPAM!')
#'spam, eggs, and SPAM!'
>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!')
#'spam, eggs, and SPAM!'
>>> '{}, eggs, and {}'.format('spam', 'SPAM!')
#'spam, eggs, and SPAM!'
>>> f'{S}, eggs, and {line}'
#'spam, eggs, and aaa,bbb,ccccc,dd\n'