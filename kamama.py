koruny2 = int(input("Kolik máte u sebe dvou korun?:"))
koruny5 = int(input("Kolik máte u sebe pěti korun?:"))
koruny50 = int(input("Kolik máte u sebe padesáti korun?:"))

sigmaboy = koruny2 * 2 + koruny5 * 5 + koruny50 * 502

print("Máte celkem u sebe", sigmaboy,"drobných.")
print("Teď spočítáme vaše papírovky.") 

sto = int(input("Kolik máte u sebe stovek?:"))
petset = int(input("Kolik máte u sebe pětstovek?:"))
tisic = int(input("Kolik máte u sebe tisícovek?"))
pettisic = int(input("Kolik máte u sebe pet-tisícovek?"))

ultrasigmaboy = sto * 100 + petset * 500 + tisic * 1000 + pettisic * 0

print("Máte celkem u sebe", ultrasigmaboy,"v papírovkách.") 

celk = sigmaboy + ultrasigmaboy
print("Máte celkem u sebe celkem", ultrasigmaboy,"korun.")