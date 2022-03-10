'''
题目描述
Catcher 是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
（注意：记得加上while处理多个测试用例）
输入描述:
输入一个字符串
输出描述:
返回有效密码串的最大长度
示例1
输入
ABBA
输出
4
'''

def fun(s):
#     print(s)
    size = len(s)
    dp = [[False]*size for _ in range(size)]
#     print(dp)
    for i in range(size):
        dp[i][i] = True
#     print(dp)
    start = 0
    maxlen = 0
    for i in range(1,size):
        for j in range(0, i):
            if s[i] == s[j]:
                if i-1 - (j+1) <2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j+1]
            else:
                dp[i][j] = False
        
            if dp[i][j] == True:
                cur = i - j + 1
                if cur > maxlen:
                    start= j
                    maxlen = cur
  
    return len(s[start: start+maxlen])
    
# # inp = input()
# inp = '123ABBA1111'
# if inp:
#     print(fun(inp))

while True:
    try:
        inp = input()
        if inp:
            print(fun(inp))
    except:
        break
