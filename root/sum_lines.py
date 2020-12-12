with open("nov_2020_spending.md", 'r') as f:
    lines = f.readlines()
    print(lines)
    print(sum([float(x) for x in lines]))
