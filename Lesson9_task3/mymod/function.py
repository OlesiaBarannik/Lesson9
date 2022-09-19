def count_lines(test1):
    with open(test1, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_chars(test1):
    with open(test1, 'r') as file:
        chars = file.read()
        number_of_characters = len(chars)
        return number_of_characters

def test(test1):
    print(count_lines(test1))
    print(count_chars(test1))


# test('test1.txt')