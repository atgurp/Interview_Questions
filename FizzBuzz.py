def fizzbuzz(limit):
      # Write your code here
  lst = [] 

  for i in range(1, limit+1):
    if i % 3 == 0 and i % 5 == 0:
      lst.append('FizzBuzz')
    elif i % 3 == 0:
      lst.append('Fizz')
    elif i % 5 == 0:
      lst.append('Buzz')
    else:
      lst.append(i)

  return lst


inp = input('What number do you want FizzBuzz to count up to? ')

print(fizzbuzz(int(inp)))
