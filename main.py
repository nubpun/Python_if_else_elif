A = int(input())
B = int(input())
H = int(input())
if (H >= A) and (B >= H):
    print('Это нормально')
elif H < A:
    print('Недосып')
else:
    print('Пересып')
