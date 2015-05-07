import pylab

x = pylab.rand(10000)

for i in range(10):
    pylab.hist(x, i+1)
    pylab.savefig('test%05d.png' % (i))
