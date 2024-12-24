#ренеймер
import os

folder_path = ''

video = [i for i in os.listdir(folder_path) if i.endswith(".mp4")]
#rename 

for i, file in enumerate(video, start=1):
    filename, extension = os.path.splitext(file)
    new_filename = f"{i:03d}{extension}"
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_filename))

print("Файлы успешно переименованы")

