def rumus_1(n,d):
    print(f"GRAF BER-ORDE :{n}: | BER-DERAJAT KELUAR :{d}:")

    #membuat label untuk titik dan yang dimasukkan ke graf
    nodes = []
    for i in range(0,n):
        nodes.append(i)
    print("label titik ->", nodes)

    #menentukan hasil relasi titik dengan rumus
    kotak = []
    for j in range(0,d) : # sebagai i
        for i in range(0,n):
            titik_keluar = (d*i) + (j % n) #ini rumusnya
            while titik_keluar >= n :
                titik_keluar -= n
            while titik_keluar < 0 :
                titik_keluar += n
            kotak.append(titik_keluar)

    #memasukkan label ke variabel yang digunakan untuk memunculkan graf
    for j in range(0,d):
        for i in nodes:
            kotak.append(i)

    #memecah variabel memunculkan graf menjadi tuple-tuple 2 titik yang akan menjadi sisi
    edge = list(zip(kotak[:(len(kotak))//2], kotak[(len(kotak))//2:]))
    print(f"pemetaan hasil graf :  \n{edge}")

    #munculkan graf
    visualisasi_graf(nodes,edge)

def rumus_2(n,d):
    print(f"GRAF BER-ORDE :{n}: | BER-DERAJAT KELUAR :{d}:")

    #membuat label untuk titik dan yang dimasukkan ke graf
    nodes = []
    for i in range(0,n):
        nodes.append(i)
    print("label titik ->", nodes)

    #menentukan hasil relasi titik dengan rumus
    kotak = []
    for j in range(0,d) : # sebagai i
        for i in range(0,n):
            titik_keluar = (d*i) - (j % n) #ini rumusnya
            while titik_keluar >= n :
                titik_keluar -= n
            while titik_keluar < 0 :
                titik_keluar += n
            kotak.append(titik_keluar)

    #memasukkan label ke variabel yang digunakan untuk memunculkan graf
    for j in range(0,d):
        for i in nodes:
            kotak.append(i)

    #memecah variabel memunculkan graf menjadi tuple-tuple 2 titik yang akan menjadi sisi
    edge = list(zip(kotak[:(len(kotak))//2], kotak[(len(kotak))//2:]))
    print(f"pemetaan hasil graf :  \n{edge}")

    #munculkan graf
    visualisasi_graf(nodes,edge)

def rumus_3(n,d):
    print(f"GRAF BER-ORDE :{n}: | BER-DERAJAT KELUAR :{d}:")

    #membuat label untuk titik dan yang dimasukkan ke graf
    nodes = []
    for i in range(0,n):
        nodes.append(i)
    print("label titik ->", nodes)

    #menentukan hasil relasi titik dengan rumus
    kotak = []
    for j in range(1,d+1) : # sebagai i
        for i in range(0,n):
            titik_keluar = ((-d)*i) - (j % n) #ini rumus
            while titik_keluar >= n :
                titik_keluar -= n
            while titik_keluar < 0 :
                titik_keluar += n
            kotak.append(titik_keluar)

    #memasukkan label ke variabel yang digunakan untuk memunculkan graf
    for j in range(1,d+1):
        for i in nodes:
            kotak.append(i)

    #memecah variabel memunculkan graf menjadi tuple-tuple 2 titik yang akan menjadi sisi
    edge = list(zip(kotak[:(len(kotak))//2], kotak[(len(kotak))//2:]))
    print(f"pemetaan hasil graf :  \n{edge}")

    #munculkan graf
    visualisasi_graf(nodes,edge)

def rumus_4(n,d):
    print(f"GRAF BER-ORDE :{n}: | BER-DERAJAT KELUAR :{d}:")

    #membuat label untuk titik dan yang dimasukkan ke graf
    nodes = []
    for i in range(0,n):
        nodes.append(i)
    print("label titik ->", nodes)

    #menentukan hasil relasi titik dengan rumus
    kotak = []
    for j in range(1,d+1) : # sebagai i
        for i in range(0,n):
            titik_keluar = ((-d)*i) + (j % n) #ini rumus
            while titik_keluar >= n :
                titik_keluar -= n
            while titik_keluar < 0 :
                titik_keluar += n
            kotak.append(titik_keluar)

    #memasukkan label ke variabel yang digunakan untuk memunculkan graf
    for j in range(1,d+1):
        for i in nodes:
            kotak.append(i)

    #memecah variabel memunculkan graf menjadi tuple-tuple 2 titik yang akan menjadi sisi
    edge = list(zip(kotak[:(len(kotak))//2], kotak[(len(kotak))//2:]))
    print(f"pemetaan hasil graf :  \n{edge}")

    #munculkan graf
    visualisasi_graf(nodes,edge)

def visualisasi_graf(nodes, edge):
    # Buat objek graf
    G = nx.DiGraph()  # Menggunakan DiGraph untuk membuat graf menjadi berarah

    # Tambahkan node ke graf
    G.add_nodes_from(nodes)

    # Tukar posisi angka pada tuple edges untuk membuat arah panah menjadi terbalik
    edge = [(destination, source) for (source, destination) in edge]

    # Tambahkan edge ke graf
    G.add_edges_from(edge)

    # Visualisasikan graf dengan panah (graf berarah)
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', arrows=True)
    plt.title("Contoh Visualisasi Graf Berarah")
    plt.show()

# -----------------------------

import os
import networkx as nx
import matplotlib.pyplot as plt

run = True
while run:
    os.system("cls")

    print("""
    SELAMAT DATANG DI PROGRAM KONSTRUKSI GRAF :3

    menu :[1] Generalisasi Graf Berarah De Brujin rumus positif (+)
          [2] Generalisasi Graf Berarah De Brujin rumus negatif (-)
          [3] Generalisasi Graf Berarah Kautz rumus positif (+)
          [4] Generalisasi Graf Berarah Kautz rumus negatif (-)
          [5] EXIT
    """)

    selection = input("Ketik menu yang anda inginkan : ")

    if selection == "1" :
        n = int(input("Masukkan jumlah orde : "))
        d = int(input("Masukkan derajat keluar graf : "))

        try :
            os.system("cls")
            rumus_1(n,d)
            input("\nTekan [enter] untuk kembali ke menu")
        except :
            input("\nKesalahan input, silahkan coba lagi")

    elif selection == "2" :
        n = int(input("Masukkan jumlah orde : "))
        d = int(input("Masukkan derajat keluar graf : "))

        try :
            os.system("cls")
            rumus_2(n,d)
            input("\nTekan [enter] untuk kembali ke menu")
        except :
            input("\nKesalahan input, silahkan coba lagi")
    elif selection == "3" :
        n = int(input("Masukkan jumlah orde : "))
        d = int(input("Masukkan derajat keluar graf : "))

        try :
            os.system("cls")
            rumus_3(n,d)
            input("\nTekan [enter] untuk kembali ke menu")
        except :
            input("\nKesalahan input, silahkan coba lagi")
    elif selection == "4" :
        n = int(input("Masukkan jumlah orde : "))
        d = int(input("Masukkan derajat keluar graf : "))

        try :
            os.system("cls")
            rumus_4(n,d)
            input("\nTekan [enter] untuk kembali ke menu")
        except :
            input("\nKesalahan input, silahkan coba lagi")
    elif selection == "5":
        break
    else:
        run = True

# klik "run anyway" bila ada peringatan keamanan
