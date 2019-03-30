##boole calculate : and, or, not
### priority: not > and> or
##比赛计分
def main():##either player has higher score than 15
    while not(scoreA == 15 or scoreB == 15):
        #比赛继续
        ##一方到达7分，另一方没有的风
        ##表达式为：a > 15 or b > 15 or (a > 7 and  b = 0) or (b > 7 and a = 0)
"""
德摩根定律
a == 15 or b == 15 -> (not a == 15) and (not b == 15)
"""
while scoreA != 15 and scoreB != 15:
    #continue