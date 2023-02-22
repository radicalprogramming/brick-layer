# brick-layer
This will take an image and make it appear as if it is throwing a brick at the viewer in the form of a GIF file.

![bricklayer gif_7](https://user-images.githubusercontent.com/125831679/220438381-a4779e73-3672-4f9e-a51c-e78831460444.gif)

# How To Run
 1. Download this repository by clicking the green "<> Code" button at the top right and click "Download ZIP"
 2. Install Python 3: https://www.python.org/downloads/
    -  Important! Make sure you check Add python.exe to PATH in the installer.
    -  ![image](https://user-images.githubusercontent.com/125831679/220442718-d8d35b9e-6db0-4285-ab5e-69a587398014.png)
 3. Install the Pillow module after installing Python:
    -  open a cmd prompt/terminal
    -  run `pip install pillow`
 4. Navigate to the directory where this Python script is:
    - In a cmd prompt/terminal, run: `cd [path to this script]`
    - Or, shift-right click in the folder with this script, and click "open PowerShell window here"
 5. Run the script: `py brick_layer.py [path to your image]`
    - I.e `py brick_layer.py myimage.png`
 6. The gif will be exported in the current folder.

# Changing the Output
You can change how your image appears by changing some settings at the top of the script.

`HORIZONTAL_OFFSET`: Increase this to move your image to the right, decrease this to move it left.

`VERTICAL_OFFSET`: Increase this to move your image to the up, decrease this to move it down.

`LARGEST_USER_IMAGE_SIZE`: Changes the size (in pixels) of the largest dimension of your image.

`SWAP_TRANSPARENCY_FRAME`: [ADVANCED] Change the frame in the `brick_throw.gif` in which it draws above your image instead of behind it.

# Acknowledgements
[GIMP](https://www.gimp.org/) for editing the `brick_throw.gif` file.

[ezgif](https://ezgif.com/) for an amazing website that has many powerful gif editing tools for FREE.

[Pillow Image Library](https://pypi.org/project/Pillow/) for a powerful Python image library that resizes and generates the gif.

Rocco Tocco: For reviewing the How To Run procedure.
