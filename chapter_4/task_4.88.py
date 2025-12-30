y_rod = int(input())
m_rod = int(input())
y_seg = int(input())
m_seg = int(input())
let = y_seg - y_rod
months = m_seg - m_rod
if months < 0:
    let -= 1
    months += 12
print(let, "лет", months, "месяцев")