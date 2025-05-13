# CAPSTONE PROJECT

# PERUSAHAAN "STRAIGHT EVENT ORGANIZER"
# NAMA : GREGORIUS DANIEL

def mainMenu() : 
    print('''
Selamat datang di STRAIGHT EVENT ORGANIZER \n
Daftar Menu : \n
1. Data Karyawan \n
2. Create Data Karyawan \n
3. Edit Data Karyawan \n
4. Hapus Data Karyawan \n
5. Exit Program \n''')

# Data Karyawan
data_table = {
    'Nomor' : [1, 2, 3, 4, 5],
    'Nama' : ['Agus Murjianto', 'Florencia Indah', 'Fransiskus Pratama', 'Rexy Aditya', 'Stevanus Hanafi'],
    'employee_id' : ['EO01', 'EO02', 'EO03', 'EO04', 'EO05'],
    'jenis_kelamin' : ['L', 'P', 'L', 'L', 'L'],
    'umur_karyawan' : [30, 25, 27, 28, 29], 
    'tingkat_jabatan' : ['Staff', 'Staff', 'Staff', 'Manager', 'Manager'],
    'gaji_karyawan' : [5000000, 4000000, 4500000, 6000000, 7000000]
    }
def dataKaryawan() :
    print(f'''Data Karyawan : \n
{'Nomor':<6} | {'Nama':<20} | {'employee_id':<15} | {'jenis_kelamin':<15} | {'umur_karyawan':<15} | {'tingkat_jabatan':<15} | {'gaji_karyawan':<15}''')
    print('-'*118)
    for i in range(len(data_table['Nomor'])):
        print(f'''{data_table['Nomor'][i]:<6} | {data_table['Nama'][i]:<20} | {data_table['employee_id'][i]:<15} | {data_table['jenis_kelamin'][i]:<15} | {data_table['umur_karyawan'][i]:<15} | {data_table['tingkat_jabatan'][i]:<15} | {data_table['gaji_karyawan'][i]:<15}''')

# Menambahkan Data Karyawan
def tambahDataKaryawan() :
    print('''
    Tambah Data Karyawan : \n
    ''')
    nama = input('Masukkan Nama Karyawan : ')
    employee_id = input('Masukkan employee_id Karyawan : ')
    jenis_kelamin = input('Masukkan Jenis Kelamin Karyawan (L/P) : ')
    umur_karyawan = int(input('Masukkan Umur Karyawan : '))
    tingkat_jabatan = input('Masukkan Tingkat Jabatan Karyawan : ')
    gaji_karyawan = int(input('Masukkan Gaji Karyawan : '))
    
    data_table['Nomor'].append(len(data_table['Nomor']) + 1)
    data_table['Nama'].append(nama)
    data_table['employee_id'].append(employee_id)
    data_table['jenis_kelamin'].append(jenis_kelamin)
    data_table['umur_karyawan'].append(umur_karyawan)
    data_table['tingkat_jabatan'].append(tingkat_jabatan)
    data_table['gaji_karyawan'].append(gaji_karyawan)

    print('\nData berhasil ditambahkan!\n')
    dataKaryawan()

# Mengubah Data Karyawan
def ubahDataKaryawan() :
    print('Ubah Data Karyawan \n')
    dataKaryawan()
    print('\n')
    while True:
        dataID_input = input('Masukkan employee_id Karyawan yang ingin diubah: ')
        if dataID_input in data_table['employee_id']:
            i = data_table['employee_id'].index(dataID_input)
            print(f'''\nData Karyawan yang dipilih:
{'Nomor':<6} | {'Nama':<20} | {'employee_id':<15} | {'jenis_kelamin':<15} | {'umur_karyawan':<15} | {'tingkat_jabatan':<15} | {'gaji_karyawan':<15}''')
            print('-' * 118)
            print(f"{data_table['Nomor'][i]:<6} | {data_table['Nama'][i]:<20} | {data_table['employee_id'][i]:<15} | {data_table['jenis_kelamin'][i]:<15} | {data_table['umur_karyawan'][i]:<15} | {data_table['tingkat_jabatan'][i]:<15} | {data_table['gaji_karyawan'][i]:<15} \n")
            bagian_ubah = input('Apa yang ingin diubah? Pilih salah satu (Nama/employee_id/jenis_kelamin/umur_karyawan/tingkat_jabatan/gaji_karyawan): ')
            if bagian_ubah in data_table:
                nilai_baru = input(f'Masukkan {bagian_ubah} yang baru: ')
                data_table[bagian_ubah][i] = nilai_baru
                print('\nData berhasil diubah!\n')
                dataKaryawan()
                break
            else:
                print('Bagian yang dimasukkan tidak valid.\n')
                input('Apakah anda ingin mencoba lagi? (y/n) : ')
                if input().lower() == 'n':
                    print('Terima kasih telah menggunakan program ini.')
                    break
                else:
                    print('Silakan coba lagi.\n')
        else:
            print('employee_id tidak ditemukan.\n')
            respon = input('Apakah anda ingin mencoba lagi? (y/n) : ')
            if respon.lower() == 'n':
                print('Terima kasih telah menggunakan program ini.')
                break
            else: 
                respon.lower() == 'y'
                print('Silakan coba lagi.\n')

# Menghapus Data Karyawan
def hapusDataKaryawan() :
    print('Hapus Data Karyawan \n')
    dataKaryawan()
    print('\n')
    while True:
        dataID_input = input('Masukkan employee_id Karyawan yang ingin dihapus: ')
        if dataID_input in data_table['employee_id']:
            i = data_table['employee_id'].index(dataID_input)
            del data_table['Nomor'][i]
            del data_table['Nama'][i]
            del data_table['employee_id'][i]
            del data_table['jenis_kelamin'][i]
            del data_table['umur_karyawan'][i]
            del data_table['tingkat_jabatan'][i]
            del data_table['gaji_karyawan'][i]
            print('\nData berhasil dihapus!\n')
            dataKaryawan()
            break
        else:
            print('employee_id tidak ditemukan.\n')
            respon = input('apakah anda ingin mencoba lagi? (y/n) : ')
            if respon.lower() == 'n':
                print('Terima kasih telah menggunakan program ini.')
                break
            else:
                respon.lower() == 'y'
                print('Silakan coba lagi.\n')

                

# Main Program
while True:
    mainMenu()
    menu = int(input('Masukkan pilihan menu (1-4) : '))
    
    if menu == 1:
        dataKaryawan()
    elif menu == 2:
        tambahDataKaryawan()
    elif menu == 3:
        ubahDataKaryawan()
    elif menu == 4:
        hapusDataKaryawan()
    elif menu == 5:
        print('Terima kasih telah menggunakan program ini.')
        break
    else:
        print('Pilihan tidak valid. Silakan coba lagi.\n')