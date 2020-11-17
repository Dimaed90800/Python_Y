
def addItem(itemName, itemCost):
    global count_of_check
    global check
    global check_sum
    check.append(itemName+' - '+ str(itemCost))
    count_of_check +=1
    check_sum += itemCost


def printReceipt():
    global check_num
    global count_of_check
    global check_sum
    if check:
        print('Чек', str(check_num)+ '.', 'Всего предметов:', count_of_check)
        check_num +=1
        count_of_check = 0
        for i in check:
            print(i)
        print('Итого:', check_sum)
        print('-'*5)
        check_sum = 0
        check.clear()


check_num = 1
count_of_check = 0
check_sum = 0
check=[]