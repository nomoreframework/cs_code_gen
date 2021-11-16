#cul.py
import sys
import os
print("\n" + "Example: generate.py Test -i" + "\n" + "added interface with name 'Test.cs' in the curent directory" + "\n" + 
        "('-i' = optional parameter, the class is created by default)")
path = os.getcwd()
parent = os.path.basename(path)
file_name = sys.argv[1]
object_flag = "interface" if sys.argv[2] == "-i" else "class"
namespace = os.path.basename(os.getcwd()) 

with open((file_name + ".cs"), "w") as file:
    file.write("namespace" + "\t" +  namespace + "\n" + "{" + "\n" + "\t" + object_flag + "\t" + file_name + "\n" + "{" + "\n" + "}" + "\n" + "}" )
