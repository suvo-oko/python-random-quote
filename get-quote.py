import random  # a module to generate random numbers

def primary():
  f = open("quotes.txt", "a")
  f.write("Be radically transparent\n")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for i in range(0,2):
        last=17
        rnd=random.randint(0,last)
        print(quotes[rnd].rstrip())

if __name__== "__main__":
    primary()
