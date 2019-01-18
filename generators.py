import checks
import structures as s

def global_var_writer(fileName):
    # generates a set of global, user-defined variables
    # takes input from the user and adds it to the file

    # check if the [global] header is present
    checkBool, lineNum = checks.check_global(fileName)
    writefile = open(fileName, 'w')

    if checkBool is True:
        #run the parameter code here
        #find the line number and append the file after the line number
        return True
    else:
        return False

def setup_file(fileName,numberOfDefaults=0):
    writefile = open(fileName, 'w')
    for i in range(numberOfDefaults):
        writefile.write(s.defaults[i]+'\n')

def setup_jobs():
    return 0