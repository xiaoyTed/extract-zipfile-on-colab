import zipfile
import os

img_path = os.path.join('test_all', 'Test_fix.zip')
img_zip = zipfile.ZipFile(img_path)
img_list = img_zip.namelist()
print("the number of image: ", len(img_list))
num_list = []
try:
    with open("record.txt", "r") as record:
        for line in record.readlines():
            num_list.append(int(line))
    print("the already read image: ", max(num_list))
except:
    print("there is no initailize record txt")
record = open("record.txt", "a")
for i, img in enumerate(img_list):
    if i >= max(num_list):
        img_zip.extract(img, path='test_all')
        record.write(str(i)+'\n')
    else:
        continue
record.close()

