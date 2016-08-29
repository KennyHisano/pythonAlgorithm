def recurPowerNew(base, exp):

    # Your code here
    if exp <= 0:
        return 1
    if exp == 1:
        return base

    if exp > 0:
        if exp % 2 == 0:
            return recurPowerNew(base*base, exp/2)
        else:
            return base*(recurPowerNew(base,exp-1))
