"""
 Author: Connor Kouznetsov
 Description: This is a python practice file for ZyLab's under Activity #6
"""

'''*****Zylab 5.15 Adjust values in a list by normalizing *****'''

stop = 9
total = 0
for number in [7, 2, 5, 5, 4, 4]:
    print(number, end=' ')
    total += number
    if total >= stop:
        print('!')
        break
else:
    print(f'/ {total}')
print('done')