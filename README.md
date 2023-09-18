# Pixel 
Adds various useful tools for pixel art to the Extras tab.

### Purpose
This extension is used to fix asymmetrical pixels in AI-generated pixel art through downscaling.
It also can be used to limit color palette and clamp grayscale values to get more stylized results. You can also use the rescale feature to get a higher resolution image (best for preview on the webui canvas).

For use with this [webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

# Installation Guide
Make sure you install ImageMagick first, otherwise the Wand module that the Python script attempts to use (for palette-specifidc palettization) will fail.

Install from webui's Extensions tab.

Extensions > Install from URL > Paste `https://github.com/Leodotpy/sd-pixel.git` > Install

Or install via the extensions menu by searching for "Pixel".

(Restart the webui via the Extensions menu to load the extension. If you run into issues loading the extension, reboot the app completely)

# Feature Comparison Examples

| Effect              | Before                              | After                                 |
|---------------------|-------------------------------------|---------------------------------------|
| Downscale           | ![](examples/before-downscale2.png) | ![](examples/after-downscale2.png)    |
| Color Palette Limit | ![](examples/before-palette.png)    | ![](examples/after-palette.png)       |
| Gray Limit          | ![](examples/before-gray.png)       | ![bad apple](examples/after-gray.png) |

### Supported Downscaling Modes

| *Original*                            |  | Nearest                           | Bicubic                           | Bilinear                           | Hamming                           | Lanczos                           |
|---------------------------------------|--|-----------------------------------|-----------------------------------|------------------------------------|-----------------------------------|-----------------------------------|
| <img src="examples/before-mode.jpeg"> |  | <img src="examples/Nearest.jpeg"> | <img src="examples/Bicubic.jpeg"> | <img src="examples/Bilinear.jpeg"> | <img src="examples/Hamming.jpeg"> | <img src="examples/Lanczos.jpeg"> |



### Credits
* Thanks AUTOMATIC1111 for an awesome sd webui

