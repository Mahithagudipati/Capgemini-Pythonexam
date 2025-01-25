
def get_details():
  age = int(input("Enter your Age: "))
  salary = int( input("Enter your Salary: ").replace(',','') )
  credit_score = int(input("Enter your Credit Score: "))

  return age, salary, credit_score

def validate(age, salary, credit_score):
  if( age < 21 ):
    return "Age too low!"
  
  elif( salary < 50000 ):
    return "Not enough Salary!"
  
  elif( credit_score < 750 ):
    return "Low Credit Score! "
  
  return "Eligible for loan!!!"

def main():
  age, salary, credit_score = get_details()
  print( validate(age, salary, credit_score) )

main()
