width = int(input())
line = ""
while(1):
   line = input()
   if (line == 'END'):
      break
   L = len(line)
   dot = (width-L)//2 
   dots = dot if (width-L)%2==0 else dot+1
   line = "."* dots + line + "."* dot
   print(line)