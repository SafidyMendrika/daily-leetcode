class Solution(object):
    def lengthOfLastWord(self, s):
        has_letter = False
        reverse_index = 0
        sentence_length = len(s)
        letter_count = 0

        
        while reverse_index != sentence_length : 
            current_char = s[-1-reverse_index] 
            if current_char != " " and not has_letter : has_letter = True 

            if current_char == " " and has_letter : return letter_count

            if has_letter : letter_count += 1

            reverse_index += 1


        return letter_count
            



        

if __name__ == "__main__":
    s = Solution()
    sentence = "Hello World"

    print(s.lengthOfLastWord(sentence))