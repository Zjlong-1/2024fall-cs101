l=input().split()
l1={'+','-','*','/'}
def solve(l):
    for i in range(1,len(l)):
        if l[i] not in l1 and l[i-1] in l1 and l[i+1] not in l1 :
            if i==1:
                return eval(f'{float(l[i])}{l[i-1]}{float(l[i+1])}')
            else:
                lk=l[0:i-1]+[eval(f'{float(l[i])}{l[i-1]}{float(l[i+1])}')]+l[i+2:]
                return solve(lk)
ans=float(solve(l))
print(f'{ans:.6f}')
#每次操作一次，做切片，进行递归。
#ON算法：
'''
# http://cs101.openjudge.cn/practice/02694/
前缀表达式是运算符在前，操作数其后，
就是假如碰到一个运算符，其后就需要有连续的两个操作数才能运算消去，
否则就一直等待输入或者等待后面的运算结束得到操作数,
这恰好能用递归实现。
'''
# pylint: skip-file
def Exp():
    global pos
    pos += 1
    chr = calculatelist[pos]
    if chr == '+':
        return Exp() + Exp()
    elif chr == '-':
        return Exp() - Exp()
    elif chr == '*':
        return Exp() * Exp()
    elif chr == '/':
        return Exp() / Exp()
    else:
        return float(chr)



calculatelist = []
pos = -1
calculatelist = list(input().split())
result = Exp()
print("{:.6f}".format(result))
#基本想法如下：从后往前读取表达式，碰见数字则压入栈，碰见运算符号则从栈顶弹出两个数据进行计算，将计算结果再压入栈即可
# http://cs101.openjudge.cn/practice/02694/
expression = input().split()
stack = []
while expression:
    a = expression.pop(-1)
    if a in ['+', '-', '*', '/']:
        c = stack.pop(-1)
        d = stack.pop(-1)
        if a == '+':
            stack.append(c + d)
        elif a == '-':
            stack.append(c - d)
        elif a == '*':
            stack.append(c * d)
        else:
            stack.append(c / d)
    else:
        stack.append(float(a))

print("{:.6f}".format(stack[0]))
#简化版：
# http://cs101.openjudge.cn/practice/02694/

D=input().split()
D.reverse()
def STACK(D):
    stack=[]
    for i in D:
        if i in '+-*/':
            a=stack.pop()
            b=stack.pop()
            stack.append(str(eval(a+i+b)))
        else:
            stack.append(i)
    return stack[0]
print('%6f'% float(STACK(D)))
