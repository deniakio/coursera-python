def fizzbuzz (n):
    if not n % 3 == 0 and not n % 5 == 0:
        return n
    else:
        if n % 3 == 0 and not n % 5 == 0:
            return "Fizz"
        else:
            if n % 5 == 0 and not n % 3 == 0:
                return "Buzz"
            else:
                return "FizzBuzz"
