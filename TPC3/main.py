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
            nome_split = nome.split(" ")
            if len(nome_split) > 1:
                freq_n_p[nome_split[0]] = freq_n_p.get(nome_split[0], 0) + 1
                if not nome_split[-1].endswith('.'):
                    freq_a[nome_split[-1]] = freq_a.get(nome_split[-1], 0) + 1


# ! Escreve o Output da alinea (b) no ficheiro output2.csv ! #
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
# ? (d) Escrever as primeiras 20 entradas em json ? #
import json

dict1 = {}

fields =['processo', 'data', 'nomes']

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

print("|Foi criado o ficheiro process.json|")