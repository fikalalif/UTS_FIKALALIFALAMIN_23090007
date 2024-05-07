tahun = int(input('Masukan tahun = '))
if tahun % 400 == 0 or tahun % 4 == 0:
    print(f'tahun {tahun} = tahun kabisat')
else:
    print(f'tahun {tahun} = bukan tahun kabisat')    