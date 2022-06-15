from PIL import Image
import json
import os 
path="C:/Users/freed/Downloads/생활 폐기물 이미지/Validation"
file_list=os.listdir(path)
def split_text(text):
    text=text.split(".jpg")
    return text[0]
def img_save(i,v):
    image_name=image_list[i]
    image_path=path2+"/"+image_folder+"/"+image_name+".jpg"
    origin_img=Image.open(image_path)
    with open('C:/Users/freed/Downloads/생활 폐기물 이미지/Validation/[V라벨링]라벨링데이터/'+c1+"/"+c2+"/"+image_folder+"/"+image_name+".json", "r",encoding= "utf-8" ) as f:
        json_obj=json.load(f)
    x1=json_obj["Bounding"][0]['x1']
    y1=json_obj["Bounding"][0]['y1']
    x2=json_obj["Bounding"][0]['x2']
    y2=json_obj["Bounding"][0]['y2']
    cropped_img=origin_img.crop(map(int,(x1,y1,x2,y2)))
    cropped_img.save("C:/Users/freed/Desktop/croppedImg/"+v+"/"+c1+"/"+image_name+".jpg")
for folder in file_list[1:]:
    c1,c2,c3=folder.split('_')
    c1=c1[5:]
    path2=path+"/"+folder
    image_folder_list=os.listdir(path2)
    for image_folder in image_folder_list:
        image_list=os.listdir(path2+"/"+image_folder)
        image_list=list(map(split_text,image_list))
        for i in range(5):
            if i in [0,1]:
                try:
                    img_save(i,"train")
                except:
                    print("keyerror: "+image_list[i])
            elif i in [2,3]:
                try:
                    img_save(i,"validation")
                except:
                    print("keyerror: "+image_list[i])
            else:
                try:
                    img_save(i,"test")
                except:
                    print("keyerror: "+image_list[i])



