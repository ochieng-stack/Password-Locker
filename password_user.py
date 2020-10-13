class password:
    '''
    Class that generates new instances of passwords
    '''
    password_list = [] # Empty password list
    
    def _init_(self,first_name,second_name,age,password):
        
        # docstring removed for simplicity
        
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.password = password