def badan():
    berat_badan = float(input('Masukan berat badan = '))
    tinggi_badan = int(input('Masukan tinggi badan = '))
    bmi = berat_badan / tinggi_badan
    if bmi < 18.5:
        print('Berat badan kurang')
    elif bmi <= 18.5 or bmi < 24.9:
        print('Berat badan normal')
    elif bmi <= 25 or bmi <29.9:
        print('Berlebihan berat badan')
    elif bmi >= 30:
        print('Obesitas')        