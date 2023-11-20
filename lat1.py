import os


def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)
    

def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)


while(True):
    os.system('cls')

    print("===========================")
    print("Program Mengurutkan Data")
    print("Dengan Metode Bubble Short")
    print("===========================")


    bil1=int(input("Masukkan bilangan ke-1 : "))
    bil2=int(input("Masukkan bilangan ke-2 : "))
    bil3=int(input("Masukkan bilangan ke-3 : "))
    bil4=int(input("Masukkan bilangan ke-4 : "))
    bil5=int(input("Masukkan bilangan ke-5 : "))


    print("=========================")
    print("Pilihan metode pengurutan :")
    print("1.Sorting Ascending")
    print("2.Sorting Descending")


    bil=[bil1,bil2,bil3,bil4,bil5]
    

    pilih=input("Metode yang dipilih : ")
    print("=========================")

    print("Data sebelum diurutkan : ")
    print(bil)
    print('Nilai Maksimal : ',max(bil))
    print('Nilai Minimal : ',min(bil))
    print('Nilai Rerata : ',sum(bil)/len(bil))
    print("Data sesudah diurutkan : ")

 
    if pilih=="1":
        urutasc(bil)
    elif pilih=="2":
        urutdesc(bil)
    else:
        print("Pilihan tidak ada")

    menu=input("Kembali ke menu awal (Y/N)?")

    if menu=="N" or menu=="n":
        print("Selesai, Terimakasih!")
        break
    elif menu!="Y" and menu!="y":
        print("Pilihan tidak ada!")
        break
