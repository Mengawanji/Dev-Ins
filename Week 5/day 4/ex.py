with open('dev.text','w') as fp:
    pass

f = open('dev.text','a')
f.write('Her sirri')
f.close()

f = open('dev.text','a+')
f.write ('\ngood job')

