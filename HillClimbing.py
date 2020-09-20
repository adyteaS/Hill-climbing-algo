import numpy as np

#Create input binary array

m = np.random.randint(2,size = 40)

#checking random array
#print (m)

#create matrix with this array repeated for 40 iterations, we need 40 different strings

m = np.tile(m,(41,1))

#checking 4 of 40 different strings
#print (m[0:10])

#create 40 different inputs, //1 because we are not altering the input string stored in first row

def flip_bit(m):

    for i in range (1,40):
    
        #ith row and i-1th column
        #1-current value, to flip the bit
    
        m[i,i-1] = np.subtract(1,m[0,i-1]) 
    
    return m

#Checking the flipped bits of 10 arrays        
#print (flip_bit(m)[0:9])

#Function

def fn(s):
    
    return abs(12*sum(s) - 160)

#Algorithm implementation

def hill_climb(t = 100):
    
    results = []
    
    for j in range (t):
        
        #Checking the number of runs
        #print ("run: " + str(j))
        
        local = False

        first_iter = True

        while local != True:

            #In the iteration we create an input string, in subseqent iterations we use vc <- vn condition till convergence

            if first_iter:

                vc = np.random.randint(2,size = 40 )

                first_iter = False

            m = np.tile(vc,(41,1))

            m = flip_bit(m)

            #input string function value

            fvc = fn(m[0])

            #temporary variable
            fvn_max = 0
            #index of array with highest function value
            index = 0

            for i in range(1,40):

                if fn(m[i])>fvn_max:

                    fvn_max = fn(m[i])
                    index = i

            fvn = fvn_max

            #Checking the outputs and iterations of each iteration
            #print ("f(vc) : " + str(fvc) +"\t"+"f(vn) : "+str(fvn))

            if fvn > fvc:

                #swapping vc and vn

                vc = m[index]

            else:
                results.append(fvc)
                local = True
                
    return results

#Final results

print (hill_climb(100))
