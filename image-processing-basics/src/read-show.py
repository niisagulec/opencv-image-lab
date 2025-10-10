import cv2
import os

# ensure output directory exists (relative to src -> ../outputs)
base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, '..', 'assets', 'images')
output_dir = os.path.join(base_dir, '..', 'outputs')
os.makedirs(output_dir, exist_ok=True)

def load_image(name):
    path = os.path.join(assets_dir, name)
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    return img

def safe_imwrite(path, img):
    ok = cv2.imwrite(path, img)
    if not ok:
        raise IOError(f"Failed to write image: {path}")

# kahlo
img = load_image('kahlo.jpg')
cv2.imshow('kahlo', img)
cv2.waitKey(0)
safe_imwrite(os.path.join(output_dir, 'kahlo_copy.jpg'), img)

# ny
img = load_image('ny.jpg')
cv2.imshow('ny', img)
cv2.waitKey(0)

# manzara
img = load_image('manzara.jpg')
cv2.imshow('manzara', img)
cv2.waitKey(0)

# sepet
img = load_image('sepet.jpg')
cv2.imshow('sepet', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
