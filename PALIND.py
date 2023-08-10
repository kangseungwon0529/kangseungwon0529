word = input()
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        break
else:
    print(word)
    print(f"입력하신 단어는 회문(Palindrome)입니다.")
    eye