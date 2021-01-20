import datetime
import sys
import csv
n=5 # on initialise le nombre total de valeurs à ajouter à la liste de départ
#start=[-1.57,-1026.78,1.58,84.85,52.7,33.98,-620.61,123.32,20.02,106.98,118.58,29.5,59.54,87.72,53.48,123.32,69.56,1.58,9.22,3.16,72.2,4.74,101.71,81.69,18.45,86.43,63.1,4.98,97.38,3.32,122.4,16.06,17.72,69.09,3.32,14.94,-4369.78,1.66,-653.64,75.07,8.30,86.50,-1688.12,-1947.38,-760.32,-630.63,-1019.16,-945.00,1.66,61.47,-272.24,-544.48,1.66,48.96,71.81]
#start=[-14130.3,-9089.51,7850.25,7849.97,6280.09,1239.5,-8704.62,5469.92,2934.7,-158.1,422.26,19.5,16.34]
#start=[-4369.78,-1947.38,-1688.12,-1026.78,-1019.16,-945.00,-760.32,-653.64,-630.63,-620.61,-544.48,-272.24,123.32,123.32,122.4,118.58,106.98,101.71,97.38,87.72,86.50,86.43,84.85,81.69,75.07,72.2,71.81,69.56,69.09,63.1,61.47,59.54,53.48,52.7,48.96,33.98,29.5,20.02,18.45,17.72,16.06,14.94,9.22,8.30,4.98,4.74,3.32,3.32,3.16,1.66,1.66,1.66,1.58,1.58,-1.57]
#start=[-27255.90,4.58,27531.21,-0.05,-11061.87,-21.23,21.05,0.01,0.01,0.10,3360.13,-34.09,-9741.37,9738.76,-97.39,0.34,-0.18,0.14,-164.90,-325.55,43.59,-2149.28,2418.04,-24158.06,4643.46,-4635.20,0.01,-18.16,-8.26,-8.58]
#start=[2,3,-1,-9,10]
#values=[]
 
#start=[-0.53,-0.63,-0.53,-2.76,-0.7,3.98,13.11,-60.6,-70.20,-56.07,360.7,-54.3,-48.54,-36.15,-58.17,-370.70,4.44,18.02,9.75,-192.15,-980.64,-418.80,-370.27,-355.24,-271.20,-181.78,-645.48,-1659.24,-1282.68,-602.40,-558.15,-286.20,-264.00,12.34,621.78,-790.92,-1137.96,0.01,0.02]
start=[]
values=[]
#values=[27531.21,-27255.90,-24158.06,-11061.87,-9741.37,9738.76,4643.46,-4635.20,3360.13,2418.04,-2149.28,-325.55,-164.90,-97.39,43.59,-34.09,-21.23,21.05,-18.16,-8.58,-8.26,4.58,0.34,-0.18,0.14,0.10,-0.05,0.01,0.01,0.01]
#values=[-13321.27,8284.29,-5555.35,-5267.36,-4416.41,3952.43,3842.20,3520.36,3313.78,2918.83,2854.78,2763.20,2434.22,-2304.61,2210.5,2179.35,2070.25,1952.75,1902.88,-1597.39,1523.51,1487.83,1476.78,1436.60,1385.37,1347.80,1346.00,-1244.88,1240.98,1185.40,1097.74,1088.78,1085.92,-1062.07,975.48,-975,888.52,-792.57,732.00,720.26,-720.00,-720.00,-714.96,703.78,694.06,686.52,-679.77,656.12,647.68,600.03,576.63,568.11,533.85,-489.60,481.47,476.37,466.40,444.99,444.45,378.91,364.08,358.89,345.44,337.84,319.36,-302.40,297.6,297.57,288.82,285.38,266.21,242.66,224.79,218.38,183.71,162.62,158.3,158.09,155.95,147.98,127.73,109.90,105.85,-98.47,88.13,82.69,82.69,-78.02,73.78,70.19,69.09,56.39,56.14,51.12,51.12,44.80,-42.30,41.11,40.58,40.58,36.36,36.2,31.62,30.27,-28.38,22.13,20.03,19.58,17.39,17.39,17.39,16.34,15.78,15.23,14.23,14.23,-12.90,8.96,8.96,6.85,6.64,6.32,6.32,4.74,4.59,3.32,3.16,1.66,0.02]
results=[] # liste des résultats
index_utilises=[]
indices=[]
index_exclus=[]
SommeDesValeurs=0
Arret=True
Compteur=0
Codes=[]
iDepart=2
def combinaisons(n, p , i , k, s, c): # fonction récursive pour générer tous les groupes de p valeurs prises parmi n valeurs de l'ensemble
        global Arret
        if c_Valide(c):
                if (i < p):
                        if ((k + (p - i)) <= n):
                                for j in range(k + 1, n+1):
                                        #print("A")
                                        if Arret==True:
                                                break
                                        if not indices[j-1] in index_utilises:
                                                # appel récursif vers prochaine valeur du groupe                
                                                combinaisons(n, p, i + 1, j, s + values[j-1], c + str(j-1) + ',') # ajout de la valeur dans la somme s et dans le groupe c
 
                else:
                        if abs(s) <= 1e-03: # si la somme des valeurs du groupe vaut 0
                            print("B")
                            #results.append(c[0:len(c)-1]) # on ajoute un groupe de valeurs dans la liste results (exemple: (-1,2,1,2))
                            Trouve(c)
                        elif abs(s-SommeDesValeurs)<=1e-03:
                            print("C")
                            TrouveComplement(c)
 
