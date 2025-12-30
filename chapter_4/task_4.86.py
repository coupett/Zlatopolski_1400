y_rod = int(input())
m_rod = int(input())
d_rod = int(input())
y_seg = int(input())
m_seg = int(input())
d_seg = int(input())
let = y_seg - y_rod
if m_rod > m_seg or (m_rod == m_seg and d_rod > d_seg):
    let -= 1
print(let)