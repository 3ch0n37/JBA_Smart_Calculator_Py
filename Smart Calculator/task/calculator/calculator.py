# write your code here

def main():
    terms = None

    while terms != '/exit':
        terms = input()
        if terms == '/exit':
            continue
        elif terms == '/help':
            print('The program calculates the sum of numbers')
            continue
        elif terms == '':
            continue

        terms = [int(x) for x in terms.split()]
        print(sum(terms))

    print('Bye!')


if __name__ == '__main__':
    main()
