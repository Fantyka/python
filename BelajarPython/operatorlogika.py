#OPERATOR PERBANDINGAN (AND) adalah akan menghasilkan nilai true apabila kedua statement benar
#RUMUS
# T and T = True
# T and F = False
# F and F = False
var = 10
print ( 5 < var and 7 < var) #T AND T = T
print (25 < var and 1 < var) #F AND T = F
print (20 < var and 1 > var) #F AND F = F


#OPERATOR PERBANDINGAN (OR) adalah akan menghasilkan nilai true apabila salah satu statement benar
#RUMUS
var = 60
print ( 1 < var or 20 > var) #T OR F = T
print ( 15 < var or 23 < var)#T OR T = T
print (40 > var or 70 < var )#F OR F = F


#operator NOT adalah kebalikan dari hasil 
# var = true, kebalikanya false
# var = false, kebalikannya True
var = 10
print (not ( 5 < var and 7 < var)) #T => F
print (not (40 > var or 70 < var ))#T => F
