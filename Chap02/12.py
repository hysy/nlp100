with open("hightemp.txt") as f:
    lines = f.readlines()
    with open("col1.txt", 'w') as out1:
        out1.writelines([line.split()[0]+'\n' for line in lines])
    with open("col2.txt", 'w') as out2:
        out2.writelines([line.split()[1]+'\n' for line in lines])

    
    
