import os
import shutil

public = "public/"
items = os.listdir("public")
for item in items:
    item_path = public + item
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)
    else:
        os.remove(item_path)

print('')
print('--------------------------')
print('')
print("Data: removed")

import main


