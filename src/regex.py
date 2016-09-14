import re

# Find a link to a snapchat account
snap_pattern = re.compile(r'(S|s)nap')

# Find a link to a tumblr account
tumblr_pattern = re.compile(r'(T|t)umblr')

# Find a link to an instagram account
insta_pattern = re.compile(r'(I|i)nsta')

# Self reference match
self_pattern = re.compile(r'\b[Ee][Uu]\b')

# Laughter
laugh_pattern = re.compile(r'\b[AEIHaeih]+[Hh][AEIaei]*\b')

# Full caps words
caps_pattern = re.compile(r'\b[A-Z][A-Z]+\b')

# Repeated alphabet
repeated_pattern = re.compile(r'(\w)(\1{2,})')

# Ellipse pattern
ellipse_pattern = re.compile(r'\.\.+')

# Affirmative statement
yes_pattern = re.compile(r'(\b[Yy][AaEe]*[YyAaEeSs]+)|(\b[Ss]i+m+\b)')

# Exclaim presence
exc_pattern = re.compile(r'!+')

# Question presence
question_pattern = re.compile(r'\?+')
