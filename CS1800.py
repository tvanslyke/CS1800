# -*- coding: utf-8 -*-
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
        both = True gives the coefficients 'A' and 'B' of
        the equation A*x + B*y = gcd(x,y)"""
    x = [1, 0]
    y = [0, 1]
    q = a / b
    a, b = b, a % a
    while r[1]:
        x[0], x[1] = x[1], x[0] - q * x[1]
        y[0], y[1] = y[1], y[0] - q * y[1]
        q = a / b
        a, b = b, a % a
    if both:
        return (x[-1], y[-1]) 
    else:
        return x[-1] % b if a == 1 else None    

def primefact(number):
    """ Prime factorization of 'number'.
        Returns a list of 2-tuples in which the first
        element is the prime factor and the second is the
        number of times that prime appears.  For example,
        [(2,1), (5,3)] corresponds to  2^1 * 5^3 = 250
        ( 2**1 * 5**3 in Python syntax )."""

    if isprime(number) or number == 1:
        return [(number, 1)]
    else:
        factors = []
        counts = []
        for primenum in (prime(n) for n in xrange(1, number)):
            if number == 1:
                break
            if not number % primenum:
                factors.append(primenum)
                counts.append(1)
                number = number // primenum
                while not (number % primenum):
                    counts[-1] += 1
                    number = number // primenum
        return zip(factors, counts)

def encrypt_general(message, encrypter, modulo = 26):
    return 

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

def cartesian(*sets):
    """ Returns the cartesian product of the argument sets.  This can get very big."""
    def product(s1, s2):
        return set([(el1, el2) for el1 in s1 for el2 in s2])
    def merge(s1, s2):
        return set(tuple(list(el1) + [el2]) for el1 in s1 for el2 in s2)
    master = product(sets[0], sets[1])
    for s in sets[2:]:
        master = merge(master, s)
    return master

def subsets(s, cardinality):
    """ Returns a set of subsets with the specified cardinality.
        The subsets will be selected from input set 's'."""
    pass
    
    


def powerset(s):
    """ Returns the powerset of a set.  Subsets will be instances of
        the 'frozenset' type.

        This is the optimal option as it is far faster than the others
        for larger sets and correctly computes powersets of powersets.
        ie) it handles sets containing sets correctly.

        NOTE:  This will hog up your RAM if you use it to compute
               the power set of the power set of a set larger than 4 elements.
               I used all 32 gigs of ram trying pset(pset({1,2,3,4,5})).
               Thats 4294967296 elements, and each element eats up a lot of
               memory!

        This implementation is recursive."""
    def iterate(s, newSet = None):
        if newSet is None:
            newSet = set()
            s = {item for item in s}
        thisItem = frozenset([s.pop()])
        newSet.add(thisItem)
        for item in set(newSet):
            newSet.add(frozenset.union(thisItem, item))
        if s:
            return iterate(s, newSet)
        else:
            newSet.add(frozenset())
            return newSet

    return iterate(s)

def totient(num):
    """ Returns the totient of num."""
    if isprime(num):
        return num - 1
    else:
        return sum((1 for n in xrange(1, num) if euclid(num, n) == 1))
        

def powerset_old(s):
    """ Returns the powerset of a set.  Subsets will be instances of
        the 'frozenset' type. Broken for sets containing sets. ¯\_(ツ)_/¯"""
    sets = set([frozenset([item]) for item in s])
    lengthstart = 0
    while len(sets) != lengthstart:
        lengthstart = len(sets)
        sets = set.union(sets, set([frozenset.union(s1, s2)
                                    for s1 in sets for s2 in sets]))
        
    return set([frozenset(subset) for subset in sets] + [frozenset()])

    
def powerset_alt(s):
    """ Much slower way of getting the powerset."""
    tuples = cartesian(*[s for _ in range(len(s))])
    return set([frozenset(item) for item in tuples] + [frozenset()])
    
    
    pass
def breakRSA(e, n, message = None):
    """ Breaks a 'nice' RSA encryption with public key '(e, n)'."""
    (p, _), (q, _)  = primefact(n)
    tot = (p - 1) * (q - 1)
    d = inverse(e, tot, both = False)
    if message:
        return [num ** d % n for num in message]
    else:
        return d

def permute(n, r):
    """ Permutations of 'r' subitems in a set of 'n' items."""
    return factorial(n)/factorial(n - r)

def choose(n, r):
    """ Combinations of 'r' subitems in a set of 'n' items"""
    return permute(n, r) / factorial(r)

permutations = permute
combinations = choose

def binom(num):
    """ Coefficients of the resultant expansion of (x+y)^(num)."""
    return [choose(num, n) for n in range(num+1)]


def pigeon(bins, pigeons):
    """ Pigeon hole principle with 'n' boxes needing
        'pigeons' items to fill them.  Gives the 'smallest maximum'
        that a bin/box must hold no matter how the 'pigeons' are arranged."""
    return pigeons // bins + bool(pigeons % bins)

def organize(seq):
    f = factorial(sum(seq))
    return f/(reduce(lambda x, y: x * y, [factorial(n) for n in seq]))

if __name__ == "__main__":
    pass
    








