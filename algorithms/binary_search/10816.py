import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
dic = {}

# 딕셔너리로 생성 {10 : 0, 9: 0 ... }
for i in m_list:
    dic[i] = int(0)

for i in n_list:
    # 딕셔너리 키 값으로 조회해서 있다면 1개 카운트
    if i in dic:
        dic[i] += 1

# 딕셔너리 키 값으로 출력하기
for i in m_list:
    print(dic[i], end=" ")
