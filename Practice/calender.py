base_year=int(1900) #just to declare and initialize a value we do it like this
print("We will consider 1st January,1900 as the start year!")
year=int(input("Please enter a year in which you want to find out what day was on 1st january: "))#variable name  cannot contain spaces and must begin with letter or an underscore
if year>=1900:
  total_year=int(year-base_year-1) #becase e.g base year is 2000 and user entered 2024 to 2000(1) 2001(2) 2023(3) we will not include 2024 because it is not completed its on 1st Jan
    #Now we will calculate leap years
  leap_year=int(total_year/4)
  non_leap_years=int(total_year-leap_year) #We will do this because total years have leap years in them and normal years have 365 days  and leap years have 366 days
  days=int((non_leap_years*365)+(leap_year*366)+1) #We will do +1 because 1st january will be included in days from above we did -1 because that was years
  day=int(days%7)
  if day==0:
    print("Monday")
  elif day==1:
    print("Tuesday")
  elif day==2:
    print("wednesday")
  elif day==3:
    print("Thursday")
  elif day==4:
    print("Friday")    
  elif day==5:
    print("Saturday")    
  else:
    print("Tuesday") 
else:
    print("You have entered a year before 1900")                       