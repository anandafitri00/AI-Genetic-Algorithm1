#generate angka random dari komputer untuk menghasilkan kromosom

def random (banyakbiner):
        import random
        listindividu = []
        for i in range (banyakbiner) :        
                y = random.randrange(0, 2)
                listindividu.append(y)
        return listindividu

#generate angka random dari komputer untuk mengetahui indeks ke berapa yang akan di crossover 

def randomindex (randomslice) :
        import random
        listrandomslice = []
        for i in range (randomslice) :
                p = random.randrange(1,7)
        return p

populasi = 4
banyakbiner = 6
randomslice = 1
generation = 1
i = 1
listkromosom =[]
listfitness =[]
listpeluang =[]
a = 0.00000000000000000000000000000000000000000000000001
totalprobabilitas = 0
generasi = 4
parent1 = []
parent2 = []
duplikatparent1 = []
duplikatparent2 = []
letakparent1 = 0
letakparent2 = 0

#mengubah kromosom biner menjadi angka real dengan rumus
#mendapatkan fitnes dari kromosom dalam bentuk angka real
#menduplikasi angka yang telah keluar agar bisa diakses untuk generasi yang selanjutnya

for i in range (populasi) :
        A=random(banyakbiner)
        print("Kromosom ke-", i+1, " = ", A)
        x1= -3+((6/0.875)*((A[0]*0.5)+(A[1]*0.25)+(A[3]*0.125)))
        x2= -2+((4/0.875)*((A[3]*0.5)+(A[4]*0.25)+(A[5]*0.125)))
        fungsi = ((4-(2*(x1**2)+(x1**4/3))))*x1+(x1*x2)+((-4+(4*x2**2))*x2**2)
        fitness = (1/(fungsi+a))
        print("Phenothype x1 ke- ", i+1, " = ", x1)
        print("Phenothype x2 ke- ", i+1, " = ", x2)
        print("Fitness individu ke- ", i+1, " = ", fitness)
        listkromosom.append(A)
        print("\n")
        totalprobabilitas = totalprobabilitas+fitness
        listfitness.append(fitness)

#membagi fitness dengan total probabilitas agar dapat memilih parent

for i in range (len(listkromosom)) :
        peluangindividu = listfitness[i]/totalprobabilitas
        listpeluang.append(peluangindividu)

print("Total Probabilitas = ", totalprobabilitas)
print("Hasil probabilitas Per-kromosom = ", listpeluang)
print('\n')

#perulangan untuk mencari parent 1
#perulangan untuk mencari dimana letak parent 1

parent1 = max(listpeluang)
print('Nilai Parent 1 = ', parent1)

for i in range (len(listpeluang)) :
        if listpeluang[i] == max(listpeluang) :
                letakparent1 = i+1
                
print("Letak Parent 1 ada di list ke- ", letakparent1)

#perulangan untuk mencari parent 2
#perulangan untuk mencari dimana letak parent 2

maxpeluang = listpeluang[1]
for i in range (len(listpeluang)) :
        if listpeluang[i]>= maxpeluang :
                if len(listpeluang) == len(listpeluang)-2 :
                        maxpeluang = listpeluang[i-1]
        letakparent2 = i-1
        
print('Nilai Parent 2 = ', maxpeluang)
print("Letak Parent 2 ada di list ke- ", letakparent2)

#parent terpilih

for i in range (letakparent1) :
        duplikatparent1.append(listkromosom)

for i in range (letakparent2) :
        duplikatparent2.append(listkromosom)
        
print('\n')


#merandom list keberapa yang ingin di slice
#proses crossover

F = randomindex(randomslice)
print('crossover pada indeks ke-', F)
print('Hasil crossover = ')
listanak1= []
listanak2= []

otwanak11 = listkromosom[letakparent1][F:]
otwanak12 = listkromosom[letakparent2][:F]
otwanak21 = listkromosom[letakparent1][:F]
otwanak22 = listkromosom[letakparent2][F:]


listanak1 = otwanak11+otwanak12
listanak2 = otwanak21+otwanak22

print(listanak1)
print(listanak2)
print('\n')


#mutasi pada anak
import random
peluangmutasi = 1/banyakbiner
for i in range (banyakbiner) :
        nilairandom= random.random()
        if nilairandom>=0 and nilairandom<=peluangmutasi :
                if listanak1[i]==0 :
                        listanak1[i]=1
                else :
                        listanak1[i]=0

print('Mutasi pada anak 1 = ', listanak1)

for i in range (banyakbiner) :
        nilairandom= random.random()
        if nilairandom>=0 and nilairandom<=1 :
                        if listanak2[i]==0 :
                                listanak2[i]=1
                        else :
                                listanak2[i]=0
                                
