# OS module in python

# import os
os.getcwd() #Gives current directory
os.chdir('../')  #Changes the directory a step behind
os.mkdir() # Make new directory
os.listdir() # Get list of all files and directories in specified directory if no directory specified then list of files in current working directory is returned
os.remove() # removes or delete a file; path cannot remove or delete a directory; if tried to delete directory throws Error
os.rmdir() # removes dir not files and only delete empty dir; if files are present throws error
os.close() # A file opened need to be closed
os.rename() # rename only existed files
os.path.exist() # Checks file exist or not
os.path.getsize() # Gives size in bytes
