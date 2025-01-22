import os
directory = "ABC"
parent_dir = r"C:\Users\DeepADabhi\Desktop"
# if the r is not specified then it will give error as the python will interpret the \
# so wherenver there is an escape character, consider adding such string inside of the raw string format
path = os.path.join(parent_dir, directory)
# os.path.join, joins the parent directory with the directory specified, both are passed as an argument over here
print(path)

os.mkdir(path)
# this will create the directory at the specified path