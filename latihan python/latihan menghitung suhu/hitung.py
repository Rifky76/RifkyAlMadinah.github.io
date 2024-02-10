print("MENGUBAH FAHRENHEIT KE KELVIN DAN SEBALIKNYA\n")

fahrenheit = float(input("Masukan suhu dalam fahrenheit : "))
print("suhu adalah :",fahrenheit," fahrenheit")
4
kelvin = (fahrenheit + 459.67) * 5/9
print("suhu dalam kelvin  adalah : ",kelvin," kelvin")

kelvin = float(input("Masukan suhu dalam kelvin : "))
print("suhu adalah : ",kelvin,"kelvin")

fahrenheitk = 1.8*(kelvin - 273)+ 32
print("suhu dalam fahrenheit adalah : ",fahrenheitk,"fahrenheit")

