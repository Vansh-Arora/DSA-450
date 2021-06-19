## Recursively print all sentences that can be formed from list of word lists

def generate(str,sub, ans):
    ## Base case
    # if number of rows becomes equal to words in my answer then print
    if len(ans) == len(str):
        print(ans)
        return
    if sub >= len(str):
        return
    for i in str[sub]:
        ans.append(i)
        generate(str,sub+1,ans)
        ans.pop()
    
inp = [["you", "we"],["have", "are"],["sleep", "eat", "drink"]]
generate(inp,0,[])