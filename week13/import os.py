import os
file_dir_path = './인터넷방송'
file_names = os.listdir(file_dir_path)
file_names

i = 1
for name in file_names:
    before_name = os.path.join(file_dir_path, name)
    after_name = str(i) + '.json'
    after_name = os.path.join(file_dir_path, after_name)
    os.rename(before_name, after_name)
    i += 1
    
    
    