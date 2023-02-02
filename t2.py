def neps(path):
    with open(path,'r') as f:
        lines = f.readlines()

        global states
        global starts
        global accepts
        global old_transits
        global epsl_dict
        global res
        states = lines[1].rstrip().split(',')
        starts = lines[3].rstrip().split(',')
        accepts = lines[4].rstrip().split(',')
        counter = 0
        lc = 5
        for line in lines[5:]:
            if line == 'end\n':
                counter+=1
                if counter == 1:
                    first_end = lc
                if counter == 2:
                    second_end = lc
                    break
            lc+=1

        old_transits = lines[5:first_end]
        for trans in old_transits:
            old_transits[old_transits.index(trans)] = trans.rstrip().split(',')
        
        epsl = lines[first_end+1:second_end]

        epsl_dict = {}
        res = []

        for ep in epsl:
            ep = ep.rstrip().split(':')
            epsl_dict[ep[0]] = []
            ep1 = ep[1].rstrip().split(',')
            for e1 in ep1:
                if e1 != ep[0]: 
                    epsl_dict[ep[0]].append(e1)
        for a in range(1,5):
            res.append(lines[a])

        for state in states:
            if epsl_dict[state] == []:
                for trans in old_transits:
                    if trans[0] == state:
                        res.append(','.join(trans))
            else:
                for es in epsl_dict[state]:
                    for trans in old_transits:
                        if trans[0] == es:
                            if trans[1] != '':
                                res.append(state+','+','.join(trans[1:3]))

        res = list(dict.fromkeys(res))
        res.append('end')
        for r in res:
            print(r.rstrip())
