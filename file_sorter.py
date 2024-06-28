# Script to sort files in a folder based on their extensions
import os
import shutil

folderPath = input("Enter the folder path: ")
fileNames = os.listdir(folderPath)

for file in fileNames:
    fileExtension = os.path.splitext(file)[1][1:] # [1] -> Getting the file extension from the file name, [1:] -> Removing the dot

    if fileExtension:
        finalFolderPath = f"{folderPath}\\{fileExtension} Files"

        if not os.path.exists(finalFolderPath):
            os.makedirs(finalFolderPath) # Creating a new folder if it does not exist

        sourceFilePath = f"{folderPath}\\{file}" # Path of the file to be moved
        destinationFilePath = f"{finalFolderPath}\\{file}" # Path of the file to be moved to
        dublicateFolderPath = f"{folderPath}\\Duplicate Files" # Path of the folder where the duplicate files will be moved to

        if not os.path.exists(destinationFilePath):
            shutil.move(sourceFilePath, destinationFilePath) # Moving the file from the source folder to the destination folder
        else:
            if not os.path.exists(dublicateFolderPath):
                os.makedirs(dublicateFolderPath) # Creating the duplicates folder
                shutil.move(sourceFilePath, f"{dublicateFolderPath}\\{file}") # Moving the duplicate file to the duplicates folder
                print (f"\'{file}\' already exists in \'{fileExtension}\' Files folder and has been moved to \'Duplicate Files\' folder")
            else:
                print(f"\'{file}\' already exists in \'{fileExtension}\' and \'Duplicate Files\' folders") 
    
    else:
        print (f"\'{file}\' does not have an extension")

print("\n---All files have been sorted successfully---")


    
    
    
