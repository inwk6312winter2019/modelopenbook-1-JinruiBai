import os
import shutil

fin = open('running-config.cfg','r')
fout = open('new_conf','w')
for line in fin:
	word = line.split()
	if word[0] == 'security-level':
       		word[1] = '10'
      		word_out = ' '.join(word)
       		fout.write(' '+word_out+'\n')
       		continue
    	if word[0] == 'ip':
      		 ipadd = word[2].split('.')
       		ipadd[3] = '10'
       		word[2] = '.'.join(ipadd)
       		word_out = ' '.join(word)
       		fout.write(' '+word_out+'\n')
    	else:
      		 fout.write(line)
