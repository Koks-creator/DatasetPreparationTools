from pathlib import Path
from typing import Union
import logging
import os


class Config:
    ROOT_PATH: str = Path(__file__).resolve().parent
    RAW_DATA_PATH: str = fr"{ROOT_PATH}/RawData"
    CLEANED_DATA_PATH: str = fr"{ROOT_PATH}/DataCleaned"
    TRAIN_IMAGES_FOLDER: str = fr"{ROOT_PATH}/train_data/images/train"
    VAL_IMAGES_FOLDER: str = fr"{ROOT_PATH}/train_data/images/val"
    TRAIN_LABELS_FOLDER: str = fr"{ROOT_PATH}/train_data/labels/train"
    VAL_LABELS_FOLDER: str = fr"{ROOT_PATH}/train_data/labels/val"
    TEST_DATA_FOLDER: str = fr"{ROOT_PATH}/TestData"
    CLASSES_PATH: str = fr"{ROOT_PATH}/classes.txt"
    MIN_HEIGHT: int = 180
    MIN_WIDTH: int = 180
    MAX_HEIGHT: int = 4000
    MAX_WIDTH: int = 4000
    ALLOWED_EXTENSIONS: tuple = (".jpg", ".png", ".jpeg")

