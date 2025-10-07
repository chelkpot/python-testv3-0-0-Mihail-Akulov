# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n = int(input("Ввеедите кол-во минут: "))
    n = n%86400
    h = n//3600
    m = n%3600//60
    s = n%60
    m_str = "0" + str(m) if m < 10 else str(m)
    s_str = "0" + str(s) if s < 10 else str(s)
    time= ((str(h) + ":") + (str(m_str) + ":") + (str(s_str)))
    print(time)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()