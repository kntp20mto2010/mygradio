import os
from PIL import Image

def slice_grid(
    input_path,
    output_dir,
    width,
    height,
    base_name="pose"
):
    os.makedirs(output_dir, exist_ok=True)
    img = Image.open(input_path)
    img_w, img_h = img.size

    count = 1
    for top in range(0, img_h, height):
        for left in range(0, img_w, width):
            box = (left, top, left + width, top + height)
            cropped = img.crop(box)
            out_name = f"{base_name}_{count:03d}.png"
            out_path = os.path.join(output_dir, out_name)
            cropped.save(out_path)
            print(f"Saved: {out_path}")
            count += 1

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Slice grid image into sub-images.")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--output_dir", required=True, help="Output directory")
    parser.add_argument("--width", type=int, required=True, help="Width of each slice")
    parser.add_argument("--height", type=int, required=True, help="Height of each slice")
    parser.add_argument("--base_name", default="pose", help="Base name for output files")
    args = parser.parse_args()

    slice_grid(
        input_path=args.input,
        output_dir=args.output_dir,
        width=args.width,
        height=args.height,
        base_name=args.base_name
    )
