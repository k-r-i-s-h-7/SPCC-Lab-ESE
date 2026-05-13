# Generic LL(1) Parser Construction

grammar = {}

n = int(input("Enter number of productions: "))

print("Enter productions (Example: E->TQ):")

# ---------------- INPUT ----------------

for i in range(n):

    rule = input()

    lhs, rhs = rule.split("->")

    grammar[lhs] = rhs.split("|")


# ---------------- FIRST ----------------

first = {}

for nt in grammar:
    first[nt] = set()


def find_first(symbol):

    # terminal
    if symbol not in grammar:
        return {symbol}

    # already calculated
    if len(first[symbol]) != 0:
        return first[symbol]

    for prod in grammar[symbol]:

        # epsilon
        if prod == '#':
            first[symbol].add('#')

        else:

            for ch in prod:

                temp = find_first(ch)

                first[symbol].update(temp - {'#'})

                if '#' not in temp:
                    break

            else:
                first[symbol].add('#')

    return first[symbol]


for nt in grammar:
    find_first(nt)


# ---------------- FOLLOW ----------------

follow = {}

for nt in grammar:
    follow[nt] = set()

start_symbol = list(grammar.keys())[0]

follow[start_symbol].add('$')

changed = True

while changed:

    changed = False

    for head in grammar:

        for prod in grammar[head]:

            for i in range(len(prod)):

                B = prod[i]

                if B in grammar:

                    before = len(follow[B])

                    # beta exists
                    if i + 1 < len(prod):

                        beta = prod[i + 1]

                        # non-terminal
                        if beta in grammar:

                            follow[B].update(first[beta] - {'#'})

                            if '#' in first[beta]:
                                follow[B].update(follow[head])

                        # terminal
                        else:
                            follow[B].add(beta)

                    else:
                        follow[B].update(follow[head])

                    if len(follow[B]) > before:
                        changed = True


# ---------------- LL(1) TABLE ----------------

table = {}

for nt in grammar:
    table[nt] = {}


for head in grammar:

    for prod in grammar[head]:

        first_prod = set()

        # epsilon production
        if prod == '#':
            first_prod.add('#')

        else:

            for ch in prod:

                temp = find_first(ch)

                first_prod.update(temp - {'#'})

                if '#' not in temp:
                    break

            else:
                first_prod.add('#')

        # fill FIRST entries
        for terminal in first_prod - {'#'}:
            table[head][terminal] = prod

        # fill FOLLOW entries for epsilon
        if '#' in first_prod:

            for terminal in follow[head]:
                table[head][terminal] = '#'


# ---------------- PRINT FIRST ----------------

print("\nFIRST SETS")

for nt in first:
    print("FIRST(", nt, ") =", first[nt])


# ---------------- PRINT FOLLOW ----------------

print("\nFOLLOW SETS")

for nt in follow:
    print("FOLLOW(", nt, ") =", follow[nt])


# ---------------- PRINT TABLE ----------------

print("\nLL(1) PARSING TABLE")

for nt in table:

    for terminal in table[nt]:

        print("M[", nt, ",", terminal, "] =",
              nt + "->" + table[nt][terminal])


# ---------------- PARSER ----------------

stack = ['$', start_symbol]

inp = list(input("\nEnter input string: ") + '$')

print("\nStack\t\tInput\t\tAction")

while True:

    stack_str = "".join(stack)

    input_str = "".join(inp)

    top = stack.pop()

    current = inp[0]

    # ACCEPT
    if top == '$' and current == '$':

        print(stack_str,
              "\t\t",
              input_str,
              "\t\tAccepted")

        break

    # MATCH TERMINALS
    elif top == current:

        print(stack_str,
              "\t\t",
              input_str,
              "\t\tMatch")

        inp.pop(0)

    # NON TERMINAL
    elif top in grammar:

        if current in table[top]:

            production = table[top][current]

            print(stack_str,
                  "\t\t",
                  input_str,
                  "\t\t",
                  top + "->" + production)

            # epsilon skip
            if production != '#':

                for symbol in reversed(production):
                    stack.append(symbol)

        else:

            print(stack_str,
                  "\t\t",
                  input_str,
                  "\t\tRejected")

            break

    else:

        print(stack_str,
              "\t\t",
              input_str,
              "\t\tRejected")

        break