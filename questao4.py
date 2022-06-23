n1=int(input("digite um valor:"))
n2=int(input("digite um valor"))
soma=0
for item in range (n1,n2-1,-2):
  print (item)
  soma+=item
print(f"a soma dos numeros é {soma}")