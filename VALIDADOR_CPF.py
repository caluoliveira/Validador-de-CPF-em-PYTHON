#Crie um algoritmo que, dados os números do CPF, o valide como VÁLIDO ou INVÁLIDO.

print("Insira os números de seu CPF para validação: \n");
dig1 = int(input(""));
dig2 = int(input(""));
dig3 = int(input(""));
dig4 = int(input(""));
dig5 = int(input(""));
dig6 = int(input(""));
dig7 = int(input(""));
dig8 = int(input(""));
dig9 = int(input(""));
dig10 = int(input(""));
dig11 = int(input(""));
soma1 = (dig1*10+dig2*9+dig3*8+dig4*7+dig5*6+dig6*5+dig7*4+dig8*3+dig9*2)
valor1 = (soma1//11) * 11;
resultado1 = soma1 - valor1;
if (resultado1==1 or resultado1==0):
    digito1=0;
else:
    digito1=11-resultado1;
soma2 = (dig1*11+dig2*10+dig3*9+dig4*8+dig5*7+dig6*6+dig7*5+dig8*4+dig9*3)+(digito1*2);
valor2 = (soma2//11) * 11;
resultado2 = soma2 - valor2;
if (resultado2==1 or resultado2==0):
    digito2 = 0;
else:
    digito2 = 11-resultado2;
if (digito1==dig10 and digito2==dig11):
    print("O CPF informado é válido \n");
else:
    print("O CPF informado é inválido \n");