def ChargerCSV(file,sep=";"):
        with open(file,newline="") as f:
                reader = csv.reader(f, delimiter=';', quotechar='|')
                r=list(reader)
                n=len(r)
 
                for i in range(1,n+1):
                        indices.append(i)
                        start.append(float(r[i-1][0].replace(",",".")))

def UpdateCSV(file,lig,col,val,sep=';'):
        with open(file,"r+",newline="") as f:
                r=csv.reader(f,delimiter=sep)
                lignes = list(r)
                try:
                        lignes[lig][col]=val
                        f.seek(0)
                        w = csv.writer(f,delimiter=sep)
                        w.writerows(lignes)
                        f.truncate()
                        return 0
                except:
                        return -1
#for i in range(-n,n,2): # on génère les valeurs de l'ensemble dans la liste values
        #if i!=0:
                #values.append(i) # ajoute une valeur dans la liste values
 
def Trouve(c):
        global Arret
        print(c[0:len(c)-1])
        o=c[0:len(c)-1].split(',')
        for a in map(lambda x:int(x),o):
            index_utilises.append(indices[a])
            Codes.append(tuple((indices[a],Compteur)))
        print(len(values)-len(index_utilises))
        print(Codes)
        Arret=True
 
def TrouveComplement(c):
        global Arret
        o=c[0:len(c)-1].split(',')
        x = map(lambda x: int(x),o)
        for i in range(len(start)):
                if not i in index_exclus and not i in index_utilises and not i in x:
                        index_utilises.append(i)
                        Codes.append(tuple((i,Compteur)))
        print(len(values)-len(index_utilises))
        print(Codes)
        Arret=True
 
def InitDeTout():
        try:
                global Arret
                global Compteur
                global SommeDesValeurs
                Compteur+=1
                Arret = False
                global n
                values.clear()
                indices.clear()
                Exclure_Hors_Limite()
                for i in range(len(start)):
                        if not i in index_utilises and not i in index_exclus :#and len(values)<30:
                            values.append(start[i])
                            indices.append(i)
                print(indices)
                n=len(values) # on évalue à nouveau le nombre total de valeurs contenues dans la liste de départ pour être sûr
                SommeDesValeurs=sum(values)
        except:
                print(sys.exc_info())
                x=input()
def A_Exclure(c):
        a=SommeNeg()
        b=SommePos()
        r=(c>0 and c+a>0) or (c<0 and c+b<0)
        #print(f"Test {c}:{r} , {a} et {b}")
        return r
 
def Exclure_Hors_Limite():                
        for i in range(len(start)):
                if not i in index_exclus and not i in index_utilises:
                    if A_Exclure(start[i])==True:
                        index_exclus.append(i)
 
def SommePos():
        r=0
        for i in range(len(start)):
                if not i in index_utilises and not i in index_exclus:
                        if start[i]>0:
                            r+=start[i]
        return r
 
def SommeNeg():
    r=0
    for i in range(len(start)):
        if not i in index_utilises and not i in index_exclus:
            if start[i]<0:
                r+=start[i]
    return r
 
def c_Valide(c):
        if c=="":
                return True
        #print(f"on teste {c}")
        o=c[0:len(c)-1].split(',')
 
        for a in o:
                #print("c")
                if indices[int(a)-1] in index_utilises:
                        return False
        return True
 

strpath=r"C:\Users\Jean-PhilippeAndre\Downloads\sommes_nulles\essai.csv"
ChargerCSV(strpath)
print (SommeNeg())        
print (SommePos())        
print(A_Exclure(start[0]))
while Arret==True:
        try:
                InitDeTout()
                print(values)
                print(n)
                print (f'début {Compteur}')
                print(datetime.datetime.now())
        except:
                print(sys.exc_info())
                x=input()
        try:
                for i in range(int((n+1)/3)+1,2,-1):#range(2,int((n+1)/2)+1): #for i in range(2,n+1): # gènère toutes les combinaisons : de combin(n,2) jusqu'à combin(n,n)
                        print(f"recherche des combinaisons de {i} composants")
                        if Arret==True:
                                iDepart=i
                                break
                        else:
                                #print("ICI")
                                combinaisons(n, i, 0, 0, 0, '') # appel de la fonction récursive pour générer les groupes de i valeurs prises dans n 
        except:
                print(sys.exc_info())
                x=input()
        print("fin")
        print(datetime.datetime.now())
        #for r in results:  # affiche toutes les combinaisons de combin(n,2) jusqu'à combin(n,n)
        #        print(r)
 
        print("index utilisés")
        print(index_utilises)
print("solution")
print("index utilisés")
print(index_utilises)
print(Codes)
for i in Codes:
        UpdateCSV(strpath,i[0],1,i[1])
x=input()
