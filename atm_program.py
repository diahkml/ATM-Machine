# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:26:14 2020

@author: ASUS
"""
from customer import Customer
import random
import datetime

nid = Customer(1,1,1)

i=1
a = 'Selamat Datang di ATM Bersama'
b = 'Untuk berbagai transaksi yang aman, ekonomis dan Mudah'
titik = '------------------------------------------------------------------------------------------------'
print(a.center(100))
print(b.center(100))
print(titik)
            
while i <= 3:
    print(titik)
    print('Demi Keamanan dan Kenyamanan, Silakan Ganti Pin Anda Secara Berkala')
    inputuser=int(input('Masukkan pin ATM Anda: '))    
    print(titik)
    if inputuser == nid.getCustPin() :
        while True :            
            print(titik)
            print('Pilih Bahasa'.center(100))
            print('--------------------'.center(100))
            print('Language Preference'.center(100))
            print('1. INDONESIA')
            print('2. ENGLISH')
            pilihbahasa = int(input('Masukkan pilihan anda : '))
            print(titik)
            if pilihbahasa == 1 :
                print(titik)
                print('Menu Penarikan Cepat'.center(100))
                print('Silakan Pilih Jumlah Penarikan(Pilih "Menu Lain" Jika ingin Cetak Receipt)'.center(100))
                print('1. 50.000')
                print('2. 200.000')
                print('3. 500.000')
                print('4. 1.000.000')
                print('5. Jumlah Lain')
                print('6. Menu Lainnya')
                pilihpenarikan = int(input('Masukkan pilihan anda : '))
                print(titik)
                if pilihpenarikan == 1:
                    ambil = 50000
                    print(nid.Debet(ambil))
                elif pilihpenarikan == 2:
                    ambil = 200000
                    print(nid.Debet(ambil))
                elif pilihpenarikan == 3:
                    ambil = 500000
                    print(nid.Debet(ambil))
                elif pilihpenarikan == 4:
                    ambil = 1000000
                    print(nid.Debet(ambil))
                elif pilihpenarikan == 5:
                    print('Tarik Tunai'.center(100))
                    print('Masukkan Jumlah Penarikan Tunai yang Anda Ingin(Dalam Kelipatan RP 50.000) Maksimal Rp 1.250.000')
                    ambil = int(input('Masukkan Jumlah Uang : '))
                    if ambil % 50000 == 0 and ambil <= 1250000:
                        print('Penarikan Uang Berhasil')
                        print(nid.Debet(ambil))
                    else :
                        print('Penarikan Tunai Gagal.')
                        print('Ulangi kembali dengan Jumlah Penarikan dalam Kelipatan RP. 50.000 dan Maksimal Rp 1.250.000')
                else :
                    print(titik)
                    print('Pilih Transaksi yang Anda Inginkan'.center(100))
                    print('1. Informasi Saldo')
                    print('2. Penarikan Tunai')
                    print('3. Setor Tunai')
                    print('4. Ganti Pin')
                    print('5. Keluar')
                    pilihmenu=int(input('Masukkan Pilihan Anda : '))
                    print(titik)
                    if pilihmenu == 1 :
                        print('Informasi Saldo'.center(100))
                        print('Saldo Tabungan Anda Saat Ini : ' + str(nid.getCustBalance()))
                    elif pilihmenu == 2:
                        print('Masukkan Jumlah Penarikan Tunai yang Anda Ingin(Dalam Kelipatan RP 50.000) Maksimal Rp 1.250.000')
                        ambil = int(input('Masukkan Jumlah Uang : '))
                        if ambil % 50000 == 0 and ambil <= 1250000:
                            print('Penarikan Tunai Berhasil')
                            print(nid.Debet(ambil))
                        else :
                            print('Penarikan Tunai Gagal.')
                            print('Ulangi kembali dengan Jumlah Penarikan dalam Kelipatan RP. 50.000 dan Maksimal Rp 1.250.000')
                    elif pilihmenu == 3:
                        print('Transaksi Setor Tunai'.center(100))
                        print('Mesin ini Menerima Uang Tunai dengan Denominasi : ')
                        print('Rp 50.000')
                        print('Rp 100.000')
                        print('Mohon Perhatian Untuk : ')
                        print('- Memastikan Denominasi Uang')
                        print('- Merapikan Uang Anda')
                        lanjut=input('Silakan Tekan "Y" untuk Melanjutkan Proses Deposit : ')
                        if lanjut == 'Y' :
                            print(titik)
                            print('SETORAN TUNAI'.center(100))
                            nabung = int(input('Silakan Masukkan Jumlah Uang yang Akan Disetor :'))
                            tabungan = nid.Simpan(nabung)
                            print('Informasi Saldo : ' + str(tabungan))
                        else :
                            break
                    elif pilihmenu == 4 :
                        print('Ganti Pin'.center(100))
                        j=1
                        while True :
                            pinlama = int(input('Masukkan Pin Lama :'))
                            if pinlama == nid.getCustPin() :
                                pinbaru = int(input('Masukkan Pin Baru : '))
                                if pinbaru != pinlama :
                                    pin = pinbaru
                                    print('Pin Berhasil Diubah')
                                    break
                                else :
                                    print('Pin Tidak Berubah. Silakan Ulangi Kembali.')
                            else :
                                print('Pin Salah. Silakan Ulangi Kembali')  
                                if j == 3 :
                                    print('Kartu ATM error')
                                    print('Anda Salah Memasukkan Pin Lama Sebanyak 3 Kali')
                                    break
                                j += 1
                    elif pilihmenu == 5 :
                        norec = random.randrange(100000,1000000)
                        tgl = datetime.datetime.now()
                        print('Struk ATM'.center(100))
                        print('Tanggal : ' + tgl.strftime("%x"))
                        print('Waktu : ' + tgl.strftime("%X"))
                        print('Lokasi : Samarinda')                        
                        print('Record No. : ' + str(norec))
                        print('Informasi Saldo : ' + str(nid.getCustBalance()))
                    else :
                        print('Error. Silakan Ulangi Kembali')                        
            else :
                print(titik)
                print('Quick Withdrawal Menu'.center(100))
                print('Please Select a Withdrawal Amount(Select "Others" If You Want to Print Receipt)'.center(100))
                print('1. 50.000')
                print('2. 200.000')
                print('3. 500.000')
                print('4. 1.000.000')
                print('5. Other Cash Withdrawal ')
                print('6. Others')
                pilihpenarikan = int(input('Enter Your Choice: '))
                print(titik)
                if pilihpenarikan == 1:
                    ambil = 50000
                    print(nid.Withdrawal(ambil))
                elif pilihpenarikan == 2:
                    ambil = 200000
                    print(nid.Withdrawal(ambil))
                elif pilihpenarikan == 3:
                    ambil = 500000
                    print(nid.Withdrawal(ambil))
                elif pilihpenarikan == 4:
                    ambil = 1000000
                    print(nid.Withdrawal(ambil))
                elif pilihpenarikan == 5:
                    print('Cash Withdrawal'.center(100))
                    print('Withdrawal Amount (Denomination RP 50.000) Maximum Amount For Each Withdrawal Rp 1.250.000')
                    ambil = int(input('Enter the Amount of Money : '))
                    if ambil % 50000 == 0 and ambil <= 1250000:
                        print('Successful Cash Withdrawal')
                        print(nid.Withdrawal(ambil))
                    else :
                        print('Failed Cash Withdrawal')
                        print('Repeat Back with the Withdrawal Amount(Denomination RP. 50.000) Maximum Amount Rp 1.250.000')
                else :
                    print(titik)
                    print('Select the Transaction'.center(100))
                    print('1. Balance Information')
                    print('2. Cash Withdrawal')
                    print('3. Cash Deposit')
                    print('4. Change Pin')
                    print('5. Exit')
                    pilihmenu=int(input('Enter Your Choice : '))
                    print(titik)
                    if pilihmenu == 1 :
                        print('Balance Information'.center(100))
                        print('Your Current Balance : ' + str(nid.getCustBalance()))
                    elif pilihmenu == 2:
                        print('Cash Withdrawal Transactions'.center(100))
                        print('Withdrawal Amount (Denomination RP 50.000) Maximum Amount For Each Withdrawal Rp 1.250.000')
                        ambil = int(input('Enter the Amount of Money : '))
                        if ambil % 50000 == 0 and ambil <= 1250000:
                            print('Successful Cash Withdrawal')
                            print(nid.Withdrawal(ambil))
                        else :
                            print('Failed Cash Withdrawal')
                            print('Repeat Back with the Withdrawal Amount(Denomination RP. 50.000) Maximum Amount Rp 1.250.000')
                    elif pilihmenu == 3:
                        print('Cash Deposit Transactions'.center(100))
                        print('This Machine Accepts Money in Denominations: ')
                        print('Rp 50.000')
                        print('Rp 100.000')
                        print('Please Attention For : ')
                        print('- Ensuring Money Denomination')
                        print('- Clean Up Your Money')
                        lanjut=input('Please Press "Y" to Continue the Deposit Process : ')
                        if lanjut == 'Y' :
                            print(titik)
                            print('Cash Deposit'.center(100))
                            nabung = int(input('Enter the Amount of Money to be Deposited :'))
                            tabungan = nid.Simpan(nabung)
                            print('Your Current Balance : ' + str(tabungan))
                        else :
                            break
                    elif pilihmenu == 4 :
                        print('Change Pin'.center(100))
                        j=1
                        while True :
                            pinlama = int(input('Enter The Old Pin :'))
                            if pinlama == nid.getCustPin() :
                                pinbaru = int(input('Enter a New Pin : '))
                                if pinbaru != pinlama :
                                    pin = pinbaru
                                    print('Pin Changed Successfully')
                                    break
                                else :
                                    print('Pin Not Changed. Please Try Again.')
                            else :
                                print('Incorrect Pin. Please Try Again')  
                                if j == 3 :
                                    print('ATM Card Error')
                                    print('You Entered the Wrong Old Pin 3 Times')
                                    break
                                j += 1
                    elif pilihmenu == 5 :
                        norec = random.randrange(100000,1000000)
                        tgl = datetime.datetime.now()
                        print('ATM Receipt'.center(100))
                        print('Date : ' + tgl.strftime("%x"))
                        print('Time : ' + tgl.strftime("%X"))
                        print('Location : Samarinda')                        
                        print('Record No. : ' + str(norec))
                        print('Balance Information : ' + str(nid.getCustBalance()))
                    else :
                        print('Error. Please Try Again')
                        
            print(titik)
            print(titik)
            if pilihbahasa == 1 :
                print('Apakah Anda ingin Mengulang Transaksi ?')
                pilihan=input('Tekan "Y" jika Ya atau Tekan "T" jika Tidak : ')
            else : 
                print('Do You Want to Repeat Transactions ?')               
                pilihan=input('Press "Y" If Yes or Press "T" If Not : ')
                print(titik)
                
            if(pilihan == 'Y') :
                continue
            else :
                break
        break
    else :
        print('Pin Anda Salah'.center(100))
        print('-------------'.center(100))
        print('Incorect Pin'.center(100))
    
    if i==3 :
        print('Kartu ATM Diblokir')
        print('Anda Salah Memasukkan Pin Sebanyak 3 Kali')
        print('Silakan menghubungi Customer Service Terdekat')
        print('---------------------------------------------')
        print('ATM Card Blocked')
        print('You Entered the Wrong Old Pin 3 Times')
        print('Please Contact the Nearest Customer Service')
    i += 1
    