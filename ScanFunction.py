import theano
import theano.tensor as T
import numpy as np

#define shared variables
k = theano.shared(0)
n_sym = T.iscalar('n_sym')

results, updates = theano.scan(lambda: {k : (k+1)}, n_steps = n_sym)

accumulator = theano.function([n_sym], [], updates=updates, allow_input_downcast=True)

print (k.get_value())
accumulator(5))
print (k.get_value())
