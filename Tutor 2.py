def celcius(suhu, ke): 
    if ke == 1:
        return (suhu * 9 / 5) + 32
    if ke == 2:
        return 4 / 5 * suhu
    if ke == 3:
        return suhu + 273


def fahrenheit(suhu, ke):
    if ke == 1:
        return (suhu - 32) * 5 / 9
    if ke == 2:
        return 4 / 9 * (suhu - 32)
    if ke == 3:
        return 5 / 9 * (suhu - 32) + 273


def reamur(suhu, ke):
    if ke == 1:
        return 5 / 4 * suhu
    if ke == 2:
        return 9 / 4 * suhu + 32
    if ke == 3:
        return 5 / 4 * suhu + 273


def kelvin(suhu, ke):
    if ke == 1:
        return suhu - 273
    if ke == 2:
        return 9 / 5 * (suhu - 273) + 32
    if ke == 3:
        return 4 / 5 * (suhu - 273)

# Function ada 4

while True:
    suhu = ['Celcius', 'Fahrenheit', 'Reamur', 'Kelvin']
    try:
        print('Dari')
        for i in range(len(suhu)): # For i in range untuk perulangan, len untuk menghitung berapa value dalam list, sehingga jumlah perulangan sesuai dengan banyaknya isi dalam list
            print(f'{i + 1}. {suhu[i]}') #i+1 digunakan agar pilihan tidak dimulai dari angka 0
        dari = int(input('Pilihan [1-4] :'))
        temperatur = int(input(f'Masukkan Suhu {suhu[dari - 1]}:'))
        del suhu[dari - 1]

        print('Ke')
        for i in range(len(suhu)):
            print(f'{i + 1}. {suhu[i]}')
        ke = int(input('Pilihan [1-3] :'))
        if dari == 1:
            hasil = celcius(temperatur, ke)
        elif dari == 2:
            hasil = fahrenheit(temperatur, ke)
        elif dari == 3:
            hasil = reamur(temperatur, ke)
        elif dari == 4:
            hasil = kelvin(temperatur, ke)
        print(f'Hasil: {hasil}')
        lanjut = int(input("lanjut(1/0)"))
        if lanjut == 0:
            break
    except ValueError:
        continue
