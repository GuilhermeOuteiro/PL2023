import pandas as panda

def parse(line):
    if line[0]=='i': 
        return None
    p = line.split(",")
    return int(p[0]), p[1], int(p[2]), int(p[3]), int(p[4]), p[5] == '1'
    return None

def read():
    res = list()
    f = open("myheart.csv")
    
    for i, line in enumerate(f):
        parsed_line = parse(line[:-1])
        if parsed_line is not None:
            res.append(parsed_line)
    f.close()
    
    return res

#  distribuição da doença por sexo
    
def doente(paciente):
    return paciente[5]

def is_male(paciente):
    return paciente[1] == 'M'

def n_M_F (i):
    n_M = 0
    n_F = 0
    
    for paciente in i:
        if(is_male(paciente)): n_M += 1
        else: n_F += 1
        
    return (n_M, n_F)

def n_M_F_Doentes (i):
    n_M = 0
    n_F = 0
    
    for paciente in i:
        if(doente(paciente)):
            if(is_male(paciente)): n_M += 1
            else: n_F += 1
        
    return (n_M, n_F)

def dist_Gender(i):
    n_Total = n_M_F(i)
    n_Doente = n_M_F_Doentes(i)
    
    tabela = [[n_Doente[0], n_Doente[1]],[n_Total[0]-n_Doente[0],n_Total[1]-n_Doente[1]]]
    
    return panda.DataFrame(tabela,columns = ["Homem","Mulher"],index=["Com Doença","Sem Doença"])

# distribuição da doença por escalões etários

def idade_dentro(paciente, min, max):
    return paciente[0]>=min and paciente[0]<=max

def min_max_idade(i, min, max):
    n_doente = 0
    n_healthy = 0
    
    for paciente in i:
        if idade_dentro(paciente, min, max):
            if doente(paciente): n_doente += 1
            else: n_healthy += 1
    
    return [n_doente, n_healthy]

# Depois de testes com min = 20 e max = 90 foi determinado que:
#Min_Existente = 25 e Max_Existente = 80
def dist_escalao(i):
    min = 25
    tabela = []
    indice = []
    
    while min < 80:
        tabela.append(min_max_idade(i, min, min+4))
        indice.append(f"[{min}-{min+4}]")
        min += 5
        
    return panda.DataFrame(tabela,columns = ["Com Doença","Sem Doença"],index=indice)
    
# distribuição da doença por níveis de colesterol

def colesterol_dentro(paciente, min, max):
    return paciente[3]>=min and paciente[3]<=max

def min_max_colesterol(i, min, max):
    n_doente = 0
    n_healthy = 0
    
    for paciente in i:
        if colesterol_dentro(paciente, min, max):
            if doente(paciente): n_doente += 1
            else: n_healthy += 1
    
    return [n_doente, n_healthy]

# Depois de testes com min = 0 e max = 700  foi determinado que:
#Min_Existente = 0 e Max_Existente = 610
def dist_colesterol(i):
    min = 0
    tabela = []
    indice = []
    
    while min < 610:
        tabela.append(min_max_colesterol(i, min, min+9))
        indice.append(f"[{min}-{min+9}]")
        min += 10
        
    return panda.DataFrame(tabela,columns = ["Com Doença","Sem Doença"],index=indice)

# Main   
def main():
    i = read()
    
    print("\nEscolha uma opção:\n")
    print("1: Distribuição por Género")
    print("2: Distribuição por Escalões Etários")
    print("3: Distribuição por Níveis de Colesterol")
    print("0: Sair")
    
    systIn = input("\nOpção: ")
    
    if systIn == '1': 
        print("\nResultado:\n")
        print(dist_Gender(i))
    elif systIn == '2': 
        print("\nResultado:\n")
        print(dist_escalao(i))
    elif systIn == '3': 
        print("\nResultado:\n")
        print(dist_colesterol(i))
    elif systIn == '0': 
        print("Desligado")
        return
    else: 
        print("Escolha incompatível!")
        
    main()
    
main()