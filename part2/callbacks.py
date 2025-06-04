# iteration is number of times to run the function
# func is the function to be called in each iteration
def processtimes(iteration,func):
    for x in range(iteration):
        print(f"Processing iteration {x+1} of {iteration}")
        func(f"iteration {x+1}")	#callback function with data
    print("Processing complete.")

def infobit(data):
    print(f"Data received: {data}")

def whocares(data):
    print(f"Who cares about this data? {data}")

targetfun = lambda data: print(f"Target function received: {data}")

processtimes(5, infobit) 
print("-------------------------------------------------")
processtimes (2, whocares)
print("---------------------------------------------------")
processtimes(3, targetfun)
print("---------------------------------------------------")