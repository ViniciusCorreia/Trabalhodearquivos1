
import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
coluna_cep = 5
leitura = open("cep_ordenado.dat",'rb')
leitura.seek(0,2)
posicao_inicial = 0
posicao_final = leitura.tell()

leitura.seek(0)        
leitura.seek(posicao_final - registroCEP.size)

contador=0
chave=int(input("Digite o cep que deseja procurar(8 digitos):"))

posicao_meio=0
while(posicao_inicial <= posicao_final):
    print(posicao_inicial,':' ,posicao_meio,':' , posicao_final)
    num_diretorios = (posicao_final - posicao_inicial) / registroCEP.size 
    posicao_meio =int(posicao_inicial + ((num_diretorios // 2) * registroCEP.size))
    leitura.seek(posicao_meio)
    meio = leitura.read(registroCEP.size)
    linha_meio = registroCEP.unpack(meio)
    
    contador = contador + 1

    cep=int(linha_meio[coluna_cep])
    
    print(posicao_inicial,':' ,posicao_meio,':' , posicao_final)

    if chave == cep:
        for i in range(0,len(linha_meio)-1):
            print(str(linha_meio[i],'latin1'))
            print('====================================')
        break
    if chave > cep:
        posicao_inicial = posicao_meio + registroCEP.size
   
    if chave < cep:
        posicao_final = posicao_meio - registroCEP.size
                
print("O número de buscas binárias foi:" , contador)

                    
            
            
                    
            
            
            
            
            
            
            
            

