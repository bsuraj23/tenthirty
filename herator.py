def my_generator (n):
    value = 0
    while value <  n:
      yield value
      value += 1
      # Using the generator to print number from 0 to 4
      for num in my_generator(5):
         print(num)
