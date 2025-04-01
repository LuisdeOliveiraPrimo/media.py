print('\n_______________________________________')
np1 = float(input('Informe a sua nota da NP1: '))
np2 = float(input('Informe a sua nota da NP2: '))
pim = float(input('Informe a sua nota do PIM: '))
faltas = int(input('Informe o número de faltas do aluno: '))
print('---------------------------------------')


def calcular_frequencia(faltas):
    # A carga horária total é 60 horas
    carga_horaria = 60
    frequencia = ((carga_horaria - faltas) / carga_horaria) * 100
    return frequencia

def calcular_media_semestral(np1, np2, pim):
    # Calculando a média semestral (MS) com as ponderações indicadas
    ms = ((4 * np1) + (4 * np2) + (2 * pim)) / 10
    return ms

def calcular_media_final(ms, exame):
    # Calculando a média final (MF) considerando a média semestral e a nota do exame
    mf = (ms + exame) / 2
    return mf

def verificar_aprovacao(ms, mf, frequencia):
    # Verificando se o aluno tem frequência suficiente e se passou no semestre ou exame
    if frequencia >= 75:
        if ms >= 7:
            return "Aluno aprovado diretamente no semestre com a média semestral."
        else:
            print("Aluno tem direito ao exame.")
            # Cálculo da média final
            exame = float(input("Informe a nota do exame: "))
            mf = calcular_media_final(ms, exame)
            if mf >= 5:
                return "Aluno aprovado após exame."
            else:
                return "Aluno reprovado após exame e fica de dependência na matéria."
    else:
        return "Aluno reprovado por frequência insuficiente."
    
# Calculando a frequência
frequencia = calcular_frequencia(faltas)

# Calculando a média semestral
ms = calcular_media_semestral(np1, np2, pim)

# Verificando se o aluno foi aprovado
resultado = verificar_aprovacao(ms, None, frequencia)

# Exibindo o resultado final
print(resultado)











