from libraries import *


""" Resize image to any dimension. """  
""" Param : folder_name : The folder source of all the images, 
            to_folder : The folder destination,
            img : image name, 
            new : The new image name
            i : The number of image when it's saved, 
            w : The width of the image,
            h : The height of the image. """

def resize_image(from_folder, to_folder, img, new, i, w, h):
    # Path folder to the image
    p = f"{from_folder}/{img}"

    # Open the image to be able to resize it
    default_image = Image.open(p)
    resized_img = default_image.resize((w, h)) # width, height

    # Save as the image with any name
    name = f"{to_folder}/{new}{i}.png"
    resized_img.save(name)

    nb = i + 1
    print(f"Successful : resize_image number {nb}")



""" Get how many items their is in the folder. """
def get_nb_files(folder):
    lst = os.listdir(folder)
    number_files = len(lst)
    print("Successful : get_nb_files")

    return number_files



""" Resize all the images from folder A and put them in folder B. """
""" Param : folder_name : The folder source of all the images, 
            to_folder : The folder destination,
            name_img : The images standard names,
            w : The width of the image,
            h : The height of the image. """

def resize_image_folder(from_folder, to_folder, name_img, w, h):
    
    # Add the new folder name
    new_folder = f"{to_folder}"
    os.mkdir(new_folder)

    # List contains all the images name to resize
    images_list = []

    # Add all the images to the list of images
    for image in os.listdir(from_folder):
        if image.endswith(".png"):
            images_list.append(image)

    # Resize all the images 
    for j in range(len(images_list)):
        resize_image(from_folder, to_folder, images_list[j], name_img, j, w, h)

    print("Successful : resize_image_folder")



""" Move folder from source to destination. """
def move_folder(source, destination):
    shutil.move(source , destination)
    print("Successful : move_folder")



""" Create video. """
""" Param : folder_big : name of the folder with big size images,
            folder_small : name of the folder with small size images,
            tmp_video : name of the temporary video that will be deleted,
            final_name : The name of the video at the end,
            p1 : path for the folder with big dimension images,
            p2 : path for the folder with small dimension images,
            f1 : logo of anime land path,
            f2 : whos next logo image,
            f3: watermark image. """

def create_video(path1, path2, tmp_video, final_name, f1, f2, f3):
    
    # folder Paths
    p1 = os.listdir(path1)
    p2 = os.listdir(path2)


    # Add all the big dimension images to clips
    clips = []
    clips.append(ImageClip(f1).set_duration(2))

    # Acces the images in the file
    for filename in p1:
        if filename.endswith(".png"):
            clips.append(ImageClip(f'{path1}/{filename}').set_duration(2))


    # Create a video with only the big dimension images
    video = concatenate(clips, method="compose")
    video.write_videofile(tmp_video, fps=1)

    clips_mini = []
    count = 11
    for filename in p2:
        if filename.endswith(".png"):
            clips_mini.append(ImageClip(f'{path2}/{filename}').set_start(count)
            .set_duration(1)
            .set_pos("center","center"))
            count -= 2


    clips_mini.append(ImageClip(f2).set_start(12)
            .set_duration(1))

    video = mp.VideoFileClip(tmp_video)

    watermark = ImageClip(f3).set_duration(13)

    # The combination of all the images in the video 
    final = mp.CompositeVideoClip([video, clips_mini[0], clips_mini[1], clips_mini[2], clips_mini[3], clips_mini[4], clips_mini[5], watermark])
    final.write_videofile(final_name)

    # Delete the temporary video
    remove_file(tmp_video)


def remove_file(name):
    os.remove(name)



""" Make a video by calling all the function needed and pass the parms. """

def make_video(default_folder, folder_big, name_big, big_width, big_height,
                folder_small, name_small, small_width, small_height,
                path_source_big, path_destination,
                path_source_small,
                p1, p2, tmp_video, final_name, f1, f2, f3,
                path_video_from, path_video_to) :
    
    # Resize images in new folder.
    resize_image_folder(default_folder, folder_big, name_big, big_width, big_height) # Big
    resize_image_folder(default_folder, folder_small, name_small, small_width, small_height) # Small

    # Move folder from source to destination.
    move_folder(path_source_big, path_destination) # Big
    move_folder(path_source_small, path_destination) # Small

    # Create the video.
    create_video(p1, p2, tmp_video, final_name, f1, f2, f3)

    # Move the video to not posted.
    move_folder(path_video_from, path_video_to)


