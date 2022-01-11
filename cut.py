f = open('data/imglist_test.txt','r')
nf = open('data/new_imglist_test.txt','w')
for line in f.readlines():
  nf.write('data/data_256_extra'+line)
f.close
nf.close

f = open('data/imglist_train.txt','r')
nf = open('data/new_imglist_train.txt','w')
for line in f.readlines():
  nf.write('data/data_256_extra'+line)
f.close
nf.close