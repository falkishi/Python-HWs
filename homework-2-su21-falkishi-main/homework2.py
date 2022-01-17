def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here
	
	#this is to check if the number of bins is negative or equal to zero
	hist = []; #empty list of hist
	
	if (n <= 0):
		#prints a statment for number of bins
		print('The bins are equal to zero or negative');
		
		return(hist); 
	elif (b > h): 

		#prints a statment if the lower band is larger than the upper band
		print('The upper limit is less than the lower limit');
		
		return(hist);
	#initializing hist that is a list of n zeros
	hist = [0] * n;

	#calculates the bin width

	w = (h - b) / n;

	#a for loop to return the right outcome

	for k in range (0,len(data)):
		
		if (b >= data[k]):
			continue;

		elif (h <= data[k]):
			continue;
		else: 
			for i in range (0,n):
		
				if ((b + w + w * i) > data[k] and (data[k] >= (b + w * i))):
					#increment by one
					hist[i] = hist[i] + 1;
					continue;
	return hist 
	

    # return the variable storing the histogram
    # Output should be a list

pass


def addressbook(name_to_phone, name_to_address):
    #name_to_phone and name_to_address are both dictionaries
    
    # Write your code here
    #initialize address_to_all
	address_to_all = {};
	
	#for loop to 
	for a in name_to_address.values():
		address_to_all[a] = 0;


	for n,a in name_to_address.items():
		#when it does not equal to zero 
		if (address_to_all[a] != 0):
			#check if it has a different number 
			if (address_to_all[a][1] != name_to_phone[n]):	
				#printing the warning for changing the number 
				print('Warning: ', n,' has a different number for ', a,' than ', address_to_all[a][0][0],'. Using the number for ', address_to_all[a][0][0],'.', sep ="");
			#inserting for address to all
			address_to_all[a][0].insert(1,n);
		else: 
			address_to_all[a] = ([n], name_to_phone[n]);
	#Sorting address to all
	address_to_all[a][0].sort;
	return address_to_all   

    

    # return the variable storing address_to_all
    # Output should be a dictionary
    
pass
