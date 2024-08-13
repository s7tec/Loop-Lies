while True:

    print("Escolha um número de 1 a 10")
    num = int(input(""))

    if num > 10:
        print("O número inserido é maior que 10, digite um valor entre 1 e 10")
    elif num < 1:
        print("O número inserido é menor que 1, digite um valor entre 1 e 10")
    else:
        print("Número valido!")
        break
print("")
print("Diante das lista abaixo escolha um dos números")

lista_num = [ 5, 1, 8, 2, 4, 9]

while True:
    escolha = int(input(f"Escolha um valor entre {lista_num}: "))

    if escolha in lista_num:
        print(f"O valor escolhido foi: {escolha}")
        break
    else:
        print("Valor invalido, escolha um dos valores da lista!")

print("")

cor = ['azul','vermelho']
while True:
    esc_cor = str(input(f"Escolha uma das cores {cor}: "))

    if esc_cor in cor:
        print(f"A cor escolhida foi: {esc_cor}")
        break
    else:
        print("Escolha uma das cores!")

print("")
if esc_cor == "azul":
    print("O azul tem o valor de 10/2, somando com os numeros anteriores escolhidos você tem o seguinte resultado: ", 5 + num + escolha)
else:
    print("O vermelho tem o valor de 25/5x2, somando com os números anteriores escolhidos você tem o seguinte resultado: ",10 + num + escolha)
print("FIM!")