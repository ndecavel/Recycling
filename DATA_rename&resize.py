import os
import cv2 as cv

dataset_path = "/content/drive/My Drive/AMLI Final Project/Testing_trashnet"
resize_path = "/content/drive/My Drive/AMLI Final Project/Resize_trashnet"
waste_types = ['Cardboard','Glass','Metal','Paper','Plastic','Trash', 'E-Waste']
# waste_types = os.listdir(dataset_path)
# subsets = ['train','valid', 'test']

os.mkdir(resize_path)

############ Rename function ############
def rename(waste): 
    i = 0
    file_path = os.path.join(dataset_path, waste, 'Photo')   #Remove 'Photo' if this folder no longer exists
    for filename in os.listdir(file_path): 
        newName = waste + str(i) + ".jpg"
        src = file_path+'/'+ filename 
        dst = file_path+ '/' + newName 
        os.rename(src, dst) 
        i += 1

############ Resize function ############
def resize(waste):
  #create categories folder in resize dataset
    file_path = os.path.join(dataset_path, waste, "Photo") 
    save_path = os.path.join(resize_path, waste) 
    os.mkdir(save_path)
  
    for filename in os.listdir(file_path):
        img = cv.imread(os.path.join(file_path,filename))
        if img is None:
            continue
        
        r_img = cv.resize(img, new_size)
        cv.imwrite(os.path.join(save_path,filename), r_img)
        

# subsets = ['train','valid', 'test']

for waste in waste_types:
    rename(waste)
    resize(waste)