import cv2 as cv
import os
import random,shutil


samp_path = "/content/drive/My Drive/AMLI Final Project/Sampling_trashnet" 
#don't forget to change! If it's not a existing path....
#os.mkdir(samp_path)

############ Sampling function ############
def sampling(waste,percentage):
    file_path = os.path.join(original_path, waste)  #get file from 
    save_path = os.path.join(samp_path, waste)      #save file to 
    os.makedirs(save_path)                          #create the folder to save sampling files

    filenames = os.listdir(file_path)
    sampled_files = random.sample(filenames, round(len(filenames)*percentage/100))

    for file in sampled_files:
        shutil.copyfile(os.path.join(file_path, file),os.path.join(save_path, file))   


############ ############
trashnet_path = ".........."
amli_path = "........./Resize_trashnet"
percentage = 20    #edit the percentage 


for original_path in [trashnet_path, amli_path]:
    waste_types = ['Cardboard','Glass','Metal','Paper','Plastic','Trash']   #Without E-waste
  
    for waste in waste_types:
        sampling(waste,percentage)

#Copy the E-waste folder to sampling dataset
shutil.copyfile(os.path.join(amli_path, "E-Waste"),samp_path)




