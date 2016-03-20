# Determine if a string has all unique characters.
def is_unique(s):
    for x in range(0, len(s)):
        for y in range(x+1,len(s)):
            if s[x]==s[y]:
                return False
    return True
# Should have used new array with simple 128 hash function and check for less than 128 size string
# That would have O(n) runtime (or O(1) because largest loop is 128 long)

def is_unique2(s):
    if len(s)>128:
        return False
    charset=[False]*128
    for letter in s:
        key=ord(letter)
        if charset[key]:
            return False
        charset[key]=True
    return True

# Check if one string is a permutation of the other
def is_permutation(string_one, string_two):
    if (len(string_one)!=len(string_two)):
        return False
    char_set = [0]*128
    for letter in string_one:
        char_set[ord(letter)]+=1
    for letter in string_two:
        char_set[ord(letter)]-=1
        if char_set[ord(letter)] < 0:
            return False
    return True

import unittest

class TestStringsQuestions(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(is_permutation("i","i"))
        self.assertFalse(is_permutation("hi","i"))
    def test_is_unique(self):
        self.assertTrue(is_unique('asdfghjk'))
        self.assertFalse(is_unique('ff'))
    def test_is_unique2(self):
      self.assertTrue(is_unique2('asdfghjk'))
      self.assertFalse(is_unique2('ff'))
if __name__ == '__main__':
    unittest.main()