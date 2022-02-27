# write your code here
def is_number(x):
    try:
        int(x)
    except ValueError:
        return False
    return True


def main():
    terms = None

    while terms != '/exit':
        terms = input()
        if terms == '/exit':
            continue
        elif terms == '/help':
            print('The program is a simple calculator, terms and operations are separated by spaces.')
            continue
        elif terms == '':
            continue
        factor = 1
        result = 0
        terms = terms.split()
        for term in terms:
            if '-' in term and not is_number(term):
                if len(term) % 2 == 0 and '+' not in term:
                    factor = 1
                else:
                    factor = -1
            elif '+' in term:
                factor = 1
            else:
                result += factor * int(term)
        print(result)

    print('Bye!')


if __name__ == '__main__':
    main()