print('Mutasi pada anak 2 = ', listanak2)


        

#mengganti parent dengan anak

listkromosom.pop(letakparent1)
listkromosom.pop(letakparent2)
listkromosom.append(listanak1)
listkromosom.append(listanak2)

print('List kromosom generasi selanjutnya adalah')
print(listkromosom)
print("\n")

listfitness.clear()
listpeluang.clear()

#pergantian generasi

def purapura (banyakbiner):
        B=0
        for i in range (banyakbiner) :
                B=B+1
        return listkromosom

Z=purapura(banyakbiner)
for i in range (generation):
        print("GENERASI KE-",(i+1))
        print('\n')
        for i in range (populasi) :
                print("Kromosom ke-", i+1, " = ", Z[i])
                x1= -3+((6/0.875)*((Z[i][0]*0.5)+(Z[i][1]*0.25)+(Z[i][3]*0.125)))
                x2= -2+((4/0.875)*((Z[i][3]*0.5)+(Z[i][4]*0.25)+(Z[i][5]*0.125)))
                fungsi = ((4-(2*(x1**2)+(x1**4/3))))*x1+(x1*x2)+((-4+(4*x2**2))*x2**2)
                fitness = (1/(fungsi+a))
                print("Phenothype x1 ke- ", i+1, " = ", x1)
                print("Phenothype x2 ke- ", i+1, " = ", x2)
                print("Fitness individu ke- ", i+1, " = ", fitness)
                print("\n")
                totalprobabilitas = totalprobabilitas+fitness
                listfitness.append(fitness)
                
        for i in range (len(listkromosom)) :
                peluangindividu = listfitness[i]/totalprobabilitas
                listpeluang.append(peluangindividu)
        print("Total Probabilitas = ", totalprobabilitas)
        print("Hasil probabilitas Per-kromosom = ", listpeluang)
        print('\n')

        parent1 = max(listpeluang)
        print('Nilai Parent 1 = ', parent1)

        for i in range (len(listpeluang)) :
                if listpeluang[i] == max(listpeluang) :
                        letakparent1 = i+1
                        
        print("Letak Parent 1 ada di list ke- ", letakparent1)

        maxpeluang = listpeluang[1]
        for i in range (len(listpeluang)) :
                if listpeluang[i]>= maxpeluang :
                        if len(listpeluang) == len(listpeluang)-2 :
                                maxpeluang = listpeluang[i-1]
                letakparent2 = i-1
                
        print('Nilai Parent 2 = ', maxpeluang)
        print("Letak Parent 2 ada di list ke- ", letakparent2)



        F = randomindex(randomslice)
        print('crossover pada indeks ke-', F)
        print('Hasil crossover = ')

        otwanak11 = listkromosom[letakparent1][F:]
        otwanak12 = listkromosom[letakparent2][:F]
        otwanak21 = listkromosom[letakparent1][:F]
        otwanak22 = listkromosom[letakparent2][F:]

        listanak1 = otwanak11+otwanak12
        listanak2 = otwanak21+otwanak22

        print(listanak1)
        print(listanak2)
        print('\n')

        import random
        peluangmutasi = 1/banyakbiner
        for i in range (banyakbiner) :
                nilairandom= random.random()
                if nilairandom>=0 and nilairandom<=peluangmutasi :
                        if listanak1[i]==0 :
                                listanak1[i]=1
                        else :
                                listanak1[i]=0

        print('Mutasi pada anak 1 = ', listanak1)

        for i in range (banyakbiner) :
                nilairandom= random.random()
                if nilairandom>=0 and nilairandom<=1 :
                                if listanak2[i]==0 :
                                        listanak2[i]=1
                                else :
                                        listanak2[i]=0
                                        
        print('Mutasi pada anak 2 = ', listanak2)
        listkromosom.pop(letakparent1)
        listkromosom.pop(letakparent2)
        listkromosom.append(listanak1)
        listkromosom.append(listanak2)

        print('List kromosom generasi selanjutnya adalah')
        print(listkromosom)
        print("\n")


finalfit = min(listfitness)
letakfitnessfinal = 0
for i in range (len(listfitness)) :
                if listpeluang[i] == min(listpeluang) :
                        letakfitnessfinal = i+1
print('KESIMPULAN :')
print('Dengan Fitness = ', finalfit)
print('sehingga adalah kromosom terbaik')
print('Jatuh pada kromosom ke - ', letakfitnessfinal)
print('dengan x1 = ', listkromosom[letakfitnessfinal-1][0:3])
print('dengan x2 = ', listkromosom[letakfitnessfinal][3:6])

#Sebelumnya mohon maaf, didalam program ini masih terdapat banyak bug, sehingga apabila error mohon dicoba run kemabali