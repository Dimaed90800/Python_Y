from yandex_testing_lesson import is_prime


ans = ''
prime_nums = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31',
              '83', '89', '97', '101', '103', '107', '109']
for i in prime_nums:    
    if is_prime(i) in prime_nums:
        ans = 'YES'
    else:
        ans = 'NO'
complicated = ['6', '9', '144', '1075', '6111']
for i in complicated:
    if is_prime(i) in complicated:
        ans = 'NO'
    else:
        ans = 'YES'
if is_prime('0') != 'ValueError' or is_prime('1') != 'ValueError':
        ans = 'NO'
print('ans')