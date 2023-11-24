#Condicional(A, B) só será verdade se A e B for verdade ou se apenas B for verdade
#Bicondicional(A, B) só será verdade se A e B tiverem o mesmo valor

tabela_verdade = [
    [True, True],
    [True, False],
    [False, True],
    [False, False]
]

for valores in tabela_verdade:
   A, B = valores
   condicional = (not A) or B # o B determina se a operação será verdadeiro ou falso
   bicondicional = (A and B) or ((not A) and  (not B)) # Necessário que A e B tenham o mesmo valor

   print(f'A = {A}, B = {B}')
   print(f'A → B = {condicional}')
   print(f'A ↔ B = {bicondicional}')
   print('---')