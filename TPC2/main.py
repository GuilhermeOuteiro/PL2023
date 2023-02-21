def is_on(i):
    return i[:2] == "ON"

def is_off(i):
    return i[:3] == "OFF"

def is_equal(i):
    return i[0] == "="

def get_number(i):
    if not i[0].isdigit(): return None
    
    number = ""
    index = 0
    
    while index<len(i) and i[index].isdigit():
        number += i[index]
        index += 1
        
    return (int(number), index)

#função principal!!

strin = input("Escreva a Sequência: ")
print()
#função upper tranforma todo o texto em letra maiuscula sendo possivel realizar a inspeção das palavras "ON" e "OFF"
strin = strin.upper()
#Assumimos que no inicio o o programa está "OFF"
turned_on = False
res = 0

while len(strin) > 0:
    if is_off(strin):
        turned_on = False
        strin = strin[3:]
    elif is_on(strin):
        turned_on = True
        strin = strin[2:]
    elif is_equal(strin):
        print("O Resultado Neste Ponto é: ", res, "!")
        strin = strin[1:]
    elif strin[0].isdigit() and turned_on:
        number, index = get_number(strin)
        res += number
        strin = strin[index:]
    else: strin = strin[1:]
    
print()
print("Resultado Final: ", res,"!")