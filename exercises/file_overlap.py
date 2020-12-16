prime = []
happy = []

# read prime numbers & append values to list prime []
with open('PrimeNumber1000.txt', 'r') as p:
    line = p.readline()
    while line:
        line = line.strip()
        prime.append(int(line))
        line = p.readline()
# read happy numbers & append values to list happy []
with open('HappyNumbers1000.txt', 'r') as h:
    line = h.readline()
    while line:
        line = line.strip()
        happy.append(int(line))
        line = h.readline()

def compare(prime,happy):
    # convert to a set
    prime_set = set(prime)
    happy_set = set(happy)

    print([x for x in (prime_set&happy_set) if (prime_set&happy_set)])
    
compare(prime,happy)