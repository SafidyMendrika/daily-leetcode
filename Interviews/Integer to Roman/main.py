class Solution(object):
    def intToRoman(self, num):
        roman = ""
        roman_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 
                      50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 
                      900: "CM", 1000: "M"}
        for key in sorted(roman_dict.keys(), reverse=True):
            while num >= key:
                roman += roman_dict[key]
                num -= key
        return roman
        
        

if __name__ == "__main__":
    num = 6
    s = Solution()
    print(s.intToRoman(num))