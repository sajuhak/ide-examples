"""
Counts the most common words
in a given text.
"""

from __future__ import print_function
import re
from collections import Counter

s = "Turku is a city on the southwest coast of Finland at the mouth of the Aura River"

# find all words in the string
#TODO: type following code "words = re.findall('[a-zA-Z_]+', s)" below, as you type you get support from PyCharm

# counts the number each time a word appears
#TODO: type following code "word_counts = Counter(words)" below


print('words in given text are {}'.format(dict(word_counts)))