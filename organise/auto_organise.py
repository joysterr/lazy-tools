#!/usr/bin/env python3

import os
import shutil

user = os.path.expanduser("~")
source = f'{user}/Downloads'
dest_images = f'{source}/Images'
dest_pdfs = f'{source}/PDF'
dest_installer = f'{source}/Installers'
dest_audio = f'{source}/Audio'
dest_video = f'{source}/Video'

destinations_arr = [dest_images, dest_pdfs, dest_installer, dest_audio, dest_video]
all_files = os.listdir(source)


def check_folders():
    for dir in destinations_arr:
        if not os.path.exists(dir):
            os.mkdir(dir)
            print(f'Created new folder: {dir}')
        else:
            continue
    print("Folder checks complete. OK to proceed.")


def move_files():
    for f in all_files:
        src_path = os.path.join(source, f)
        if f.endswith("jpg") or f.endswith("jpeg") or f.endswith("png") or f.endswith("heif") or f.endswith("raw") or f.endswith("svg") or f.endswith("webp"):
            dst_path = os.path.join(dest_images, f)
            shutil.move(src_path, dst_path)
        elif f.endswith("pdf"):
            dst_path = os.path.join(dest_pdfs, f)
            shutil.move(src_path, dst_path)
        elif f.endswith("dmg") or f.endswith("pkg") or f.endswith("exe"):
            dst_path = os.path.join(dest_installer, f)
            shutil.move(src_path, dst_path)
        elif f.endswith("mp3") or f.endswith("wav") or f.endswith("flac") or f.endswith("alac"):
            dst_path = os.path.join(dest_audio, f)
            shutil.move(src_path, dst_path)
        elif f.endswith("mp4") or f.endswith("mov") or f.endswith("avi"):
            dst_path = os.path.join(dest_video, f)
            shutil.move(src_path, dst_path)
        else:
            continue
    print("Downloads Folder is now auto-organised.")
               

check_folders()
move_files()