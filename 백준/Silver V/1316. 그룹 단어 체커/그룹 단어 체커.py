n = int(input())
cnt = 0


def is_group_word(word):
    group_keys = []
    # 단어 한 글자씩 순회
    for j in range(len(word)):
        # 첫 문자는 별 체크 필요 없음
        if j == 0:
            group_keys.append(word[j])
        # 두 번째 문자 이후 부터 앞 문자와 같은 지 체크
        # 앞 문자 != 현재 문자인 경우,
        #   이미 키로 삽입된 전적이 있다 == 같은 문자가 뒤에 동 떨어져 있다는 뜻이므로 Fasle 리턴
        #                     없다 == 처음 나오는 문자로 판단하여 그룹 키 삽입
        # 앞 문자 == 현재 문자인 경우, 별 처리 필요 없음
        else:
            if word[j - 1] != word[j]:
                if word[j] in group_keys:
                    return False
                else:
                    group_keys.append(word[j])  # 반례 추가
    return True


for i in range(n):
    word = input()
    if is_group_word(word):
        cnt += 1

print(cnt)

# 아스키 정렬을 할까 생각했는데, 그냥 눈으로 문제풀듯이 문자열 하나씩 비교
# 귀찮아도 일단 적으면서 생각해보자..

'''
2
abcb
abbcbb
'''
