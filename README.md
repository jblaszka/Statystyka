ekipa=['Kamil','Justynka','Asia']
x=input()
print(x)
ekipa.append(x)
print(ekipa)
ekipa[0]='Kozak'
print(ekipa)
for i, ludzie in enumerate(ekipa):
    if i==2:
        print("Koniec {} {}".format('kasia','basia'))
        break
    print(i)
    print(ludzie)
