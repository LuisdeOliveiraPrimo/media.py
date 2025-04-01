# Solicita as notas e o número de faltas do aluno
np1 = float(input('Informe a sua nota da NP1: '))
np2 = float(input('Informe a sua nota da NP2: '))
pim = float(input('Informe a sua nota do PIM: '))
faltas = int(input('Informe o número de faltas do aluno: '))

# Definição da carga horária total e cálculo da frequência
carga_horaria = 60
frequencia = ((carga_horaria - faltas) / carga_horaria) * 100

# Cálculo da média semestral (MS)
ms = ((4 * np1) + (4 * np2) + (2 * pim)) / 10

# Verifica se a frequência mínima foi atingida
if frequencia < 75:
    print("Aluno reprovado por frequência insuficiente.")
else:
    # Verifica se a média semestral é suficiente para aprovação direta
    if ms >= 7:
        print("Aluno aprovado diretamente no semestre com a média semestral.")
    else:
        print("Aluno tem direito ao exame.")
        exame = float(input("Informe a nota do exame: "))

        # Cálculo da média final (MF)
        mf = (ms + exame) / 2

        # Verifica se o aluno foi aprovado após o exame
        if mf >= 5:
            print("Aluno aprovado após exame.")
        else:
            print("Aluno reprovado após exame e fica de dependência na matéria.")
