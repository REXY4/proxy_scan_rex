import os

def read_file(path_file):
    file_name,file_extension = os.path.splitext(path_file)
    # check format file
    if file_extension != '.txt':
       print("your format file not txt") 
       return
    
    with open(path_file, 'r') as file:
        content = file.read()
        content = content.replace("https://" , "")
        content = content.replace("http://" , "")
        content = content.replace("socks4://" , "")
        content = content.replace("socks5://" , "")
        return content;
