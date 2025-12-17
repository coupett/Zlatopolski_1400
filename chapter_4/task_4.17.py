y_rod = int(input())
m_rod = int(input())
y_seg = int(input())
m_seg = int(input())
let = y_seg - y_rod
if m_rod > m_seg:
    let -= 1
print(let)