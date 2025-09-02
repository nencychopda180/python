'''
* 
* * 
* * *
* * * *
* * * * *
'''

# for i in range(0,5):
#     for j in range(0,i+1):
#         print ("*",end=' ')
#     print()

'''
1 
2 2 
3 3 3
4 4 4 4
5 5 5 5 5
'''

# for i in range(1,6):
#      for j in range(1,i+1):
#          print (i,end=' ')
#      print()
    
'''
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
'''

# for i in range(1,6):
#      for j in range(1,i+1):
#          print (j,end=' ')
#      print()
    
'''
* 
* * 
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

# for i in range(1,6):
#      for j in range(1,i+1):
#          print ("*",end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print ("*",end=' ')
#      print()
# print()

'''
1 
2 2 
3 3 3
4 4 4 4
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

# for i in range(1,6):
#      for j in range(1,i+1):
#          print (i,end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print (i-1,end=' ')
#      print()
# print()

'''
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

# for i in range(1,6):
#      for j in range(1,i+1):
#          print (j,end=' ')
#      print()
# for i in range(5,1,-1):
#      for j in range(1,i):
#          print (j,end=' ')
#      print()
# print()

'''
5 4 3 2 1 
4 3 2 1 
3 2 1
2 1
1
'''

# for i in range(5,0,-1):
#      for j in range(i,0,-1):
#          print (j,end=' ')
#      print()

  
'''
    *
   **
  ***
 ****
*****

'''

# for i in range(1,5+1):
#     print(" "*(5-i)+"*"*i)

'''
     *
    * *
   * * *
  * * * *
 * * * * *

'''

# for i in range(1,5+1):
#     print(" "*(5-i)+" *"*i)

'''
1 
    0 1
   1 0 1
  0 1 0 1
 1 0 1 0 1
'''

# for i in range(1, 6 + 1 ):
#     print ( " " * (6 - i),end =" " ) 
#     for j in range(1, i):
#          print (( i + j) % 2,end =" " )
#     print()

'''
1 
   2 2 
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
'''

# for i in range(1,5 + 1):
#      print ( " " * (5 - i),end ="" ) 
#      print ((str(i) + " ")* i)
# for i in range(5 - 1,0,-1):
#      print ( " " * (5 - i),end ="" ) 
#      print ((str(i) + " ")* i)


'''
    1 
   1 2 
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

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

'''
* * * * * 
*       * 
*   *   * 
*       * 
* * * * * 
'''

# for i in range(5):
#     for j in range(5):
#         if i== 0 or i==5 -1 or j==0 or j== 5 -1 or (i==j and i ==5//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
    * * * * * 
     * * * * 
      * * *
       * *
        *
'''
# for i in range(5,0,-1):
#     print(" "*(5-i)+"* "*i)

'''
    * 
   * * 
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

# for i in range(1,5+1):
#     print(" "*(5-i) + "* " * i)
# for i in range(5-1,0,-1):
#     print(" "*(5-i) + "* " * i)

'''
* * * * * 
 * * * * 
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''

# for i in range(5,0,-1):
#     print(" "*(5-i)+"* "* i)
# for i in range(2,5+1):
#     print(" "*(5-i)+"* "* i)

'''
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
'''

# num=1
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''

# ch=65
# for i  in range(1,5+1):
#     for j in range(i):
#         print(chr(ch),end=" ")
#     ch+=1
#     print()
