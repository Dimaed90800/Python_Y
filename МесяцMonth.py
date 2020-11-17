def monthName(number, language):
    rus=['Январь', 'Февраль','Март', 'Апрель', 'Май', 'Июнь','Июль ','Август','Сентябрь','Октябрь',' Ноябрь', 'Декабрь']
    eng=['January', 'Febrary', 'March', 'April', 'May', 'June', 'july', 'Augest', 'September', 'October', 'November', 'December' ]
    if language == 'ru':
        month=rus[number-1]
        return month
    if language == 'en':
        month=eng[number-1]
        return month

