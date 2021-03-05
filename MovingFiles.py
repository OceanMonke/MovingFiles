import glob
import shutil

#this programe will take all .MOV files and put them in chosen location

source_files = 'D:/Zdjęcia/103APPLE/*.MOV' 
target_folder = 'C:/Users/Łukasz/Desktop/.MOV'

filelist=glob.glob(source_files)
for single_file in filelist:
    shutil.move(single_file, target_folder)
