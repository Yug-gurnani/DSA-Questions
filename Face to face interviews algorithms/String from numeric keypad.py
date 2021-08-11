def letterCombinations(self, digits):
    ans = []
    dic = {0:[],"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
    digits = list(digits)
    if len(digits) == 0:
        return dic[0]
    if len(digits) == 1:
        return dic[digits[0]]
    else:
        def backtrack(comb,digits,ans,dic):
            if len(digits) == 0:
                ans.append(comb)
                return
            else:
                for i in dic[digits[0]]:
                    backtrack(comb + i,digits[1:],ans,dic)
            
        backtrack("",digits,ans,dic)
        return ans