class Solution:
    def distinctNames(self, ideas: List[str]) -> int:



        output = 0

        checker = set(ideas)

        for i in range(len(ideas)):
            word_i = ideas[i]
            suffix_i = word_i[1:]
            for j in range(i + 1, len(ideas)):
                word_j = ideas[j]
                suffix_j = word_j[1:]

                if word_i[0] != word_j[0] and word_i[1:] != word_j[1:]:
                    new_word_one = word_i[0] + suffix_j
                    new_word_two = word_j[0] + suffix_i
                
                    if new_word_one not in checker and new_word_two not in checker:
                        output += 2         
        
        return output