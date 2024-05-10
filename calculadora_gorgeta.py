print("Calculadora de Gorgeta")
conta = float(input("Qual foi o valor da conta? R$ "))
gorgeta = int(input("Qual a porcentagem da gorgeta? 10, 12 ou 15? "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))

gorgeta_as_percent = gorgeta / 100
total_gorgeta_amount = conta * gorgeta_as_percent
total_conta = conta + total_gorgeta_amount
conta_per_person = total_conta / pessoas
final_amount = round(conta_per_person, 2)





<<<<<<< HEAD
print(f"Cada pessoa pagará: R${final_amount}")
=======
print(f"Cada pessoa pagará: R${final_amount} ")
>>>>>>> ebabb7e056920f3145612580ec5afd5478cfe223

