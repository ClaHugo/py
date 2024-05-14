aluno = []

while True:
    nome_aluno = input("nome: ")
    if nome_aluno == 'fim' :
        break
    aluno_parcial= input(int("parcial: "))
    aluno_bimestral= input(int("bimestral: "))
    media = (aluno_parcial+aluno_bimestral)/2
    aluno.append({'nome' : nome_aluno, "aluno-parcial" : aluno_parcial, "bimestral" :  aluno_bimestral, "media": media})
    print(aluno) 