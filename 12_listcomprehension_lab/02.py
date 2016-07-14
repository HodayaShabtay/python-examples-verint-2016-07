
"""
This program prints all possible permutation of 3 small letters
"""

import sys

letters = [chr(i) for i in range(97,123)]
words = ["".join(a+b) for a in letters for b in letters]
groups = ["".join(a+b) for a in words for b in letters]
print groups