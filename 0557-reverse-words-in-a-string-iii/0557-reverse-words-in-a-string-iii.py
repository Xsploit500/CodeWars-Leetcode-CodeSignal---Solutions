class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(" ")

        reversed_words = ""

        for word in words:
            word = list(word)

            left, right = 0, len(word) - 1

            while left <= right:
                word[left], word[right] = word[right], word[left]

                left += 1
                right -= 1
            
            new_word = "".join(word)

            reversed_words += new_word + " "

        return reversed_words[0:len(s)]
        