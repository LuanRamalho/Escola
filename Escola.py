#-*- coding:utf-8 -*-

class Escola:
    def Aluno():
        i = 1
        z = 0
        mediaprova = [0]*9999
        mediateste = [0]*9999
        mediafinal = [0]*9999
        prova1 = [0]*9999
        prova2 = [0]*9999
        teste1 = [0]*9999
        teste2 = [0]*9999
        frequência = [0]*9999
        
        print("Digite a quantidade de alunos a serem avaliados: ")
        qtd = int(input())
        while(i>0 and z<qtd):
            print("Digite a nota do primeiro teste: ")
            teste1[z] = float(input())
            
            while(teste1[z] ==-0 or teste1[z]>10):
                print("Valor Errado. Digite o valor correto")
            
            print("Digite a nota da primeira prova: ")
            prova1[z] = float(input())
            
            while(prova1[z] ==-0 or prova1[z]>10):
                print("Valor Errado. Digite o valor correto")
                
            print("Digite a nota do segundo teste: ")
            teste2[z] = float(input())
            
            while(teste2[z] ==-0 or teste2[z]>10):
                print("Valor Errado. Digite o valor correto")    
            
            print("Digite a nota da segunda prova: ")
            prova2[z] = float(input())
            
            while(prova2[z] ==-0 or prova2[z]>10):
                print("Valor Errado. Digite o valor correto")
            
            mediateste[z] = ( teste1[z] + teste2[z] ) / 2
            mediaprova[z] = ( prova1[z] + prova2[z] ) / 2
            mediafinal[z] = ( mediateste[z] + mediaprova[z] ) / 2
            
            print("Digite a frequência do aluno: ")
            frequência[z] = float(input())
                
            print("")
            print("")
            
            z = z + 1
            print("Digite 1 para continuar ou 0 para sair: ")
            i = int(input())
            
            print("")
            
            
        i = 0
        c = 1
        while(i<z):
            print("Nota do primeiro teste do ", c , "º aluno: %.1f" % teste1[i])
            print("Nota do segundo teste do ", c , "º aluno: %.1f " % teste2[i])
            print("Nota da primeira prova do ", c , "º aluno: %.1f " % prova1[i])
            print("Nota da segunda prova do ", c , "º aluno: %.1f " % prova2[i])
            
            print("")
            
            print("Média do Teste do ", c , "º aluno: %.1f " % mediateste[i])
            print("Média da Prova do ", c , "º aluno: %.1f " % mediaprova[i])
            print("Média final do ", c , "º aluno: %.1f " % mediafinal[i])
            
            print("") 
            
            print("Frequência do ", c , "º aluno: %.1f %%" % frequência[i])
            
            print("")
            print("")
            
            if ( mediafinal[i]>=6 and frequência[i]>=75 ):
                print("Esse aluno está aprovado.")
            elif (mediafinal[i]<6 or frequência[i]<75):   
                print("Este aluno está reprovado.")
            
            
            i = i + 1
            c = c + 1
            
            print("")
            print("")
            

       
e = Escola
e.Aluno()
           
            
            
            
                