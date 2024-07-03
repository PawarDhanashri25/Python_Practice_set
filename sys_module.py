import sys

print("Number of arguments: ", len(sys.argv))

if len(argv)>=2:
    for item in sys.argv[1:]:
        with open(item, 'r') as f:
            f.read(item)
else:
    print("Wrong no of arguments. The script must be executed with atleast one argument")
    

