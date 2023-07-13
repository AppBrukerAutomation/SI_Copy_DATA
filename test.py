# import shutil
# import os
# path = r"C:\Users\Shachar.Yust-extern\OneDrive"
#
#
# # print(path)
# #
# # print(os.path.basename(path))
#
#
# import pyinstaller_versionfile
#
# pyinstaller_versionfile.create_versionfile(
#     output_file="Version_SICopyData.txt",
#     version="1.0.0",
#     company_name="Bruker Application Team",
#     original_filename="SICopyData.exe",
#     product_name="App Automation - SI Copy Data"
# )
import datetime
# from shutil import *
#
# path_file = r"D:\Documents\Desktop\test1\New Text Document.txt"
# path_folder = r"D:\Documents\Desktop\test1"
#
# becup = r"D:\Documents\Desktop\aaa221"
#
#
# try:
#     copytree(path_folder, becup)
# except:
#     copy2(path_folder, becup)




# from tkinter.filedialog import *
#
# im = askopenfilename()
# print(im)

# from datetime import *
#
# print(datetime.today().date())



import os
from zipfile import ZipFile

# Create a ZipFile Object
with ZipFile('D:/Documents/Desktop/Zipped file.zip', 'w') as zip_object:
   # Adding files that need to be zipped
   zip_object.write(r"D:\Documents\Desktop\test1\New Text Document.txt")
   zip_object.write(r"D:\Documents\Desktop\test1\222")