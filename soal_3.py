barang = str(input('masukan nama barang = '))
barang2 = str(input('masukan nama barang = '))
jumlah_barang = int(input('masukan jumlah barang = '))
jumlah_barang2 = int(input('masukan jumlah barang = '))
harga_barang = int(input('masukan harga barang = '))
harga_barang2 = int(input('masukan harga barang = '))
harga1 = harga_barang * jumlah_barang
harga2 = harga_barang2 * jumlah_barang2
total_harga = harga1 + harga2
print(f'total harga = Rp{total_harga:,}')