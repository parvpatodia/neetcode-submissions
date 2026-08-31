class Solution:

    def encode(self, strs):
        encoded_strs = ""
        for i in range(len(strs)):
            encoded_strs += str(len(strs[i]))+ "#" + (strs[i])
        return encoded_strs

    def decode(self, encoded_strs):
        l = 0
        result = []
        while l < len(encoded_strs):
            pos = encoded_strs.find("#", l)
            length = int(encoded_strs[l:pos])# the digit substring from l to pos
            content = encoded_strs[pos+1:pos+1+length]# length characters, starting 
            result.append(content)
            l = pos + 1 + length
        return result