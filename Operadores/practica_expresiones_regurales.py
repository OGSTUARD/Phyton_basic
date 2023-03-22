>>> import re
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello
>>> match.group(1)
#AttributeError: 'function' object has no attribute 'group'

>>> match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
>>> match.groups()
#('usr', 'home', 'lumberjack')
>>> re.split('[/:]', '/usr/home/lumberjack')
#['', 'usr', 'home', 'lumberjack']

>>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phone_num_regex.search('My number is 415-555-4242.')
>>> print(f'Phone number found: {mo.group()}')
#Phone number found: 415-555-4242

>>> phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phone_num_regex.search('My number is 415-555-4242.')
>>> mo.group(1)
#'415'
>>> mo.group(2)
#'555-4242'
>>> mo.group(0)
#'415-555-4242'
>>> mo.group()
#'415-555-4242'
>>> hero_regex = re.compile (r'Batman|Tina Fey')
>>> mo1 = hero_regex.search('Batman and Tina Fey.')
>>> mo1.group()
#'Batman'
>>> mo2 = hero_regex.search('Tina Fey and Batman.')
>>> mo2.group()
#'Tina Fey'