import os, random
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageFile, UnidentifiedImageError
import numpy as np
ImageFile.LOAD_TRUNCATED_IMAGES = True

INPUT_DIR = Path("input_images")
OUTPUT_DIR = Path("images")
TARGET_PER_CLASS = 100
VALID_EXT = {".jpg", ".jpeg", ".png", ".bmp"}

random.seed(42)

def list_images(folder):
    return [p for p in folder.iterdir() if p.suffix.lower() in VALID_EXT]

def random_augment(img):
    if random.random() < 0.5: img = img.transpose(Image.FLIP_LEFT_RIGHT)
    if random.random() < 0.2: img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img = img.rotate(random.uniform(-20,20), resample=Image.BICUBIC, expand=False)
    if random.random() < 0.9: img = ImageEnhance.Brightness(img).enhance(random.uniform(0.7,1.3))
    if random.random() < 0.9: img = ImageEnhance.Contrast(img).enhance(random.uniform(0.8,1.4))
    if random.random() < 0.8: img = ImageEnhance.Color(img).enhance(random.uniform(0.6,1.4))
    if random.random() < 0.3: img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.5,1.8)))
    w,h = img.size
    crop_scale = random.uniform(0.7,1.0)
    cw,ch = int(w*crop_scale), int(h*crop_scale)
    left,top = random.randint(0,max(0,w-cw)), random.randint(0,max(0,h-ch))
    img = img.crop((left,top,left+cw,top+ch)).resize((224,224),Image.BICUBIC)
    if random.random() < 0.4:
        gamma = random.uniform(0.8,1.4)
        arr = np.array(img).astype(np.float32)/255.0
        arr = np.power(arr,gamma)
        img = Image.fromarray((arr*255).clip(0,255).astype(np.uint8))
    return img

def ensure_output_class(folder): folder.mkdir(parents=True, exist_ok=True)

def main():
    print("INPUT_DIR:", INPUT_DIR.resolve())
    print("OUTPUT_DIR:", OUTPUT_DIR.resolve())
    classes = [p.name for p in INPUT_DIR.iterdir() if p.is_dir()]
    if not classes: print("No classes found inside", INPUT_DIR); return

    for cls in classes:
        src, dst = INPUT_DIR/cls, OUTPUT_DIR/cls
        ensure_output_class(dst)
        src_imgs = list_images(src)
        if not src_imgs:
            print(f"WARNING: no images found for class {cls}")
            continue
        idx = 0
        for p in src_imgs:
            try:
                im = Image.open(p).convert("RGB")
                outp = dst / f"{cls}_orig_{idx:04d}.jpg"
                im.resize((224,224), Image.BICUBIC).save(outp, quality=90)
                idx += 1
            except (OSError, UnidentifiedImageError) as e:
                print(f"⚠️  Skipping unreadable file {p.name}: {e}")
        cur = len(list_images(dst))
        while cur < TARGET_PER_CLASS:
            try:
                im = Image.open(random.choice(src_imgs)).convert("RGB")
                aug = random_augment(im)
                aug.save(dst / f"{cls}_aug_{cur:04d}.jpg", quality=90)
                cur += 1
            except Exception as e:
                print(f"⚠️  Augment skip: {e}")
                continue
        print(f"{cls} final count = {cur}")

if __name__ == "__main__":
    main()
