import os
import shutil
import time

SRC_DIR = "/FramePack/outputs/"
DST_DIR = "/notebooks/FramePack/results/"

def move_new_images():
    for fname in os.listdir(SRC_DIR):
        if fname.endswith('.png'):
            src_path = os.path.join(SRC_DIR, fname)
            dst_path = os.path.join(DST_DIR, fname)
            # resultsに同名ファイルがなければ移動
            if not os.path.exists(dst_path):
                shutil.move(src_path, dst_path)
                print(f"Moved {fname} to results/")

if __name__ == "__main__":
    while True:
        move_new_images()
        time.sleep(2)  # 5秒ごとにチェック