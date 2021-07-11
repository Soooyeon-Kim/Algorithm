def is_palindrome(word):
    word_reverse = ''
    for w in word:
        word_reverse = w + word_reverse
    if word_reverse == word:
        return True
    else:
        return False

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))