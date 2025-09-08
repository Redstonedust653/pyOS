import random, os
print(str('echo '+str(random.randbytes(5))+' > ./root/secret.txt'))
os.system(str('echo '+str(random.randbytes(5))+' > ./root/secret.txt'))
