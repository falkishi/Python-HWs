import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    # The below is for identifing a valid and an invalid phone number
    str_search = re.search(r'^(\S?\d+\W?)\W?(\d+)\-(\d+)', searchstring);
    
    
    if (str_search):
        return (True);
    else:
        return (False);


    pass
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """

    #The below is for determining the names of streets 

    Var = re.split('\d+', searchstring )[-1];
    str_search = re.search('(.*)\s(?=(Ave|St|Rd|Dr))', Var)
    Fv = str_search.group()
    
    
    
    Fv1 = Fv.split(" ")[1:];

    
    
    return " ".join(Fv1);



    pass
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    #The below is for returning the street names but in reverse 

    L = re.split('\d+',searchstring)[-1];
    str_search =re.search('(\s.*)\s(?=(Ave|St|Rd|Dr))', L);
    
    G_F = str_search.group();
    G_S = G_F;
    
    Q = str(G_S[::-1]);
    M = set(L.split(" "));
    N = set(G_F.split(" "));
    

    End_res = sorted(M.difference(N));
    
    End_res =" ".join(End_res);
    Val = searchstring.replace(L,Q);

    return(Val+End_res);


    pass


if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
