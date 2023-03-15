import re
from sys import stdin

def comando_invalido():
    print("\n+" + "-" * 23 + "+")
    print("|Comando Inválido|")
    print("+" + "-" * 23 + "+\n")

def pousar(saldo):
    print("\n+" + "-" * 23 + "+")
    print(f"|maq: Troco: {saldo}|")
    print("|maq: Volte Sempre!|")
    print("+" + "-" * 23 + "+\n")
    exit()

def abortar(saldo):
    print("\n+" + "-" * 23 + "+")
    print(f"|maq: Valor da Decolução: {saldo}|")
    print("|maq: Volte Sempre!|")
    print("+" + "-" * 23 + "+\n")
    exit()

def depositar_dinheiro(money, saldo):
    if money in saldo:
        saldo[money] +=1
    else: saldo[money] =1
    
def transf_para_saldo(dinheiro):
    saldo = dict()

    while dinheiro > 0:
        if dinheiro >= 500:
            depositar_dinheiro("500e",saldo)
            dinheiro -= 500

        elif dinheiro >= 200:
            depositar_dinheiro("200e",saldo)
            dinheiro -= 200   

        elif dinheiro >= 100:
            depositar_dinheiro("100e",saldo)
            dinheiro -= 100

        elif dinheiro >= 50:
            depositar_dinheiro("50e",saldo)
            dinheiro -= 50

        elif dinheiro >= 20:
            depositar_dinheiro("20e",saldo)
            dinheiro -= 20

        elif dinheiro >= 10:
            depositar_dinheiro("10e",saldo)
            dinheiro -= 10

        elif dinheiro >= 5:
            depositar_dinheiro("5e",saldo)
            dinheiro -= 5

        elif dinheiro >= 2:
            depositar_dinheiro("2e",saldo)
            dinheiro -= 2

        elif dinheiro >= 1:
            depositar_dinheiro("1e",saldo)
            dinheiro -= 1

        elif dinheiro >= 0.5:
            depositar_dinheiro("50c",saldo)
            dinheiro -= 0.5

        elif dinheiro >= 0.2:
            depositar_dinheiro("20c",saldo)
            dinheiro -= 0.2

        elif dinheiro >= 0.1:
            depositar_dinheiro("10c",saldo)
            dinheiro -= 0.1

        elif dinheiro >= 0.05:
            depositar_dinheiro("5c",saldo)
            dinheiro -= 0.05

        elif dinheiro >= 0.02:
            depositar_dinheiro("2c",saldo)
            dinheiro -= 0.02

        elif dinheiro >= 0.01:
            depositar_dinheiro("1c",saldo)
            dinheiro -= 0.01

        else: break;              

    res = ""
    for key in saldo:
        res += f"{saldo[key]}x{key}, "
    if (res == ""): return "[Sem troco]"
    else: return res[:-2]

def validar_dinheiro(money):
    return int(re.search(r"\d+", money).group()) in [1,2,5,10,20,50,100,200,500]

def print_saldo(saldo):  
    e = int(saldo)
    c = int((saldo - e) * 100)
    print("\n+" + "-" * 23 + "+")
    print(f"|maq: saldo = {e}e{c}c|")
    print("+" + "-" * 23 + "+\n")
    
def saldo_para_transf(saldo):
    res = 0.0
    for money in saldo:
        valor = float(re.search(r"\d+", money).group())
        if not validar_dinheiro(money):
            print("\n+" + "-" * 31 + "+")
            print(f"|maq: {money} - moeda inválida;|\n", end="")
            print("+" + "-" * 31 + "+")
            continue
        if money[-1] == "c":
            valor /= 100
        res += valor
    return res

# ! Main ! #

saldo = 0
status = "OFF"
    
print("\n+" + "-" * 23 + "+")  
print("|maq: Levante o telefone|")
print("+" + "-" * 23 + "+\n")  

for systIn in stdin:
    systIn = systIn[:-1]
    
    if systIn == "Levantar" or systIn == "LEVANTAR":
        status = "ON"
        print("\n+" + "-" * 23 + "+")
        print("|maq: Introduza moedas.|")
        print("+" + "-" * 23 + "+\n")
            
    elif systIn == "Pousar" or systIn == "POUSAR":
        if status == "OFF" :
            print("\n+" + "-" * 23 + "+")  
            print("|maq: Levante o telefone|")
            print("+" + "-" * 23 + "+\n")
            continue
        pousar(saldo)
            
    elif re.fullmatch(r"Moeda [\d+(c|e)(, |.)]+", systIn) or re.fullmatch(r"MOEDA [\d+(c|e)(, |.)]+", systIn):
        if status == "OFF" :
            print("\n+" + "-" * 23 + "+")  
            print("|maq: Levante o telefone|")
            print("+" + "-" * 23 + "+\n")
            continue
        transf = re.findall(r"(\d+[c|e])", systIn)
        saldo += saldo_para_transf(transf)
        print_saldo(saldo)
            
    elif re.fullmatch(r"T=((00\d+)|(\d{9}))", systIn):
        if status == "OFF" :
            print("\n+" + "-" * 23 + "+")  
            print("|maq: Levante o telefone|")
            print("+" + "-" * 23 + "+\n")
            continue
        
        if re.match(r"T=6(0|4)1", systIn):
            print("\n+" + "-" * 40 + "+")
            print("|maq: Número inválido. Digite novamente!|")
            print("+" + "-" * 40 + "+\n")
            continue
        
        custo = 0.0

        if re.match("T=00", systIn):

            custo = 1.5

        elif re.match("T=2", systIn):

            custo = 0.25

        elif re.match("T=808", systIn):

            custo = 0.1

        if custo > saldo:
            print("\n+" + "-" * 31 + "+")
            print(f"|maq: Saldo Insuficiente.|")
            print(f"|maq: Troco: {saldo}|")
            print("|maq: Volte Sempre!|")
            print("+" + "-" * 31 + "+\n")
            exit()

        else:

            saldo -= custo

        print_saldo(saldo)
        
    elif systIn == "Abortar" or systIn == "ABORTAR":
        abortar(saldo)
            
    else: comando_invalido()
