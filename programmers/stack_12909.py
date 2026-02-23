# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    st = list();
    
    for c in s:
        if c == '(' :
            st.append(c)
            
        if c == ')' :
            if len(st) < 1 :
                return False
            else :
                st.pop()
    
    return len(st) == 0
            
# 아래는 테스트로 출력해 보기 위한 코드
print( solution("(hello)()"))
print( solution(")("))       
            
