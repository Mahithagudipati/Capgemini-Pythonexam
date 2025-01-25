cart = {}
total = 0

def prompt():
  return input("\nChoose an option from below:\n1. Add items\n2. View items\n3. Total\n4. Exit\n")

def add_items():
  item = input("Enter the name of the item: ")
  price = int(input("Enter the price of the item: "))
  global total
  total += price

  if item in cart:
    cart[item] += price
  else:
    cart[item] = price

def view_items():
  print()
  for key in cart:
    print(f"{key} : ${cart[key]}")
  print()

def total_price():
  global total
  print(f"\nThe total price of the items in the cart is ${total}")
  print()

def main():
  while True:
    n = prompt()
    if n in ['1','2','3','4']:
      if n == '1':
        add_items()
      elif n == '2':
        view_items()
      elif n == '3':
        total_price()
      elif n == '4':
        break
    else:
      print("Enter a valid option(1,2,3,4)")

main()
