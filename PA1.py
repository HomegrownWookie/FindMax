# Problem 1
def Problem1():
    findMax([])
    findMax([3])
    findMax([5, 2, 8])
    findMax([2, 4, 8, 1, 6])


def findMax(l1):
    if len(l1) == 0:
        print('List is Empty')
    elif len(l1) == 1:
        print("Max Entry is: ", l1[0])
    elif len(l1) > 1:
        maxNum = -1000000
        for x in range(0, len(l1)):
            temp = l1[x]
            if temp > maxNum:
                maxNum = temp
        print("Max Entry is: ", maxNum)


'''
/Users/Ian/PycharmProjects/PA1/venv/bin/python /Users/Ian/PycharmProjects/PA1/PA1.py
Which Problem Would You Like To Test? (1, 2): 1
List is Empty
Max Entry is:  3
Max Entry is:  8
Max Entry is:  8

Process finished with exit code 0
'''


# Problem 2
def Problem2():
    choice = input('Which Method Would You Like To Use? (1, 2, 3): ')
    if choice == '1':
        MethodX()
    elif choice == '2':
        MethodY()
    elif choice == '3':
        MethodZ()


def MethodX():
    listx = []
    for x in range(1, 199):
        listx.append(x);
    print(listx)


'''
/Users/Ian/PycharmProjects/PA1/venv/bin/python /Users/Ian/PycharmProjects/PA1/PA1.py
Which Problem Would You Like To Test? (1, 2): 2
Which Method Would You Like To Use? (1, 2, 3): 1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 
63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 
142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 
166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 
190, 191, 192, 193, 194, 195, 196, 197, 198]

Process finished with exit code 0
'''


# New Lines added by author for purpose of readability, system outputs list in single line.


def MethodY():
    listy = list(range(1, 199))
    print(listy)


'''
/Users/Ian/PycharmProjects/PA1/venv/bin/python /Users/Ian/PycharmProjects/PA1/PA1.py
Which Problem Would You Like To Test? (1, 2): 2
Which Method Would You Like To Use? (1, 2, 3): 2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 
63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 
142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 
166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 
190, 191, 192, 193, 194, 195, 196, 197, 198]

Process finished with exit code 0
'''


# New Lines added by author for purpose of readability, system outputs list in single line.


def MethodZ():
    listz = [z for z in range(1, 199)]
    print(listz)


'''
/Users/Ian/PycharmProjects/PA1/venv/bin/python /Users/Ian/PycharmProjects/PA1/PA1.py
Which Problem Would You Like To Test? (1, 2): 2
Which Method Would You Like To Use? (1, 2, 3): 3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 
63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 
142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 
166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 
190, 191, 192, 193, 194, 195, 196, 197, 198]

Process finished with exit code 0
'''
# New Lines added by author for purpose of readability, system outputs list in single line.


switch = input('Which Problem Would You Like To Test? (1, 2): ')

if switch == '1':
    Problem1()
elif switch == '2':
    Problem2()
