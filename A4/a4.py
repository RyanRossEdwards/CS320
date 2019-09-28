import random

def main(): 
    # Initial Values
    n = 8000000
    p = 8024047 # prime number > n

    # Initalise an empty Hash Table
    hash_table = [0] * n

    # 0 <= a, b < p
    a = random.randrange(0, p)
    b = random.randrange(0, p)
    
    # Create the email address list
    total_addresses = 1000000
    email_address_list = [i for i in range(1, total_addresses + 1)]
    
    for address in email_address_list:
        hash_table[universal_hash(a, b, n, p, address)] = 1 


### Question one ###
    try:
        for number in email_address_list:
            hash_value = universal_hash(a , b, n, p, number)
            
            if hash_table[hash_value] == 0:
                raise SpamDetected

    except SpamDetected:
        print("Spam test failed")

    else:
        print("Spam test passed")

### Question two ###
    # Based on formula in theoretical question 2
    theoretical_probability = 1 - (1 - 1/n) ** total_addresses

    print("Theoretical Probability =", theoretical_probability)
    
### Question three ###
    spam_email_count = 0
    spam_email_no = 1000
    
    for i in range(spam_email_no):
        random_address = random.randrange(total_addresses + 1, 9999999)
        hash_value = universal_hash(a, b, n, p, random_address)
        if hash_table[hash_value] == 1:
            spam_email_count += 1

    print("Simulated Probability =", spam_email_count / spam_email_no)
    print("No. Unblocked Spam =", spam_email_count)
    print()


# Hashing function based on universal hash family for integer
def universal_hash(a, b, n,  p, x):
    return ((a * x + b) % p) % n

class Error(Exception):
   """Base class for other exceptions"""
   pass
class SpamDetected(Error):
   """Spam has been detected"""
   pass

main()