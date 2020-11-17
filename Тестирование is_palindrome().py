from yandex_testing_lesson import is_palindrome


ans = ''
palindrome = ['pollop', '1221', '6', 'r', ' ', 'lw5tet5wl', '66666', 'rrr']
for i in palindrome:
    if is_palindrome(i) in palindrome:
        ans = 'YES'
    else:
        ans = 'NO'
notpalindrome = ['3475', 'hello', ' 9', ' r', 'pool', '78fghmdfn34', 'krgb683j']
for i in notpalindrome:
    if is_palindrome(i) in notpalindrome:
        ans = 'NO'
    else:
        ans = 'YES'
print(ans)