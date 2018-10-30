def check_prime_number(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, ' is not Prime Number')
            break
    else:
        print(num, ' is Prime Number')


check_prime_number(13)
check_prime_number(29)
check_prime_number(37)
check_prime_number(9)
check_prime_number(15)
check_prime_number(46)
check_prime_number(100)
