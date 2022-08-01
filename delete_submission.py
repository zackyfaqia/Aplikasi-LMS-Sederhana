dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113','114': 'Ini jawaban mahasiswa 114'},
 2: {'113' : 'Ini jawaban mahasiswa 113','114': 'Ini jawaban mahasiswa 114'}}

list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
 {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}]


dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
 1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
 2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}}

                     
def delete_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Hapus assignment tersebut.
    '''
    print('-----------------Fungsi "delete_submission" dijalankan-----------------')
    
    for i in range (2):
        print(f"{i+1}: {list_topic [i] ['Title']} ")

    topik = int(input("Masukan nomor topic: "))

    print('ID \t | Title \t\t | Type \t | Description')
    print('-' *70)

    for k,v in list_topic [topik - 1].items():
        if k == 'Activities':
            for i in v:
                for k,v in dict_activity [i].items():
                    if k == 'Type' and v == 'assignment':
                        print(f"{i} \t | {dict_activity [i] ['Title']} \t | {dict_activity [i] ['Type']} \t | {dict_activity [i] ['Description']}")

    id = int(input("Masukkan ID Assignment: "))
    dict_submission [id].pop (nim)
    print ('''Delete Berhasil!
        

        
Tekan Enter untuk kembali ke menu utama...''')


delete_submission(dict_submission, list_topic, dict_activity, '114')



