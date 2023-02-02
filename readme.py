def read_eps(filepath) -> dict:
    lines = []
    with open(filepath,'r') as f:
        lines = f.readlines()

    list_of_states = lines[1].rstrip().split(',')

    res = {}
    for state in list_of_states:
        res[state] = []
        res[state].append(state)
    
    list_of_starts = lines[3].rstrip().split(',')
    list_of_accepts = lines[4].rstrip().split(',')
    transits = lines[4:-1]

    for st in list_of_starts:
        for t in transits:
            lt = t.rstrip().split(',')
            if lt[0] == st:
                if lt[1] == '':
                    res[st].append(lt[2])

    for state in list_of_states:
        if state not in list_of_starts:
            for t in transits:
                lt = t.rstrip().split(',')
                if lt[0] == state: 
                    if lt[1] == '':
                        res[state].append(lt[2])

    for t in transits:
        lt = t.rstrip().split(',')
        if lt[1] == '':
            for saved in res[lt[2]]:
                if saved != lt[2]:
                    res[lt[0]].append(saved)
                        
    for s in res:
        print(s+':'+','.join([sres for sres in sorted(res[s])]))
    print(lines[-1])
