stack = []

expr = input("Enter postfix expression: ").split()

temp = 1
index = 0

quadruples = []
triples = []

for token in expr:
    if token in ['+', '-', '*', '/']:
        op2 = stack.pop()
        op1 = stack.pop()

        result = "t" + str(temp)

        quadruples.append([token, op1, op2, result])

        triples.append([index, token, op1, op2])

        stack.append(result)

        temp += 1
        index += 1

    else:
        stack.append(token)

print("\nQUADRUPLES")
print("Op\tArg1\tArg2\tResult")

for q in quadruples:
    print(q[0], "\t", q[1], "\t", q[2], "\t", q[3])

print("\nTRIPLES")
print("Index\tOp\tArg1\tArg2")

for t in triples:
    print(t[0], "\t", t[1], "\t", t[2], "\t", t[3])