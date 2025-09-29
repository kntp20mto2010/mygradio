from PIL import Image, ImageOps
import os
import argparse
def resize_to_square(input_path, output_path, size=1024, bg_color=(255, 255, 255)):
    img = Image.open(input_path)
    img = img.convert("RGB")
    img = img.resize((int(img.width * size / max(img.size)), int(img.height * size / max(img.size))), Image.LANCZOS)
    new_img = Image.new("RGB", (size, size), bg_color)
    paste_x = (size - img.width) // 2
    paste_y = (size - img.height) // 2
    new_img.paste(img, (paste_x, paste_y))
    new_img.save(output_path)

def resize_images_in_folder(folder_path, size=1024, bg_color=(255, 255, 255)):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
            input_path = os.path.join(folder_path, filename)
            output_path = input_path  # 上書き保存
            resize_to_square(input_path, output_path, size=size, bg_color=bg_color)

def parse_bg_color(bg_color_str):
    parts = bg_color_str.split(',')
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("Background color must be R,G,B")
    return tuple(int(x) for x in parts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images in a folder to square.")
    parser.add_argument("--folder", help="Path to the folder containing images")
    parser.add_argument("--size", type=int, default=1024, help="Target square size (default: 1024)")
    parser.add_argument("--bg_color", type=parse_bg_color, default=(255,255,255), help="Background color as R,G,B (default: 255,255,255)")
    args = parser.parse_args()
    resize_images_in_folder(args.folder, size=args.size, bg_color=args.bg_color)