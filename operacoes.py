media_baixa = ""

def calculo_media(notas):
    media = sum(notas)/4
    print(media)
    return media

def resultado_final(media):
    if media < 6:
        print('Reprovado')
        return 
    else:
        print("Aluno aprovado")

def reprovado(aluno,matricula):
    if media_baixa < 6:
        print(f"Aluno reprovado: {aluno} com a matrícula {matricula} teve a média {media_baixa}")
