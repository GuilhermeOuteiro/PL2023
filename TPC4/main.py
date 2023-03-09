import json

# Parsing de cada linha
def parse(line):
    if line[0]=='N': 
        return None
    p = list(line.strip().split(",", 3))
    if(len(p)==4):
        return int(p[0]), str(p[1]), str(p[2]), p[3]
    else:
        return int(p[0]), str(p[1]), str(p[2])
    return None

#  Função para criar os ficheiros Json #
# ! flag = 1..5 (error if another value), file = ficheiro origem, fields = [parametros do json], outputfile = ficheiro output ! #
def toJson(flag, file, fields, outputfile):
    dict1 = {}
    with open(file) as fh:
        l = 1
        for line in fh:
            content = parse(line)
            sno ='n'+str(l)
            i = 0
            dict2 = {}
            # A flag = 1 Trata do ficheiro alunos.csv 
            if flag == 1:
                if content == None: continue
                else:
                    while i<len(fields):
                        # dicionário para cada entrada
                        dict2[fields[i]]= content[i]
                        i += 1
                    dict1[sno]= dict2
                    l += 1
            # A flag = 2 Trata do ficheiro alunos2.csv (notas{5})
            if flag == 2:
                if content == None: continue
                else:
                    while i<len(fields)-1:
                        # dicionário para cada entrada
                        dict2[fields[i]]= content[i]
                        i += 1
                    if (i == len(fields)-1):
                        notas = content[i].split(",")
                        notas_int = []
                        for n in notas:
                            if n == '': continue
                            notas_int.append(int(n))
                        counter = 0
                        while counter <5:
                            dict2[fields[i]]= str(notas_int)
                            counter += 1
                        i += 1
                    dict1[sno]= dict2
                    l += 1
            # A flag = 3 Trata do ficheiro alunos3.csv (notas{3-5})
            if flag == 3:
                if content == None: continue
                else:
                    while i<len(fields)-1:
                        # dicionário para cada entrada
                        dict2[fields[i]]= content[i]
                        i += 1
                    if (i == len(fields)-1):
                        notas = content[i].split(",")
                        notas_int = []
                        for n in notas:
                            if n == '': continue
                            notas_int.append(int(n))
                        while len(notas_int) < 3: 
                            notas_int.append(' ')
                        counter = 0
                        while counter <5:
                            dict2[fields[i]]= str(notas_int)
                            counter += 1
                        i += 1
                    dict1[sno]= dict2
                    l += 1
            # A flag = 4 e flag = 5 Trata do ficheiro alunos4.csv (notas_sum) alunos5.csv (notas_media)
            if flag == 4 or flag == 5:
                if content == None: continue
                else:
                    while i<len(fields)-1:
                        # dicionário para cada entrada
                        dict2[fields[i]]= content[i]
                        i += 1
                    if i == len(fields)-1:
                        notas = content[i].split(",")
                        sum = 0
                        for n in notas:
                            if n != '':
                                sum += int(n)
                        if flag == 4:
                            dict2[fields[i]]= sum
                            i += 1
                        elif flag == 5:
                            dict2[fields[i]]= sum / len(notas)
                            i += 1
                        dict1[sno]= dict2
                    l += 1

    # ! creating json file ! # 
    out_file = open(outputfile, "w", encoding='iso-8859-1')
    json.dump(dict1, out_file, indent = 4, ensure_ascii=False)
    out_file.close()
    
    print("Informação Escrita no ficheiro: "+outputfile+"!")
    
def main():
    fields1 = ['Numero', 'Nome', 'Curso']
    fields2 = ['Numero', 'Nome', 'Curso', 'Notas']
    fields3 = ['Numero', 'Nome', 'Curso', 'Notas']
    fields4 = ['Numero', 'Nome', 'Curso', 'Notas_Sum']
    fields5 = ['Numero', 'Nome', 'Curso', 'Notas_Media']
    
    toJson(1, "alunos.csv", fields1, "alunos.json")
    toJson(2, "alunos2.csv", fields2, "alunos2.json")
    toJson(3, "alunos3.csv", fields3, "alunos3.json")
    toJson(4, "alunos4.csv", fields4, "alunos4.json")
    toJson(5, "alunos5.csv", fields5, "alunos5.json")

main()    