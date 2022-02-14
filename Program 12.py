#30 Shruti nathavani
def checkValidity(p, q, r):
     
    # check condition
    if (p + q <= r) or (p + r <= q) or (q + r <= p) :
        return False
    else:
        return True       
 
# driver code
p = 10
q = 20
r = 30
if checkValidity(p, q, r):
    print("Valid")
else:
    print("Invalid")