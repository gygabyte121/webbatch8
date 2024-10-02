class Data:
    username = 'standard_user'
    password = 'secret_sauce'

class DataError:
    error_sample = [('standard_user','salah','Epic sadface: Username and password do not match any user in this service'),
                ('locked_out_user','secret_sauce','Epic sadface: Sorry, this user has been locked out.'),
                ('salah','secret_sauce','Epic sadface: Username and password do not match any user in this service'),
                ('','secret_sauce','Epic sadface: Username is required')]