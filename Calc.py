import math


def get_term():
    return input("term: ")


def split_term(term):
    chararray = []
    for char in term:
        chararray.append(char)
    # print(chararray)
    return chararray


def check_inner_parenthesis(chararray):
    begin = 0
    end = None
    for i in range(0, len(chararray)):
        if chararray[i] == '(':
            begin = i
        elif chararray[i] == ')':
            end = i
            break

    # print(begin, end)
    return begin, end


def check_syntax(term, ans):
    for i in range(len(term)):
        if term[i] == 's' and term[i-1] == 'n' and term[i-2] == 'a':
            term[i-2] = ans
            del(term[i])
            del(term[i-1])
            check_syntax(term, ans)
            break
    for i in range(len(term)):
        if term[i] == '*' and term[i-1] == '*':
            term[i-1] = '**'
            del(term[i])
            check_syntax(term, ans)
            break
    for i in range(len(term)):
        if term[i] == '/' and term[i-1] == '/':
            term[i-1] = '//'
            del(term[i])
            check_syntax(term, ans)
            break
    for i in range(2, len(term)):
        if term[i-3] == 'r' and term[i-2] == 'o' and term[i-1] == 'o' and term[i] == 't':
            term[i - 3] = 'root'
            del (term[i])
            del (term[i-1])
            del (term[i-2])
            check_syntax(term, ans)
            break
    for i in range(1, len(term)):
        try:
            term[i - 1] = str(float(term[i - 1]) * 10 + float(term[i]))
            del (term[i])
            check_syntax(term, ans)
            break
        except:
            pass
    for i in range(0, len(term)):
        if term[i] == 'i' and term[i-1] == 'p':
            term[i-1] = math.pi
            del(term[i])
            check_syntax(term, ans)
            break
    for i in range(0, len(term)):
        if term[i] == 'u' and term[i-1] == 'a' and term[i-2] == 't':
            term[i-2] = 2 * math.pi
            del(term[i])
            del(term[i-1])
            check_syntax(term, ans)
            break
    for i in range(0, len(term)):
        if term[i] == 'e':
            term[i] = math.e
            check_syntax(term, ans)
            break
    for i in range(2, len(term)-1):
        if term[i] == 'n' and term[i-1] == 'i' and term[i-2] == 's' and term[i-3] == 'a':
            term[i-3] = 'asin'
            del(term[i])
            del(term[i-1])
            del(term[i-2])
            check_syntax(term, ans)
            break
    for i in range(2, len(term)-1):
        if term[i] == 's' and term[i-1] == 'o' and term[i-2] == 'c' and term[i-3] == 'a':
            term[i-3] = 'acos'
            del(term[i])
            del(term[i-1])
            del(term[i-2])
            check_syntax(term, ans)
            break
    for i in range(2, len(term)-1):
        if term[i] == 'n' and term[i-1] == 'a' and term[i-2] == 't' and term[i-3] == 'a':
            term[i-3] = 'atan'
            del(term[i])
            del(term[i-1])
            del(term[i-2])
            check_syntax(term, ans)
            break
    for i in range(2, len(term)-1):
        if term[i] == 'n' and term[i-1] == 'i' and term[i-2] == 's':
            term[i-2] = 'sin'
            del(term[i])
            del(term[i-1])
            check_syntax(term, ans)
            break
    for i in range(2, len(term)-1):
        if term[i] == 's' and term[i-1] == 'o' and term[i-2] == 'c':
            term[i-2] = 'cos'
            del(term[i])
            del(term[i-1])
            check_syntax(term, ans)
            break
    for i in range(2, len(term)-1):
        if term[i] == 'n' and term[i-1] == 'a' and term[i-2] == 't':
            term[i-2] = 'tan'
            del(term[i])
            del(term[i-1])
            check_syntax(term, ans)
            break
    return term


