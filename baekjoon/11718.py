"""
    11718 : 그대로 출력하기
    URL : https://www.acmicpc.net/problem/11718
    Input :
        Hello
        Baekjoon
        Online Judge
    Output :
        Hello
        Baekjoon
        Online Judge
"""
while True:
    try:
        print(input())
    except EOFError:
        break