print "1 calculadora"
print "2 par o impar"
op= int(raw_input(""))
if op==1:
  num1 = int(raw_input("ingrese un numero"))
  num2 = int(raw_input("ingrese otro numero"))
  var= raw_input("escoja la operacion")

  if var == "+" or "suma":
   print num1 + num2
  elif var == "-" or"resta":
   print  num1-num2
  elif var=="*" or"multiplicacion":
   print  num1 * num2
  elif var=="/" or "division":
   print num1 / num2
else:
    ok=int(raw_input("ingrese un numero\n"))  
    if(ok%2==0):
        print(str(ok)+" es par")  
    else:
        print(str(ok)+" es impar")
print "nacho es gay"        
 

