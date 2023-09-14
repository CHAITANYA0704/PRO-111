import os 
import shutil
os.getcwd()
os.mkdir("Images")
from_dir = ""
list = os.listdir(from_dir)
print(list)


path1 = "C:/Users/salun/OneDrive/Desktop/Python/PRO_C135_STUDENT_BOILERPLATE-main/app.py"
root, extension = os.path.splittext(path1);
print("The root element are ", root);
print("The extension is ", extension);


source = "C:/Users/salun/OneDrive/Desktop/Python/PRO_C135_STUDENT_BOILERPLATE-main/app.py"
destination = ""
dost = shutil.copy(source,destination)
print("The file has been copied sucessfully !!")