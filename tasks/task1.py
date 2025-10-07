# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    num= int(input("Введите число: "))
    num_last_digit= num%10
    num_second_digit= num//10%10
    num_first_digit= num//100%10
    sum= num_last_digit + num_second_digit + num_first_digit
    print(sum)
    

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()