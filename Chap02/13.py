with open("col1.txt") as f1:
    with open("col2.txt") as f2:
        with open ("merged.txt", "w") as out:
            for a in zip (f1.readlines(), f2.readlines()):
                out.write("\t".join([x.rstrip() for x in a])+"\n")
