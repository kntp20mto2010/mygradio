import os
import shutil
import time

SRC_DIR = "/FramePack/outputs/"
DST_DIR = "/notebooks/FramePack/results/"

def wait_for_complete_write(filepath, wait_time=1.0, max_wait=10):
    last_size = -1
    stable_time = 0
    total_time = 0
    while total_time < max_wait:
        try:
            size = os.path.getsize(filepath)
        except Exception:
            size = -1
        if size == last_size and size > 0:
            stable_time += wait_time
            if stable_time >= wait_time * 2:
                return True
        else:
            stable_time = 0
        last_size = size
        time.sleep(wait_time)
        total_time += wait_time
    return False

def move_new_images():
    for fname in os.listdir(SRC_DIR):
        if fname.endswith('.png'):
            src_path = os.path.join(SRC_DIR, fname)
            dst_path = os.path.join(DST_DIR, fname)
            if not os.path.exists(dst_path):
                if wait_for_complete_write(src_path):
                    shutil.move(src_path, dst_path)
                    print(f"Moved {fname} to results/")
                else:
                    print(f"File write not completed in time: {fname}")

if __name__ == "__main__":
    while True:
        move_new_images()
        time.sleep(2)