#Calculate pension(age, monthsOfService, firstSalaries, secondSalaries, thirdSalaries, annualPension)
def main():
      age = int(input('Enter your age: '))
      monthsOfService = int(input('Enter number of months of service: '))
      firstSalaries = float(input('Enter first of three highest salaries: '))
      secondSalaries = float(input('Enter second of three highest salaries: '))
      thirdSalaries = float(input('Enter third of three highest salaries: '))

      ave = calculateAve(firstSalaries, secondSalaries, thirdSalaries)

      p = percentageRate(monthsOfService)

      print('Annual pension: $%.2f' % (ave * p))

def yrs(age, monthsOfService):
      while True:
            try:
                  numOfMonths = monthsOfService / 12
            except ValueError:
                  print('Error value!')
                  continue
            if ((numOfMonths >= 0 and numOfMonths < 20) or (age >= 0 and age < 50)):
                        print('Wrong input, retirement should at least 20 years of service!')
                        exit(0)
            else:
                  break

def calculateAve(firstSalaries, secondSalaries, thirdSalaries):
      return ((firstSalaries + secondSalaries + thirdSalaries) / 3)

def percentageRate(monthsOfService):
      fixedRate = 80
      firstRate = 1.5
      secondRate = 1.75
      thirdRate = 2
      yrs = monthsOfService / 12

      r1 = 0.0
      r2 = 0.0
      r3 = 0.0

      if (yrs <= 10):
            for x in range(round(yrs)):
                  if(x < 5):
                        r1 += firstRate
                  elif(x >= 5 and x < 10):
                        r2 += secondRate
      else:
            r1 = firstRate * 5
            r2 = secondRate * 5
            r3 = thirdRate * (yrs - 10)
      
      perRate = (r1 + r2 + r3)
      
      if (perRate < fixedRate):
            return perRate / 100
      else:
            return fixedRate / 100

main()