from operacoes import calculo_media
from operacoes import resultado_final
from operacoes import reprovado

alunos = {26 : 'maria', 101 : 'ana', 13 : 'João', 37 : 'Ágatha', 72: 'Joaquim', 5 : 'Félix'}
maria = [8,7,5,9]
ana = [9,9,8,9]
joao = [6,5,5,5]
agatha = [8,6,7.5,9]
joaquim = [6,5.5,5,7]
felix = [10,8,8,8]

#maria
maria_ = calculo_media(maria)
maria_resul = resultado_final(maria_)
#ana
ana_ = calculo_media(ana)
ana_resul = resultado_final(ana_)
#joao
joao_ = calculo_media(joao)
joao_resul = resultado_final(joao_)
#agatha 
agatha_ = calculo_media(agatha)
agatha_result = resultado_final(agatha_)
#joaquim
joaquim_ = calculo_media(joaquim)
joaquim_resul = resultado_final(joaquim_)
#felix 
felix_ = calculo_media(felix)
felix_resul = resultado_final(felix_)