class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel=0
        consonant=0
        vowelset={'a','e','i','o','u'}
        for char in s:
            if char.isalpha():
                if char in vowelset:
                    vowel+=1
                else:
                    consonant+=1
        if consonant>0:
            return vowel//consonant
        else:
            return 0
            #done