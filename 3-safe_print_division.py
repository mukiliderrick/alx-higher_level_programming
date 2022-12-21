#!/usr/bin/python3                                                
def safe_print_division(a, b):                                    
    try:                                                          
        result = a / b                                            
    except ZeroDivisionError:                                     
        print("Error: cannot divide by 0")                        
        return None                                               
    finally:                                                      
        print("Inside result: {}".format(result))                 
    return result