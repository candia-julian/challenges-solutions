def tribonacci(signature, n):
    #create an empty list as container for the future addition of numbers of tribonacci
    sec = []
    #create a conditional for attempts of try signature list with less than the original requiriment
    if len(signature) <= 2:
        return signature
    #conditionals for n <= 3, in that cases return the first numbers of list or empty list if n = 0
    if n == 0:
        return sec
    elif n == 1:
        return signature[:1]
    elif n == 2:
        return signature[:2]
    elif n == 3:
        return signature[:3]
    #principal operation
    else:
        sec = signature
        #loop creating for any element range beetween [3:n)
        for i in range(3, n):
            #create a variable as container of sum of last three variables of the list sec. IMPORTANT: slicing is in reverse (last negative number -1 in slicing) and stop in after -4 element in list
            suma_sec = sum(sec[:-4:-1])
            #add the sum of three last numbers in sequence to the list
            sec.append(suma_sec)
        #return the sequence :D
        return sec
