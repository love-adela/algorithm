# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기
def solution(string:str)->int:
    stack = []
    for c in string:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return 1 if len(stack) == 0 else 0

params = input()
print(solution(params))

