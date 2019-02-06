def create_list():
    fin = open('running-config.cfg')
    line = fin.readline()
    t = []
    for line in fin:
        word = line.split()
        if word[0] == 'access-list':
           if word[1] == 'global_access':
              t.append(line)
           elif word[1] == 'fw-management_access_in':
              t.append(line)
    print(t)
create_list()

