code = "9I2×1+P."
prc = 0
ch = list(code)
labels = [i for i, x in enumerate(ch) if x == "@"]
running = True
stack = []
fstack = ""
functions = {}
def f(token):
    if token == "0":
        stack.extend([0])
    elif token == "1":
        stack.extend([1])
    elif token == "2":
        stack.extend([2])
    elif token == "3":
        stack.extend([3])
    elif token == "4":
        stack.extend([4])
    elif token == "5":
        stack.extend([5])
    elif token == "6":
        stack.extend([6])
    elif token == "7":
        stack.extend([7])
    elif token == "8":
        stack.extend([8])
    elif token == "9":
        stack.extend([9])
    elif token == "D":
        stack[-1] -= 1
    elif token == "I":
        stack[-1] += 1
    elif token == ".":
        running = False
        
    elif token == "+":
        stack[-2] = stack[-2] + stack[-1]
        stack.pop()
    elif token == "-":
        stack[-1] *= -1
    elif token == "×":
        stack[-2] = stack[-2] * stack[-1]
        stack.pop()
    elif token == "÷":
        stack[-1] = 1/stack[-1]
    elif token == "P":
        print(stack[-1])
    elif token == "p":
        stack.pop()
    elif token == "T":
        stack.extend([True])
    elif token == "F":
        stack.extend([False])
    elif token == "¬":
        stack[-1] = not stack[-1]
    elif token == "∧":
        stack[-2] = stack[-2] and stack[-1]
        stack.pop()
    elif token == "i":
        stack.extend([int(input())])
    elif token == "G":
        prc = label[stack[-1]]
    elif token == "g":
        if stack[-2]:
            prc = label[stack[-1]]
    elif token == "⇔":
        a = stack[-1]
        stack[-1] = stack[-2]
        stack[-2] = a
    elif token == "^":
        stack[-2] = stack[-2] ** stack[-1]
        stack.pop()
    elif token == "f":
        fstack.extend([chr(stack[-1])])
    elif token == "d":
        functions[stack[-1]] = "".join(fstack)
        fstack = []
    else:
        fn(ord(token))
def fn(t):
    frc = 0
    while running:
        try:
            token = functions[t][frc]
        except:
            running = False
            break
        f(token)
        frc += 1
while running:
    try:
        token = ch[prc]
    except:
        running = False
        break
    f(token)
    prc += 1
print(stack)
