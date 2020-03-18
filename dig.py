import sys

a0=["  ***  ",
    " *   * ",
    "*     *",
    "*     *",
    "*     *",
    " *   * ",
    "  ***  "]
a1 = [" * ",
      "** ",
      " * ",
      " * ",
      " * ",
      " * ",
      "***"] 

a2 = [" ** ",
      "*  *",
      "   *",
      "  * ",
      "*   ",
      "*   ",
      "****"]

a3=  [" ** ",
      "*  *",
      "   *",
      " ** ",
      "   *",
      "*  *",
      " ** "]

a4=  ["*  *",
      "*  *",
      "*  *",
      " ***",
      "   *",
      "   *",
      "   *"]
    
a5=  ["****",
      "*   ",
      "*   ",
      "*** ",
      "   *",
      "*  *",
      " ** "]

a6=  [" ** ",
      "*  *",
      "*   ",
      "*** ",
      "*  *",
      "*  *",
      " ** "]

a7=  ["****",
      "   *",
      "   *",
      "  * ",
      " *  ",
      "*   ",
      "*   "]

a8=  [" ** ",
      "*  *",
      "*  *",
      " ** ",
      "*  *",
      "*  *",
      " ** "]

a9=  [" ** ",
      "*  *",
      "*  *",
      " ***",
      "   *",
      "*  *",
      " ** "]

set_trace()
Dig = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]

import time


import sys

try:

   dig = sys.argv[1] 
   row = 0 
    
   while row < 7: 
        
        time.sleep (.2)    
        line ="" 
        column = 0
        while column < len(dig): 
            
            number = int(dig[column]) 
            digit = Dig[number] 
            digit2=""   
            for i in range (len(digit[row])):
               
                if digit[row][i]=="*":digit2+=str (number)
                else: digit2+=" "
            
            line += digit2 + " "
            
            column += 1 
        print(line) 
        row += 1
        
except IndexError: 
    print(column)
    
    input ()
  
except ValueError as err: 
    print(err, "in", dig)
    
    input ()
    
print ('\a')
input ()

