def parse(infile,outfile):
    in_file = open(infile)
    out_file = open(outfile)
    quotes = []
    line_lengths = []
    max_len = 0
    min_len = 0
    
    file_contents = in_file.readlines()

    for line in file_contents:
        if line[0] != '-':
            quotes.append(line.lower())
            line_lenghts.append(len(line))
    for length in line_lengths:
        n = length
        if n > max_len:
            acc = n
    for length in line_lengths:
        m = length
        if m < max_len:
            min_len = m
        
    in_file.close()
    out_file.close()
