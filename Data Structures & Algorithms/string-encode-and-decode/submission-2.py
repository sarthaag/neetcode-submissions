class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
        # TODO: Find algo that's O(n) instead of O(n^2) here 

    # can probably just do result = result += [string] but is that inefficient? let's just do it first 
    def decode(self, s: str) -> List[str]:
        # lst = []
        # temp = []
        # count = 0
        # # "4#hell5#world" --> ["hell", "world"]
        # # to make a string of length n with just the += operation one char at a time, this is O(n^2) operations. So preferable to add all chars to a list and then use .join operation i think. 
        # for char in s:
        #     if #char is an integer and not count:
        #         count = int(char)
        #     else:

        # Ok forgot to account for the fact that the num indicating the length of the string after it can be multiple digits. Therefore, just look for the part of the string all the way up until the # character and use that as the length. 
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            nextstr = s[j+1:j+1+length]
            result.append(nextstr)
            i = j + 1 + length
        return result

# First thought: just combine all the strings into one, adding something to indicate separation. Spaces not good bc each of the individual strings could have spaces. Idt this works at all actually. You can't get rid of any of the characters though.
# ["he llo","world"] -> ["he llo world"]
# Tech: after each string include the length of the string as a number? But how to differentiate that with any numbers present in the string? 
# WHat the fuck is this bro 
# I see. Have number followed by # to indicate how many characters make up the following string. Even if there is another 4# or something WITHIN the string, it will get ignored because of the starting number + # we added. Now to code it. 

