#!/usr/bin/python3                                                
def safe_print_list_integers(my_list=[], x=0):                    
    num_int_print = 0                                             
    try:                                                          
        for i in range(x):                                        
            print("{:d}".format(my_list[i]), end='')              
            num_int_print += 1                                    
        print()                                                   
    except ValueError:                                            
        pass                                                      
    except IndexError:                                            
        pass                                                      
    return num_int_print