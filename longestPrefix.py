class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        prefix = ''
        if len(strs) != 0:
            temp_prefix = ''
            for i in range(len(strs[0])):
                temp_prefix += strs[0][i]
                
                match = True
                for string in strs:
                    if string != "":
                        if i == 0:
                            pref = string[0]
                        else:
                            pref = string[0:i+1]
                        if pref != temp_prefix:
                            match = False
                            break    
                    else:
                        match = False
                if match == True:
                    prefix += strs[0][i]
        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix([]))

print(sol.longestCommonPrefix(["abab","aba",""]))