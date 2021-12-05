	#generate random numbers
    import random
    import time
   random.seed(6)
   for i in range(5):
    print(random.randint(10,50))
    print()
  t=int(time.time())
  random.seed(t)
  for i in range(5):
  print(random.randint(10,50))
