
numero = input()
def luhn(numero: str) -> bool:
    
    numero = numero.replace(" ", "")
    
    
    digitos = [int(d) for d in numero[::-1]]
    
    soma = 0
    for i, digito in enumerate(digitos):
        if i % 2 == 0:  
            
            soma += digito
        else:  
            
            dobro = digito * 2
            if dobro > 9:
                dobro -= 9  
            soma += dobro
    
    return soma % 10 == 0
  
if luhn():
    print("Cartão válido!")
else:
    print("Cartão inválido!")


