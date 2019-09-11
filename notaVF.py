import numpy as np

def iterador():
    VE=[]
    print('quantas VEs foram realizadas?')
    n_provas=int(input())
    for i in range (int(n_provas)):
        print('qual o peso da Ve #',i+1,'?')
        peso=input()
        print('qual foi a sua nota?')
        nota=input()
        VE.append([float(peso),float(nota)])
        
    return(VE)

def calculaMedia (VE):
    print('qual foi sua nota na VC?')
    VC=float(input())
    media_VE=0
    media=0
    soma_pesos=0
    for i in range (len(VE)):
        media_VE+=VE[i][0]*VE[i][1]
        soma_pesos+=VE[i][0]
    media=(VC+(media_VE/soma_pesos))/2
    
    return (media)

def falta(media):
    falta = 10-media
    if falta<4:
        falta=4.0
        print("Na VF voce precisa tirar:",falta)

falta(calculaMedia(iterador()))