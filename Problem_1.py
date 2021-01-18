'''
Project Euler
Problem 1

'''
def euler (limit, multiple_1, multiple_2):
    sum = 0
    for i in range (limit):
        if i % multiple_1 == 0 or i % multiple_2 == 0:
            sum = sum + i
    print (sum)

if __name__ == '__main__':
    euler(1000, 3, 5)