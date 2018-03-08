x = int(input('Enter first number:'))
print('you entered: {}.'.format(x))
y = int(input('Enter second number:'))
print('you entered: {}.'.format(y))
z = int(input('Enter third number:'))
print('you entered: {}.'.format(z))
n = int(input('Enter last number:'))
print('you entered: {}.'.format(n))
i, j, k = 0, 0, 0


def main():
    a = [[i, j, k] for i in range(x + 1)
         for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
    print(a)


if __name__ == "__main__":
    main()
