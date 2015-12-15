import os

def job_depend(jobs):
    depend = {}
    for ajob in jobs:
        depend[ajob] = {}
        output = jobs[ajob]['outputs']
        for bjob in jobs:
            if bjob == ajob:
                continue
            binput = jobs[bjob]['inputs']
            for k in output:
                if k in binput:
                    if jobs[bjob]['pe'] or jobs[bjob]['pairs']:
                        depend[ajob][bjob] = 1
                    else:
                        depend[ajob][bjob] = 1/len(binput)
    return depend

def pollTree(depend,jobs,filesneedtoDel,filesneedtoAdd):
    for