def calc_sin(term):
    for i in range(len(term)):
        if term[i] == 'sin':
            term[i] = math.sin(float(term[i+1]))
            del(term[i+1])
            calc_sin(term)
            break
    for i in range(len(term)):
        if term[i] == 'cos':
            term[i] = math.cos(float(term[i+1]))
            del(term[i+1])
            calc_sin(term)
            break
    for i in range(len(term)):
        if term[i] == 'tan':
            term[i] = math.tan(float(term[i+1]))
            del(term[i+1])
            calc_sin(term)
            break
    for i in range(len(term)):
        if term[i] == 'asin':
            term[i] = math.asin(float(term[i+1]))
            del(term[i+1])
            calc_sin(term)
            break
    for i in range(len(term)):
        if term[i] == 'acos':
            term[i] = math.acos(float(term[i+1]))
            del(term[i+1])
            calc_sin(term)
            break
    for i in range(len(term)):
        if term[i] == 'atan':
            term[i] = math.atan(float(term[i+1]))
            del(term[i+1])
            calc_sin(term)
            break
    for i in range(len(term)):
        if term[i] == '!':
            term[i] = factorial(term[i-1])
            del(term[i-1])
            calc_sin(term)
            break
    return term


def factorial(number):
    result = 1
    for i in range(1, int(number)+1):
        result *= i
    return result



def calc_power(term):
    for i in range(len(term)):
        if term[i] == '**':
            term[i] = str(float(term[i-1]) ** float(term[i+1]))
            del(term[i+1])
            del(term[i-1])
            calc_power(term)
            break
        elif term[i] == 'root':
            term[i] = str(float(term[i + 1]) ** (1 / float(term[i - 1])))
            del (term[i + 1])
            del (term[i - 1])
            calc_power(term)
            break
    return term


def calc_multiply(term):
    for i in range(len(term)):
        if term[i] == '*':
            term[i] = str(float(term[i-1]) * float(term[i+1]))
            del(term[i+1])
            del(term[i-1])
            calc_multiply(term)
            break
        elif term[i] == '/':
            term[i] = str(float(term[i - 1]) / float(term[i + 1]))
            del (term[i + 1])
            del (term[i - 1])
            calc_multiply(term)
            break
        elif term[i] == '%':
            term[i] = str(float(term[i - 1]) % float(term[i + 1]))
            del (term[i + 1])
            del (term[i - 1])
            calc_multiply(term)
            break
        elif term[i] == '//':
            term[i] = str(float(term[i - 1]) // float(term[i + 1]))
            del (term[i + 1])
            del (term[i - 1])
            calc_multiply(term)
            break
    return term


def calc_plus(term):
    for i in range(len(term)):
        if term[i] == '+':
            term[i] = str(float(term[i-1]) + float(term[i+1]))
            del(term[i+1])
            del(term[i-1])
            calc_plus(term)
            break
        elif term[i] == '-':
            term[i] = str(float(term[i - 1]) - float(term[i + 1]))
            del (term[i + 1])
            del (term[i - 1])
            calc_plus(term)
            break
    return term


def check_del_parenthesis(term, begin, end):
    if end is None or end == 0:
        return term
    if (begin + 1) == (end - 1):
        del(term[end])
        del(term[begin])
    return term


def calculate(term, ans):
    try:
        term = split_term(term)
        print(term)
        term = check_syntax(term, ans)
        print(term)
        # print(term)
        while len(term) > 1:
            interval = check_inner_parenthesis(term)

            term[interval[0]:interval[1]] = calc_sin(term[interval[0]:interval[1]])
            print(term)
            term[interval[0]:interval[1]] = calc_power(term[interval[0]:interval[1]])
            print(term)
            term[interval[0]:interval[1]] = calc_multiply(term[interval[0]:interval[1]])
            print(term)
            term[interval[0]:interval[1]] = calc_plus(term[interval[0]:interval[1]])
            print(term)
            check_del_parenthesis(term, interval[0], interval[1])
        return float(term[0])
    except:
        return 'Syntax Error, Type "/reporterror your_term" to report that this error was no syntax error (replace ' \
               'your_term with your term) '


if __name__ == "__main__":
    calculate(get_term())
