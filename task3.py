# tasks/task3.py

def solve():
# Ниже пишите решение задачи
     n=int(input("Введите сумму: "))
     k= [100, 20, 10, 5, 1]
     k_count=0
     for k_num in k:
        k_count+= n// k_num
        n%= k_num
     print(k_count)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()