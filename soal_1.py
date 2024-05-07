bilangan_pertama = int(input("input bilangan pertama : "))
bilangan_kedua = int(input("input bilangan kedua : "))

print('1. penjumlahan')
print('2. pengurangan')
print('3. sisa bagi')

pilih = int(input("pilih operasi : "))
if pilih == 1:
    hasil = bilangan_pertama + bilangan_kedua
    print (f'{bilangan_pertama} + {bilangan_kedua} = {hasil}')
elif pilih == 2:
    hasil = bilangan_pertama - bilangan_kedua
    print (f'{bilangan_pertama} - {bilangan_kedua} = {hasil}')
elif pilih == 3:
    hasil = bilangan_pertama % bilangan_kedua 
    print (f'{bilangan_pertama} % {bilangan_kedua} = {hasil}')