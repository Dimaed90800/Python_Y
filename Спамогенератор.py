def letter( email, name, date, place='Москва'):
    read=''
    read+= 'To: '+ email +'\n'
    read+= 'Здравствуйте'+', '+ name +'!' + '\n'
    read+= 'Были бы рады видеть вас на встрече начинающих программистов в '+ place +','+' которая пройдет ' +  date +'.'+'\n'
    return read


print(letter(email='VMaria@mail.ru', name='Мария', date='5 марта', place='Калининград'))
print(letter(email='Shlyahova@mail.ru', name='Анастасия', date='5 марта', place='Калининград'))