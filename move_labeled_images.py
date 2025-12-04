from glob import glob
import shutil
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import Config

train_images = glob(fr"{Config.VAL_IMAGES_FOLDER}/*.*")
train_labels = glob(fr"{Config.VAL_LABELS_FOLDER}/*.txt")
print(len(train_labels))
print(len(train_images))
# sys.exit()
for image in train_images:
    file, ext = os.path.splitext(image)
    labels_path = f"{file.replace('images', 'labels')}.txt"
    if os.path.exists(labels_path):
        shutil.copy(image, r"C:\Users\table\PycharmProjects\MojeCos\ocr_dwa\DatasetPrepTools\train_data\images\val")
        shutil.copy(labels_path, r"C:\Users\table\PycharmProjects\MojeCos\ocr_dwa\DatasetPrepTools\train_data\labels\val")
