n = int(input())
if n % 2 != 0: #reminder
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5: #n is between 2 and 5
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
else:
    print('Not Weird')
