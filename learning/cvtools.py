"""
cvtools — image processing tools you write yourself in Module 1a.

Each function is the output of one problem. You write the body; once the
test cell in the notebook runs without errors, that problem is done.

    P1  load_bgr, show
    P2  color_mask, apply_mask
    P3  excess_green
    P4  diagnose_exposure
    P5  smooth
    P6  binarize
    P7  edge_map
    P8  find_boxes, draw_boxes
    --- Module 1b ---
    P9  rotate, resize_scale
    P10 crop_boxes
    P11 clean_mask
    P12 combine

The final problems (facade windows v1, v2) only chain these tools together.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------- P1
def load_bgr(path):
    """Reads an image as BGR.

    Raises FileNotFoundError instead of returning None if the file cannot be read.
    """
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(f"Could not read image: {path}")

    return img


def show(*images, titles=None, ncols=None):
    """Displays images side by side.

    2D image → gray colormap.
    3D image → converted from BGR to RGB.
    Turns the axes off. If titles is given, adds a title to each image.
    """
    if len(images) == 0:
        raise ValueError("No images to show")
    n = len(images)
    if titles is not None and len(titles) != n:
        raise ValueError(
            f"Titles not the same length as images: {len(titles)} titles, {n} images")
    if ncols is None:
        ncols = n
    if ncols < 1:
        raise ValueError(f"ncols must be >= 1, got {ncols}")
    nrows = int(np.ceil(n / ncols))

    _, axs = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows), squeeze=False)
    for i, img in enumerate(images):
        r, c = divmod(i, ncols)
        ax = axs[r][c]
        if img.ndim == 2:
            ax.imshow(img, cmap="gray")
        elif img.ndim == 3:
            ax.imshow(
                cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else:
            raise ValueError(f"Unexpected dimension count: {img.ndim}, shape: {img.shape}")
        if titles is not None:
            ax.set_title(titles[i])

    for ax in axs.ravel():
        ax.axis("off")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------- P2
def color_mask(bgr, lower_hsv, upper_hsv):
    """Converts a BGR image to HSV and selects the pixels within the given range.

    Returns: a (H, W) uint8 mask containing only 0 and 255.
    """
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    binary = cv2.inRange(hsv, lower_hsv, upper_hsv)

    return binary


def apply_mask(bgr, mask,resize_mask=False):
    """Sets pixels where the mask is 0 to black and leaves the rest unchanged."""
    m=mask
    if mask.shape != bgr.shape[:2]:
        if resize_mask:
            mask_h, mask_w = bgr.shape[:2]
            m = cv2.resize(
                mask,
                (mask_w, mask_h),
                interpolation=cv2.INTER_NEAREST
            )
        else:
            raise ValueError(f"Mask shape {mask.shape} does not match image {bgr.shape[:2]}")
    result = cv2.bitwise_and(
        bgr,
        bgr,
        mask=m
    )
    return result


# ---------------------------------------------------------------- P3
def excess_green(bgr):
    """Excess Green index: 2·G − R − B.

    Compute in int16, clip the result to the 0–255 range, return uint8.
    Green-dominant areas come out bright, the rest dark.
    """
    B,G,R= cv2.split(bgr)
    B= B.astype("int16")
    G= G.astype("int16")
    R= R.astype("int16")
    exc_g= 2*G-R-B
    exc_green= np.clip(exc_g, 0, 255)
    return exc_green.astype("uint8")


# ---------------------------------------------------------------- P4
def diagnose_exposure(gray):
    """Diagnoses the exposure of a gray image from numbers.

    Returns a dict:
        "mean"         mean intensity
        "dark_ratio"   fraction of pixels with value below 50 (0–1)
        "bright_ratio" fraction of pixels with value above 205 (0–1)
        "suggestion"   dark_ratio > 0.5 → "karanlık",
                       bright_ratio > 0.5 → "aşırı parlak",
                       otherwise → "normal"
                       (these three strings are the exact values to return)
    """
    a= gray.mean()
    b= (gray<50).mean()
    c=(gray>205).mean()

    if b>0.5:
        d="karanlık"
    elif c>0.5:
        d="aşırı parlak"
    else:
        d="normal"

    result= {"mean":float(a),"dark_ratio":float(b),"bright_ratio":float(c),"suggestion":d}

    return result


# ---------------------------------------------------------------- P5
def smooth(img, method="median", k=5):
    """Noise suppression.

    method: "average", "gaussian", "median", "bilateral"
    Raises ValueError if k is not odd or if method is unknown.
    """
    if k%2!=1 or k<1:
        raise ValueError("k value must be odd")
    elif method  not in ["average", "gaussian", "median", "bilateral"]:
        raise ValueError("method must be one of 'average', 'gaussian', 'median', 'bilateral'")

    if method == "average":
        img = cv2.blur(img, (k, k))
    elif method == "gaussian":
        img = cv2.GaussianBlur(img, (k, k), 0)
    elif method == "median":
        img = cv2.medianBlur(img, k)
    elif method == "bilateral":
        img = cv2.bilateralFilter(img, k, 75, 75)

    return img

# ---------------------------------------------------------------- P6
def binarize(gray, method="otsu", invert=False):
    """Converts a gray image to a 0/255 mask.

    method: "otsu", "adaptive" (Gaussian, block 11, C = 2) or an integer (fixed threshold)
    If invert=True, dark regions become 255.
    Raises ValueError for a 3-channel input.
    """
    if np.ndim(gray)==3:
        raise ValueError("expected a single-channel (2D) image")

    if invert:
        tresh_type=cv2.THRESH_BINARY_INV
    else:
        tresh_type=cv2.THRESH_BINARY

    if isinstance(method,str):
        if method == "otsu":
            _, mask = cv2.threshold(
                gray,
                0,
                255,
                tresh_type + cv2.THRESH_OTSU
            )
        elif method == "adaptive":
            mask = cv2.adaptiveThreshold(
                gray,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                tresh_type,
                11,
                2
            )
        else:
            raise ValueError("method must be one of 'otsu', 'adaptive'")
    elif isinstance(method, int):
        _, mask = cv2.threshold(
            gray,
            method,
            255,
            tresh_type
        )
    else:
        raise ValueError("method must be one of 'otsu', 'adaptive' or an integer value")
    return mask

# ---------------------------------------------------------------- P7
def edge_map(gray, low, high, blur_k=0):
    """Canny edge map.

    If blur_k > 0, applies a Gaussian blur of that size before Canny.
    Raises ValueError for a 3-channel input (cv2.Canny does not check this itself).
    """
    if np.ndim(gray)==3:
        raise ValueError("expected a single-channel (2D) image")
    if blur_k<0:
        raise ValueError("must not be negative")

    if blur_k>0 :
        if blur_k % 2 == 0:
            raise ValueError("blur_k must be odd")
        gray=cv2.GaussianBlur(gray,(blur_k,blur_k),0)

    cnn=cv2.Canny(gray,low,high)
    return cnn

# ---------------------------------------------------------------- P8
def find_boxes(mask, min_area):
    """Finds the separate regions in a filled mask.

    Finds contours with RETR_EXTERNAL and discards those with area below min_area.
    Returns: [(x, y, w, h, area), ...], sorted by area from largest to smallest.
    """
    raise NotImplementedError


def draw_boxes(bgr, boxes, color=(0, 255, 0)):
    """Draws the boxes on a copy of the image; does not modify the original."""
    raise NotImplementedError


# ================================================================ Module 1b
# ---------------------------------------------------------------- P9
def rotate(img, angle, expand=True):
    """Rotates the image by angle degrees about its center (positive = counter-clockwise).

    expand=True  → enlarges the canvas so no corner is cut off:
                   new width  = round(h·|sin| + w·|cos|)
                   new height = round(h·|cos| + w·|sin|)
                   (shift the translation part of the rotation matrix to the new center)
    expand=False → size stays the same, corners that overflow are cropped.
    """
    raise NotImplementedError


def resize_scale(img, s):
    """Multiplies the dimensions by s (rounded).

    s < 1 → INTER_AREA, s >= 1 → INTER_LINEAR. Raises ValueError if s <= 0.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- P10
def crop_boxes(bgr, boxes, pad=0):
    """For each (x, y, w, h, ...) box, returns a crop expanded by pad pixels on every side.

    The crop does not extend beyond the image bounds. Each crop is a copy;
    modifying a crop does not modify the original.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- P11
def clean_mask(mask, open_k=3, close_k=5):
    """Opening with an open_k × open_k square kernel first, then closing with close_k × close_k.

    If open_k or close_k is 0, that step is skipped.
    """
    raise NotImplementedError


# ---------------------------------------------------------------- P12
def combine(a, b, op):
    """Combines two 0/255 masks.

    op: "and", "or", "xor", "minus" (a and not b). Raises ValueError for an unknown op.
    """
    raise NotImplementedError
