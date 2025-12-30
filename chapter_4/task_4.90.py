n = int(input())
m = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    m_prev = m - 1
    n_prev = days[m_prev - 1]
else:
    m_prev = m
    n_prev = n - 1
print(n_prev, m_prev)

n = int(input())
m = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == days[m - 1]:
    m_next = m + 1
    n_next = 1
else:
    m_next = m
    n_next = n + 1
print(n_next, m_next)

g = int(input())
m = int(input())
n = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    if m == 1:
        g_prev = g - 1
        m_prev = 12
        n_prev = 31
    else:
        g_prev = g
        m_prev = m - 1
        n_prev = days[m_prev - 1]
else:
    g_prev = g
    m_prev = m
    n_prev = n - 1
print(n_prev, m_prev, g_prev)

g = int(input())
m = int(input())
n = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == days[m - 1]:
    if m == 12:
        g_next = g + 1
        m_next = 1
        n_next = 1
    else:
        g_next = g
        m_next = m + 1
        n_next = 1
else:
    g_next = g
    m_next = m
    n_next = n + 1
print(n_next, m_next, g_next)

g = int(input())
m = int(input())
n = int(input())
vis = (g % 400 == 0) or (g % 4 == 0 and g % 100 != 0)
days = [31, 29 if vis else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    if m == 1:
        g_prev = g - 1
        vis_prev = (g_prev % 400 == 0) or (g_prev % 4 == 0 and g_prev % 100 != 0)
        days_prev = [31, 29 if vis_prev else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        m_prev = 12
        n_prev = days_prev[11]
    else:
        g_prev = g
        m_prev = m - 1
        n_prev = days[m_prev - 1]
else:
    g_prev = g
    m_prev = m
    n_prev = n - 1
print(n_prev, m_prev, g_prev)

g = int(input())
m = int(input())
n = int(input())
vis = (g % 400 == 0) or (g % 4 == 0 and g % 100 != 0)
days = [31, 29 if vis else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == days[m - 1]:
    if m == 12:
        g_next = g + 1
        m_next = 1
        n_next = 1
    else:
        g_next = g
        m_next = m + 1
        n_next = 1
else:
    g_next = g
    m_next = m
    n_next = n + 1
print(n_next, m_next, g_next)