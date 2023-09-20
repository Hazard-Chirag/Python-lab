import os
import pathlib
import zipfile
import sys

dirname=input("Enter the directory name that you want to zip")
if not os.path.isdir(dirname):
    print("Doesnt exist")
    sys.exit(0)
curdir=pathlib.Path(dirname)
with zipfile.ZipFile("ex.zip",mode="w") as archive:
    for file_path in curdir.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curdir))
if(os.path.isfile("ex.zip")):
    print("SuccesS")
else:
    print("ERRor")