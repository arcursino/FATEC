# n = int(input())
#
# for x in range (n):
#     nome = input()
#
#     if nome == nome[::-1]:
#         print("sim")
#
#     else:
#         print("nao")
#
# n = int(input())
# palindrome = True
#
# for x in range(n):
#     nome = input()
#
#     nome_invertido = nome[::-1]
#
#     palindrome = True
#     for i in range(len(nome)):
#         if nome[i] != nome_invertido[i]:
#             print('nao')
#             palindrome = False
#             break
#
#     if palindrome:
#         print('sim')

n = int(input())
palindrome = True

for x in range(n):
    nome = input()
    metade = len(nome) // 2

    palindrome = True
    for i in range(metade):
        if nome[i] != nome[len(nome) - i - 1]:
            print('nao')
            palindrome = False
            break
    if palindrome:
        print('sim')
