#This program takes two lines of input. The first line is a "starting time" expressed in a 24-hour clock 
# with leading zeroes, like 08:30 or 14:07. The second line is a duration D in minutes. 
# Print out what time it will be D minutes after the starting time. For example, for input 12:30, 47 
# the correct output would be 13:17. All times should be formatted as numbers between 00:00 and 23:59,
# but the time period may go over midnight. For example, on input 23:59, 13 the correct output is 00:12

starting_time = list(input())   #24 hour clock
D = input()               # Duration in minutes
hour = int(starting_time[0]+ starting_time[1])
minute = int(starting_time[3]+starting_time[4])

if int(D) < 60:

   if (minute+int(D)) <=59:
      minute = minute + int(D)
      print("{}:{}".format(hour,minute))
   else:
      if(hour!= 23):
         gap = 60 - minute
         left = int(D) - gap
         minute = left
         hour = hour + 1
         print("{:02d}:{:02d}".format(hour,minute))
      else:
         gap = 60 - minute
         left = int(D) - gap
         minute = left
         hour = int("00")                                        #this solution is only for d <=60
         print("{:02d}:{:02d}".format(hour,minute))

else:              #if D > 60 min
    hr_gap = int(D) // 60
    hour = hour + hr_gap

    if (hour + hr_gap) >= 23:
        exceed_hr = 24-(hour+hr_gap)
        hour = hour + exceed_hr
        minute_gap = (int(D)%60)
        minute = minute + minute_gap

        if minute<= 59:
            print("{:02d}:{:02d}".format(hour,minute))

        else:
            if(hour!= 23):
                gap = 60 - minute
                left = int(D) - gap
                minute = left
                hour = hour + 1
                print("{:02d}:{:02d}".format(hour,minute))
            else:
                gap = 60 - minute
                left = int(D) - gap
                minute = left
                hour = int("00")                                        #this solution is only for d <=60
                print("{:02d}:{:02d}".format(hour,minute))
    
    else:
        minute_gap = (int(D)%60)
        minute = minute + minute_gap
        hour = hour + hr_gap
    
        if minute<= 59:
            print("{:02d}:{:02d}".format(hour,minute))
        else:
            if(hour!= 23):
                gap = 60 - minute
                left = int(D) - gap
                minute = left
                hour = hour + 1
                print("{:02d}:{:02d}".format(hour,minute))
            else:
                gap = 60 - minute
                left = int(D) - gap
                minute = left
                hour = int("00")                                        
                print("{:02d}:{:02d}".format(hour,minute))