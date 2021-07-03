# 2주차 실습 2번 줄세우기
def lining(n) :
    MOD = int(1e9 + 7)
    dp = [[0, 0] for i in range(101)]
    
    dp[1][0] = 1
    dp[1][1] = 1
    
    for i in range(2, 101):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD # 끝이 여학생인 경우
        dp[i][1] = dp[i - 1][0] # 끝이 남학생인 경우 -> 자기 앞에 여학생만 와야 한다!!!
        
    return (dp[n][0] + dp[n][1]) % MOD