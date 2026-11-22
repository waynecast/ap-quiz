"""Paint out the printed labels on each handout image (for the Find-it mode)."""
import cv2, numpy as np, sys, os
from diagram_coords import COORDS
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for name, items in COORDS.items():
    im = cv2.imread(f"{src}/{name}.jpg")
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    H, W = g.shape
    mask = np.zeros_like(g)
    for key, (_, glyphs) in items.items():
        wide = len(str(key)) > 1
        for x, y, on_bone in glyphs:
            if on_bone:
                hw, hh = (40 if wide else 26), 28
                cv2.rectangle(mask, (x - hw, y - hh), (x + hw, y + hh), 255, -1)
            else:
                hw, hh = (34 if wide else 22), 24
                x0, x1, y0, y1 = max(0, x - hw), min(W, x + hw), max(0, y - hh), min(H, y + hh)
                win = g[y0:y1, x0:x1] < 140
                ys, xs = np.nonzero(win)
                if len(xs):
                    cv2.rectangle(mask, (x0 + xs.min() - 5, y0 + ys.min() - 5), (x0 + xs.max() + 5, y0 + ys.max() + 5), 255, -1)
    clean = cv2.inpaint(im, mask, 7, cv2.INPAINT_TELEA)
    cv2.imwrite(f"{out}/{name}.jpg", clean, [cv2.IMWRITE_JPEG_QUALITY, 85])
    print(name)
