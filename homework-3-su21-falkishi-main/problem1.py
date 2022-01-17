import numpy as np
import matplotlib.pyplot as plt



def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: list
    :return: list
    """


    i = 0;

    h_sum = 0;

    h_new = [];

    while i < len(hist):
        h_sum =  h_sum + hist[i]
       
	 i += 1;

    for j in hist:
        a = j / h_sum;

        h_new.append(a);

    return (h_new);
    
    pass


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width
    :param histo: list 
    :param width: float
    :return: float
    """
    

    q_sum = 0;

    a = 0;

    b = 0;

    h_p = norm_histogram(histo);
    
    h_sq =[0] * len(h_p);
    
         
    while b < len(h_p):
        h_sq[b] = h_p[b] ** 2;
        
        q_sum = q_sum + (h_sq[b]);

        a += histo[b];

        b += 1;


    j_compute = 2 / ((a - 1) * width) - (((a + 1)/((a - 1) * width))* (q_sum))

    return (j_compute);

    pass


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    op_h = [];

    low = min_bins;

    while low <= max_bins:
        j_compute = compute_j( plt.hist( data, low, (minimum ,maximum))[0], (maximum - minimum)/ low);
        
        op_h.append(j_compute);
        
        low += 1;


    return (op_h);

    pass


def find_min(l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.
    :param l: list
    :return: tuple
    """

    l_min = min(l);
    
    min_i = l.index(l_min);

    min_t = (l_min,min_i);
    

    return min_t ;
    
    pass



if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
