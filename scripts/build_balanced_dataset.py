import os, random, shutil
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageFile
import numpy as np

ImageFile.LOAD_TRUNCATED_IMAGES = True

# CONFIG
INPUT_DIR = Path("input_images")     # raw input images
OUTPUT_DIR = Path("images")          # output balanced dataset
TARGET_PER_CLASS = 100
TARGET_SIZE = (224,224)
VALID_EXT = {".jpg",".jpeg",".png",".bmp",".tif",".tiff"}

random.seed(42)

def safe_open(p: Path):
    try:
        im = Image.open(p)
        im.verify()
        im = Image.open(p).convert("RGB")
        return im
    except Exception:
        return None

def list_good_images(folder: Path):
    files = [folder / f for f in os.listdir(folder) if (folder / f).suffix.lower() in VALID_EXT]
    good = []
    for f in sorted(files):
        img = safe_open(f)
        if img is not None:
            good.append(f)
    return good

def random_augment(img: Image.Image):
    img = img.copy()
    if random.random() < 0.5: img = img.transpose(Image.FLIP_LEFT_RIGHT)
    if random.random() < 0.2: img = img.transpose(Image.FLIP_TOP_BOTTOM)
    angle = random.uniform(-20, 20)
    img = img.rotate(angle, resample=Image.BICUBIC, expand=False)
    if random.random() < 0.9:
        img = ImageEnhance.Brightness(img).enhance(random.uniform(0.75, 1.25))
    if random.random() < 0.9:
        img = ImageEnhance.Contrast(img).enhance(random.uniform(0.8, 1.3))
    if random.random() < 0.8:
        img = ImageEnhance.Color(img).enhance(random.uniform(0.7, 1.3))
    if random.random() < 0.3:
        img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.3, 1.5)))
    w,h = img.size
    crop_scale = random.uniform(0.75,1.0)
    cw,ch = int(w*crop_scale), int(h*crop_scale)
    left = random.randint(0, max(0,w-cw))
    top = random.randint(0, max(0,h-ch))
    img = img.crop((left,top,left+cw,top+ch)).resize(TARGET_SIZE, Image.BICUBIC)
    if random.random() < 0.4:
        gamma = random.uniform(0.85,1.3)
        arr = np.array(img).astype(np.float32)/255.0
        arr = np.power(arr, gamma)
        arr = (arr*255).clip(0,255).astype(np.uint8)
        img = Image.fromarray(arr)
    return img

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def save_img(img: Image.Image, path: Path):
    try:
        img.save(path, quality=90)
        return True
    except Exception:
        return False

def build():
    if not INPUT_DIR.exists():
        print("ERROR: input_images folder not found:", INPUT_DIR.resolve())
        return
    classes = [p.name for p in INPUT_DIR.iterdir() if p.is_dir()]
    if not classes:
        print("No class folders found inside input_images/")
        return
    print("Found classes:", classes)
    ensure_dir(OUTPUT_DIR)

    for cls in classes:
        src = INPUT_DIR / cls
        dst = OUTPUT_DIR / cls
        ensure_dir(dst)
        good_list = list_good_images(src)
        print(f"\nClass '{cls}': good originals = {len(good_list)}")
        cur = 0
        if len(good_list) >= TARGET_PER_CLASS:
            sample = random.sample(good_list, TARGET_PER_CLASS)
        else:
            sample = list(good_list)
        for p in sample:
            im = safe_open(p)
            if im is None: continue
            im = im.resize(TARGET_SIZE, Image.BICUBIC)
            outp = dst / f"{cls}_orig_{cur:04d}.jpg"
            if save_img(im, outp):
                cur += 1
        print(f"  copied originals -> {cur}")

        attempts = 0
        while cur < TARGET_PER_CLASS and good_list:
            attempts += 1
            src_p = random.choice(good_list)
            im = safe_open(src_p)
            if im is None:
                good_list.remove(src_p)
                continue
            aug = random_augment(im)
            outp = dst / f"{cls}_aug_{cur:04d}.jpg"
            if save_img(aug, outp):
                cur += 1
            if attempts > TARGET_PER_CLASS * 30:
                print("  too many attempts, stopping augmentation")
                break
        print(f"  final count = {cur} (attempts {attempts})")
    print("\n✅ Done. Balanced dataset written to:", OUTPUT_DIR.resolve())

if __name__ == "__main__":
    build()
