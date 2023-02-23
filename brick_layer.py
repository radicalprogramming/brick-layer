from pathlib import Path
import os
import argparse
from PIL import Image

########################### START USER PARAMETERS #############################
HORIZONTAL_OFFSET = 0 # Change this to alter the centering of your image.
                       # negative = left of center, positive = right of center
VERTICAL_OFFSET = 25 # Change this to alter the centering of your image.
                      # negative = down, positive = up

LARGEST_USER_IMAGE_SIZE = 125 # Change this to alter the size of your image

REVERSE = True # Set to "True" if you want the gif reversed

SWAP_TRANSPARENCY_FRAME = 41 # The frame at which to have your image appear
                             # below the brick, instead of above it.
                             # Max = 43, min = 0
############################ END USER PARAMETERS ##############################
  
OPTMIZE_GIF = True # Change this to optimize gif file size

TEMP_FOLDER = 'temp'
BRICK_GIF = Path('./brick_throw.gif') # Relative path to the brick_throw.gif

parser = argparse.ArgumentParser(description='Make an image throw a brick!')
parser.add_argument('image', type=str, help='Path to image')

args = parser.parse_args()

user_image = Path(args.image)

# Check if brick_throw.gif and use image exists
if not BRICK_GIF.is_file():
    print(f"The brick_throw.gif file wasn't found at {BRICK_GIF}!\
            Please put it back.")
    exit(2)
if not user_image.is_file():
    print(f"Couldn't find image at {user_image}.")
    exit(2)
    
while not os.path.exists(TEMP_FOLDER):
    os.makedirs(TEMP_FOLDER)

# Resize user image to have one border be 125, and the other scaled
filename, extension = os.path.splitext(user_image) # grabs the extension
with Image.open(user_image, 'r') as im:
    sizeX = im.size[0]
    sizeY = im.size[1]

    if sizeX >= sizeY:
        ratio = sizeY / sizeX
        scaled_val = round(ratio * LARGEST_USER_IMAGE_SIZE)

        if scaled_val > LARGEST_USER_IMAGE_SIZE: # if in some freak incident where it could round
            scaled_val = LARGEST_USER_IMAGE_SIZE # above the largest dimension that is set, prevent that.
        resized = im.resize((LARGEST_USER_IMAGE_SIZE, round(ratio * LARGEST_USER_IMAGE_SIZE)))
    else:
        ratio = sizeX / sizeY
        scaled_val = round(ratio * LARGEST_USER_IMAGE_SIZE)
        
        if scaled_val > LARGEST_USER_IMAGE_SIZE: # if in some freak incident where it could round
            scaled_val = LARGEST_USER_IMAGE_SIZE # above the largest dimension that is set, prevent that.
        resized = im.resize((scaled_val, LARGEST_USER_IMAGE_SIZE))
    
    temp_img_path = Path(f'{TEMP_FOLDER}/resized{extension}')
    if temp_img_path.is_file():
        os.remove(temp_img_path)
    resized.save(f"{TEMP_FOLDER}/resized{extension}")


# get brick gif frames into a list
print("Cooking up your gif now...")
brick_gif_frames = []
final_gif = []
with Image.open(BRICK_GIF) as brick:
    if SWAP_TRANSPARENCY_FRAME > brick.n_frames - 1:
        print(f"ERROR: SWAP_TRANSPARENCY_FRAME is larger than the number of frames in the gif (was {SWAP_TRANSPARENCY_FRAME}). Max = {brick.n_frames - 1}")
        exit(1)
    user_image_box = Image.new('RGBA', (brick.size[0], brick.size[1]), (255, 255, 255, 0))
    with Image.open(f"{TEMP_FOLDER}/resized{extension}") as im:
        # create a BRICK_GIF_X by BRICK_GIF_Y blank box, put user icon at bottom center
        user_image_box.paste(im, ((round(brick.size[0] / 2.25)) - (im.size[0] // 2) + HORIZONTAL_OFFSET, brick.size[1] - im.size[1] - VERTICAL_OFFSET))
    for frame_num in range(brick.n_frames):
        #brick_gif_frames.append(frame)
        brick.seek(frame_num)
        if frame_num >= SWAP_TRANSPARENCY_FRAME:
            new_frame = Image.alpha_composite(user_image_box, brick.convert("RGBA"))
            brick_gif_frames.append(new_frame)
        else:
            new_frame = Image.alpha_composite(brick.convert("RGBA"), user_image_box)
            brick_gif_frames.append(new_frame)

# save the gif
    temp = 'bricklayer.gif'
    i = 0
    while os.path.exists(temp):
        temp = 'bricklayer' + "_" + str(i) + ".gif"
        i += 1
    brickgif = temp
    if REVERSE:
        brick_gif_frames.reverse()

    brick_gif_frames[0].save(brickgif,
                save_all = True, append_images=brick_gif_frames[1:],
                optimize = OPTMIZE_GIF, duration = 40,
                loop = 0, disposal = 2, version= 'GIF89a')
                
os.remove(f'{TEMP_FOLDER}/resized{extension}') # cleanup
