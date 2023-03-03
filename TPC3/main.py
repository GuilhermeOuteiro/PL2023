with open("processos.txt") as f:
    content = f.readlines()
    
# Todas as linhas incluindo linhas em branco
all_lines = []

for line in content:
    all_lines.append(line.strip().split('::'))
    
# A valid_lines tem todas as linhas que não estão em branco
valid_lines = [x for x in all_lines if x != ['']]

print("|Programa Iniciado|")

# ? (a) Frequência de Processo Por Ano ? #
freq_proc = dict()

datas = []

for i in range(len(valid_lines)):
    datas.append(valid_lines[i][1].split('-')[0])   

datas.sort()

c=0

while c<len(datas):
    counter = 0
    counter = datas.count(datas[c])
    freq_proc[datas[c]] = counter
    c += counter
    
# ! Escreve o Output da alinea (a) no ficheiro output1.csv ! #

f = open("output1.csv", "w")
f.write("Ano : Counter\n")
for (i,j) in freq_proc.items():
    f.write(f"{i} : {j}\n")
f.close()

print("|Output da primeira tarefa escrito no ficheiro output1.csv|")

# ? (b) Frequência de Nomes ? #
freq_n_p = {}
freq_a = {}
for line in open("processos.txt"):
    if line.strip():
        nomes_proprios = line.strip().split("::")[2:]
        for nome in nomes_proprios:
            
            while len(nome) > 0 and nome[0] == " ":
                nome = nome[1:]
            if (nome == ""): continue
            if (nome.isnumeric()): continue
            if (nome == "Proc"): continue
            if (nome.startswith("Em Anexo:")): continue
            if (nome == "Doc"): continue
            if (nome == "danificado"): continue
            if (any(char.isdigit() for char in nome)): continue
            
            nome_split = nome.split(" ")
            if len(nome_split) > 1:
                freq_n_p[nome_split[0]] = freq_n_p.get(nome_split[0], 0) + 1
                if not nome_split[-1].endswith('.'):
                    freq_a[nome_split[-1]] = freq_a.get(nome_split[-1], 0) + 1


# ! Escreve o Output da alinea (b) nos ficheiros output2*.csv ! #
f = open("output2Proprios.csv", "w")
f.write("Nome Proprio : Counter\n")
for (i,j) in freq_n_p.items():
    f.write(f"{i} : {j}\n")
f.close()

f = open("output2Apelidos.csv", "w")
f.write("Apelido : Counter\n")
for (i,j) in freq_a.items():
    f.write(f"{i} : {j}\n")
f.close()

print("|Output da segunda tarefa escrito nos ficheiros output2Proprios.csv e output2Apelidos.csv|")

# ? (c) Frequencia das relações ? #

freq_rel = {}

for x in valid_lines:
    x = str(x).split(".")
    for info in x:
        while len(info) > 0 and info[0] == " ":
            info = info[1:]
        if (info == ""): continue
        if (info.isnumeric()): continue
        if (info == "Proc"): continue
        if (info.startswith("Em Anexo:")): continue
        if (info == "Doc"): continue
        if (info == "danificado"): continue
        if (any(char.isdigit() for char in info)): continue

        nome_e_relacao = info.split(",",2)

        if len(nome_e_relacao) > 1 and not(nome_e_relacao[1].startswith(" ")) and len(nome_e_relacao[1]) < 26:
                freq_rel[nome_e_relacao[1]] = freq_rel.get(nome_e_relacao[1], 0) + 1      
        
# ! Escreve o Output da alinea (c) no ficheiro output3.csv ! #

f = open("output3.csv", "w")
f.write("Relacao : Counter\n")
for (i,j) in freq_rel.items():
    f.write(f"{i} : {j}\n")
f.close()

print("|Output da terceira tarefa escrito no ficheiro output3.csv|")

# ? (d) Escrever as primeiras 20 entradas em json ? #
import json

dict1 = {}

fields =['processo', 'data', 'nome']

with open("processos.txt") as fh:
    l = 1
    
    for line in fh:
        while l in range(21):
            description = list( line.strip().split('::'))
            
            # id de cada entrada
            sno ='n'+str(l)
            
            i = 0
            dict2 = {}
            while i<len(fields):
                # dicionário para cada entrada
                dict2[fields[i]]= description[i]
                i += 1
            
            dict1[sno]= dict2
            l += 1

# ! creating json file ! # 
out_file = open("process.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()

print("|Foi criado o ficheiro process.json relativo à quarta tarefa|")
print("|Programa Terminou|")