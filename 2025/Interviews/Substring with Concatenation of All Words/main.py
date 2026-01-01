from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        one_word = len(words[0])
        n = len(s)
        word_count = Counter(words)
        res = []
        for i in range(one_word):
            left = i
            sub_dict = Counter()
            count = 0
            for j in range(i, n - one_word + 1, one_word):
                word = s[j:j + one_word]
                if word in word_count:
                    sub_dict[word] += 1
                    count += 1
                    while sub_dict[word] > word_count[word]:
                        sub_dict[s[left:left + one_word]] -= 1
                        left += one_word
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    sub_dict.clear()
                    count = 0
                    left = j + one_word
        return res
        

if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    solution = Solution()
    print(solution.findSubstring(s, words))