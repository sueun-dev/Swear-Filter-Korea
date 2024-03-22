import re

# 중복 제거를 위해 세트 사용
banned_words = set()

# 텍스트 파일에서 비속어 목록을 읽어와서 세트에 저장
with open("fword_list.txt", "r", encoding="utf-8") as file:
    for line in file:
        banned_words.add(line.strip())

# 자연스러운 순서로 정렬하기 위한 키 함수
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# 중복 제거된 비속어 목록을 리스트로 변환하고 자연스러운 순서로 정렬
banned_words_list = sorted(list(banned_words), key=natural_sort_key)

# 중복 제거된 비속어 목록을 지정된 형식의 문자열로 변환
formatted_words = '["' + '", "'.join(banned_words_list) + '"]'

# 지정된 형식의 문자열을 텍스트 파일에 저장
with open("formatted_banned_words.txt", "w", encoding="utf-8") as file:
    file.write(formatted_words)

print("중복 제거된 비속어 목록이 'formatted_banned_words.txt' 파일에 저장되었습니다.")
