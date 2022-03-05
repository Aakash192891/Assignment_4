# Question 1 
def Towers_Of_Hanoi(numdisks, frm_disc, to_disc, aux_disc):
    if numdisks == 1:
        print("Move disk [1] from rod [",
              frm_disc, "] to rod {", to_disc, '}')
        return
    Towers_Of_Hanoi(numdisks-1, frm_disc, aux_disc, to_disc)
    print("Move disk ["+str(numdisks) + "] from rod [",
          str(frm_disc)+" ] to rod {", to_disc, '}')
    Towers_Of_Hanoi(numdisks-1, aux_disc, to_disc, frm_disc)
numdisks = 4
Towers_Of_Hanoi(numdisks, 'A', 'C', 'B') 

# Output 1
Move disk [1] from rod [ A ] to rod { B }
Move disk [2] from rod [ A ] to rod { C }
Move disk [1] from rod [ B ] to rod { C }
Move disk [3] from rod [ A ] to rod { B }
Move disk [1] from rod [ C ] to rod { A }
Move disk [2] from rod [ C ] to rod { B }
Move disk [1] from rod [ A ] to rod { B }
Move disk [4] from rod [ A ] to rod { C }
Move disk [1] from rod [ B ] to rod { C }
Move disk [2] from rod [ B ] to rod { A }
Move disk [1] from rod [ C ] to rod { A }
Move disk [3] from rod [ B ] to rod { C }
Move disk [1] from rod [ A ] to rod { B }
Move disk [2] from rod [ A ] to rod { C }
Move disk [1] from rod [ B ] to rod { C }



#Question 2
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 

# Output 2 
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]



