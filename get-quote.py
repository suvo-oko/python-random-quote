import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for i in range(0,2):
        last=16
        rnd=random.randint(0,last)
        print(quotes[rnd].rstrip())

if __name__== "__main__":
  primary()
