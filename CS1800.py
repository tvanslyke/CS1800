from sympy import isprime, prime, factorial

def euclid(a, b):
    """ Euclidean Algorithm."""
    a, b = b, a%b
    return a if not b else euclid(a, b)

def lcm(a, b):
    """ Least common multiple."""
    return (a * b) / (euclid(a, b))

def inverse(a, b, both = False):
    """ Multiplicative inverse of 'a' in mod 'b'.
        both = True give"""
    x = [1, 0]
    y = [0, 1]
    r = [a, b]
    q = r[0] / r[1]
    r[0], r[1] = r[1], r[0] % r[1]
    while r[1]:
        x[0], x[1] = x[1], x[0] - q * x[1]
        y[0], y[1] = y[1], y[0] - q * y[1]
        q = r[0] / r[1]
        r[0], r[1] = r[1], r[0] % r[1]
    if both:
        return (x[-1], y[-1]) 
    else:
        return x[-1] % b if r[0] == 1 else None    

def primefact(number):
    """ Prime factorization of 'number'"""

    if isprime(number):
        return [(number, 1)]
    else:
        factors = []
        counts = []
        for primenum in (prime(n) for n in xrange(1, number)):
            if number == 1:
                break
            elif not number % primenum:
                factors.append(primenum)
                counts.append(1)
                number = number // primenum
                while not (number % primenum):
                    counts[-1] += 1
                    number = number / primenum
        return zip(factors, counts)

def encrypt(message, a, b):
    """ Encrypts a message with formula y = a * x + b.
        Input may be either a string message or a list of indices 0-25."""
    alpha = [chr(char) for char in range(ord('a'), ord('z'))]
    if isinstance(message, str):
        offset = 65 if ord(message[0]) <=90 else 97
        encrypted = [(a * (ord(char) - offset) + b) % 26 for char in message]
    else:
        encrypted = [(a * char + b) % 26 for char in message]
    return "".join([chr(char + 65) for char in encrypted]), encrypted

def decrypt(message, a, b):
    """ Decrypts a message encrypted with formula y = a * x + b.
        Input may be either a string message or a list of indices 0-25."""

    if isinstance(message, str):
        offset = 65 if ord(message[0]) <=90 else 97
        message = [(ord(char) - offset) % 26 for char in message]  
    a = inverse(a, 26)
    b = 26 - b
    decrypted = [(a * (char + b)) % 26 for char in message]
    return "".join([chr(char+65) for char in decrypted]), decrypted

def cartesian(s1, s2):
    """ Returns the cartesian product of two sets.  This can get very big."""
    return set([(el1, el2) for el1 in s1 for el2 in s2])

def powerset(s):
    """ Returns the powerset of a set.  Subsets will be instances of
        the 'frozenset' type. """
    sets = set([frozenset([item]) for item in s])
    lengthstart = 0
    while len(sets) != lengthstart:
        lengthstart = len(sets)
        sets = set.union(sets, set([frozenset.union(s1, s2)
                                    for s1 in sets for s2 in sets]))
        
    return set([frozenset(subset) for subset in sets] + [frozenset()])


def breakRSA(e, n, message = None):
    """ Breaks a 'nice' RSA encryption with public key '(e, n)'."""
    (p, _), (q, _)  = primefact(n)
    tot = (p - 1) * (q - 1)
    d = inverse(e, tot, both = False)
    if message:
        return [num ** d % 33 for num in message]
    else:
        return d

def permute(n, r):
    """ Permutations of 'r' subitems in a set of 'n' items."""
    return factorial(n)/factorial(n - r)

def choose(n, r):
    """ Combinations of 'r' subitems in a set of 'n' items"""
    return permute(n, r) / factorial(r)

def pigeon(bins, num_to_fill):
    """ Pigeon hole principle with 'n' boxes needing
        'num_to_fill' items to fill them."""
    return bins * (num_to_fill - 1) + 1

def cardinality(s1, s2):
    """ Cardinality of 's1' and 's2'"""
    return len(set.union(s1,s2))

permutations = permute
combinations = choose


def organize(seq):
    f = factorial(sum(seq))
    return f/(reduce(lambda x, y: x * y, [factorial(n) for n in seq]))

if __name__ == "__main__":
    pass









