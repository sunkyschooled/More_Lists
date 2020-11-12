def sum_of_odd_nums(n):
    numbers = list(range(1,(n*2)))
    odds = [i for i in numbers if i%2 == 1]
    return sum(odds)
    

def caesar_cipher(message, key):
    list1 = [ord(i)+key for i in message]
    return bytes(list1).decode('ascii')
def fizzbuzz(n):
    listy = list(range(1,n+1))
    def Buzzy(m):
      if m%3 == 0 and m%5 == 0:
        return "Fizzbuzz!"
      elif m%3 == 0:
        return "Fizz!"
      elif m%5 == 0:
        return "Buzz!"
      else:
        return m
    listie = [Buzzy(i) for i in listy]
    return listie
def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(10):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "Frpsxwhu#Vflhqfh#lv#qr#pruh#derxw#frpsxwhuv#wkdq#dvwurqrp|#lv#derxw#whohvfrshv1"
    print(caesar_cipher(ciphertext, -3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()