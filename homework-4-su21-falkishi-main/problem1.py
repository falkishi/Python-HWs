def composeMap(fun1, fun2, l):
    """
    Returns a new list r where each element in r is fun2(fun1(i)) for the
    corresponding element i in l
    :param fun1: function
    :param fun2: function
    :param l: list
    :return: list
    """
    # Fill in
    #a new list r where each element in r is f2(f1(i))
    new_r = [];
    
    #a for loop to change all the elements in r to the desired output
    for i in l:

        new_r.append(fun2(fun1(i)));


    return(new_r);

    pass


def tripleMap(fun, l):
    """
    Returns a new list r where each element in r is fun(fun((fun(i))) for the
    corresponding element i in l
    :param fun: function
    :param l: list
    :return: list
    """
    # Fill in
    #creates a new list r 
    new_r= [];
    
    #a for loop to change each element in r to f(f(f(i)))
    for i in l:

        new_r.append(fun(fun(fun(i))));


    #returns the new list
    return (new_r);
    
    pass


def compose(fun1, fun2):
    # Fill in
    """
    Returns a new function f. f should take a single input i, and return
    fun1(fun2(i))
    :param fun1: function
    :param fun2: function
    :return: function
    """
    def retfun(i):

        #f takes a single input i 
        f = fun1(fun2(i));
        
        #returns f
        return (f);

        pass

    return retfun



def repeater(fun, num_repeats):
    """
    Returns a new function f. f should take a single input i, and return
    fun applied to i num_repeats times. In other words, if num_repeats is 1, f
    should return fun(i). If num_repeats is 2, f should return fun(fun(i)). If
    num_repeats is 0, f should return i.
    :param fun: function
    :param num_repeats: int
    :return: function
    """
    def retfun(i):
        
        #the value of the function
        
        func = i;

        # set the control variable to 0
        
        a = 0;
        
        
        #checks if num_repeats is zero to return i
        if num_repeats == 0:
            
            return i;
        # a while loop to get the function value after num_repeats iterations
        while a < num_repeats:
            
            func= fun(func);

            a += 1;

        return (func);
        
        pass
    return retfun


if __name__ == '__main__':
    def test1(x):

        return x * 2
    
    def test2(x):

        return x - 3
        
    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]

    print(composeMap(test1, test2, data))
    print(composeMap(test2, test1, data))
    print(tripleMap(test1, data))
    
    f1 = compose(test1, test2)
    
    print(f1(4))
    
    print(list(map(f1, data)))
    
    f2 = compose(test2, test1)

    print(f2(4))

    print(list(map(f2, data)))
    
    z = repeater(test1, 0)
    once = repeater(test1, 1)
    twice = repeater(test1, 2)
    thrice = repeater(test1, 3)
    
    print("repeat 0 times: {}".format(z(5)))
    print("repeat 1 time: {}".format(once(5)))
    print("repeat 2 times: {}".format(twice(5)))
    print("repeat 3 times: {}".format(thrice(5)))
