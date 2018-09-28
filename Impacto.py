def Impact(file):
    fileIN=open(file, 'r')
    lineasSTR=fileIN.readlines()
    lineasList=[]
    for i in lineasSTR:
        if i[0]!='\n':
            lineasList.append(i.rstrip().split(','))
    final=[]
    for line in lineasList:
        impacto=(int(line[3])*0.5)+(int(line[4])*0.4)+(int(line[5])*0.1)
        final.append(line[0]+','+line[1]+','+line[2]+','+str(impacto)+'\n')
    fileOUT=open('./ImpactoTweetsWithMedia/'+file[:-4]+'IMPACT.csv','w')
    fileOUT.write('idTweet,'+'Fecha,'+'mediaURL,'+'Impacto'+'\n')
    for i in final:
        fileOUT.write(i)

def main():
    Impact('CINUlinks.csv')
    Impact('FAOlinks.csv')
    Impact('UNDPlinks.csv')
    Impact('UNICEFlinks.csv')
    Impact('UNODClinks.csv')
main()