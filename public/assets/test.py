input_bilangan = input(" angka: ")
bilangan = int(input_bilangan)
if (bilangan<0) and (bilangan % 2 == 0):
    print("bilangan genap negatif")
elif (bilangan<0) and (bilangan % 2 == 1):
    print("bilangan ganjil negatif")
elif (bilangan>0) and (bilangan % 2 == 0):
    print("bilangan genap negatif")
elif (bilangan>0) and (bilangan % 2 == 1):
    print("bilangan ganjil negatif")
else:
    print("tet")