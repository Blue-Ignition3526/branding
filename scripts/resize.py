import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help="Input image")
parser.add_argument("-s", "--size", "--sizes", required=True, help="Comma-separated output sizes: 100x100,200x200,...")
parser.add_argument("-d", "--dest", "--destination", required=False, help="File output destination")
parser.add_argument("-n", "--name", "--naming", required=False, help="Naming variables: {name} (source name), {size} (image size), {format} (image format). Default: {name}-{size}.{format}", default="{name}-{size}.{format}")
args = parser.parse_args()

fp = os.path.abspath(args.input)
fp_dir = os.path.dirname(fp)
fp_fbn = os.path.basename(fp).split(".")
fp_fln = fp_fbn[0]
fp_fmt = ".".join(fp_fbn[1:])
image = Image.open(fp)

for size in args.size.split(","):
    print(f"Generating {size} Image")
    
    dest = args.dest
    if not dest:
        dest = fp_dir
    
    [xres, yres] = size.split("x")
    new_image = image.resize((int(xres), int(yres)), Image.Resampling.BILINEAR)
    new_image.save(os.path.join(dest, str(args.name).format(name=fp_fln, size=size, format=fp_fmt)))