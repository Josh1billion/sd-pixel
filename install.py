import launch

# This extension uses cv2 for image effects
if not launch.is_installed("opencv-python"):
    launch.run_pip("install opencv-python", "opencv-python")

# Uses wand for palette reduction
if not launch.is_installed("wand"):
    launch.run_pip("install wand", "wand")

for dep in ['onnxruntime', 'pymatting', 'pooch', 'opencv-python']:
    if not launch.is_installed(dep):
        launch.run_pip(f"install {dep}", f"{dep} for pixel extension")