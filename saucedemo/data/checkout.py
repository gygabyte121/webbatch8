class DataCheckout:
    first_name = 'dandi'
    last_name = 'setiawan'
    postal_code = '12121'

class DataValidateError: 
    validateError_sample = [('','setiawan','12121','Error: First Name is required'),
                     ('dandi','','12121','Error: Last Name is required'),
                     ('dandi','setiawan','','Error: Postal Code is required')]
