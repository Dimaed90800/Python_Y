from yandex_testing_lesson import is_correct_mobile_phone_number_ru


ans = ''
numbers = ['+7(900)1234567', '8(900)1234567', '+7 999 123-45-67',
           '+7-999-123-45-67', '8 (900) 123 45 67']
for i in numbers:
    if is_correct_mobile_phone_number_ru(i):
        ans = 'YES'
    else:
        ans = 'NO'
notnumber = ['9(900)1234567', '+7(9lo)1234567', '+7(900)12(345)67', 
             '+7)900(12((3456))7']
for i in notnumber:
    if is_correct_mobile_phone_number_ru(i):
        ans = 'NO'
    else:
        ans = 'YES'
print(ans)
