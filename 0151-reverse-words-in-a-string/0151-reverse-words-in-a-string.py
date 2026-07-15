class Solution(object):
    def reverseWords(self, s):

        words = s.split()

        low = 0
        high = len(words) - 1

        while(low < high):

            words[low], words[high] = words[high], words[low]

            low += 1
            high -= 1

        return " ".join(words)