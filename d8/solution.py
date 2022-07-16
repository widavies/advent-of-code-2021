def p1():
    with open('input.txt') as f:
        signals = []
        outputs = []
        for line in f:
            split = line.split('|')
            signals.append(split[0].split())
            outputs.append(split[1].split())

    uniques = {2, 3, 4, 7}

    print("Count:", sum(map(lambda x: sum(map(lambda y: len(y) in uniques, x)), outputs)))

p1()
