

def find_number():
    ops = ['+','-','*','/','']
    for i in range(1000,10000):
        num_str = str(i)
        ans = int(num_str[::-1])
        expression = ''
        for first in range(len(ops)):
            for second in range(len(ops)):
                for thrid in range(len(ops)):
                    expression += num_str[0]+ops[first]+num_str[1]+ops[second]+num_str[2]+ops[thrid]+num_str[3]
                    if '/0' in expression :
                        break;
                    copyexpression = '';
                    pos = 0;
                    while pos < len(expression):
                        if expression[pos] == '0' and pos+1<len(expression) and expression[pos+1] not in ops:
                            pos += 1
                        else:
                            copyexpression += expression[pos]
                            pos += 1

                    if len(expression) > 4 and eval(copyexpression) == ans:
                        print(expression + ' = ' + str(ans))
                    expression = ''

if __name__ == '__main__':
    find_number()
