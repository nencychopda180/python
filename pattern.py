# for i in range(0,5):
#     for j in range(0,i+1):
#         print ("*",end=' ')
#     print()

# for i in range(1,6):
#      for j in range(1,i+1):
#          print (i,end=' ')
#      print()
    
# for i in range(1,6):
#      for j in range(1,i+1):
#          print (j,end=' ')
#      print()
    

# for i in range(1,6):
#      for j in range(1,i+1):
#          print ("*",end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print ("*",end=' ')
#      print()
# print()


# for i in range(1,6):
#      for j in range(1,i+1):
#          print (i,end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print (i-1,end=' ')
#      print()
# print()


# for i in range(1,6):
#      for j in range(1,i+1):
#          print (j,end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print (j,end=' ')
#      print()
# print()

# for i in range(1,6):
#      for j in range(1,i+1):
#          print (i,end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print (i-1,end=' ')
#      print()
# print()


# for i in range(5,0,-1):
#      for j in range(i,0,-1):
#          print (j,end=' ')
#      print()
# print()
  

# for i in range(1,5+1):
#     print(" "*(5-i)+"*"*i)

# for i in range(1,5+1):
#     print(" "*(5-i)+" *"*i)


# for i in range(1, 6 + 1 ):
#     print ( " " * (6 - i),end =" " ) 
#     for j in range(1, i):
#          print (( i + j) % 2,end =" " )
#     print()


# for i in range(1,5 + 1):
#      print ( " " * (5 - i),end ="" ) 
#      print ((str(i) + " ")* i)
# for i in range(5 - 1,0,-1):
#      print ( " " * (5 - i),end ="" ) 
#      print ((str(i) + " ")* i)


# for i in range(1,5 + 1):
#      print (" " * (5 - i),end="") 
#      for j in range(1,i + 1):
#          print(j,end=" ")
#      print()

# for i in range(5 - 1,0,-1):
#      print (" " *(5 - i),end="" ) 
#      for j in range(1,i + 1):
#          print(j,end=" ")
#      print()

for i in range(5):
    for j in range(5):
        if i== 0 or i==5 -1 or j==0 or j== 5 -1 or (i==j and i ==5//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    