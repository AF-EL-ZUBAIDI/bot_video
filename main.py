from libraries import *
from type1 import *
from type2 import *
from type3 import *

# Dimension of the video size for the images.
big_width = 1080
big_height = 1920

small_width = big_width//2
small_height = big_height//2


while True:
    # Answer to chose between a wallpaper video or a quote video
    try:
        answer = int(input("\n>> Choose between producing a wallpaper video, a quote video, or entering anything to quit :\n>> 1. Wallpaper video.\n>> 2. Quote Video.\n>> 3. Anime serie.\n>> Answer : "))

        # Make a wallpaper video
        if answer == 1:
            # That is the number of the folder to take images from.
            nb_file = int(input("\n>> Enter the number of the folder : "))

            # Name of all the folders : The default, The folder with big and small resize.
            default_folder = f'../wallpapers/wallpaper {nb_file}'
            folder_big = f'wallpaper_big_{nb_file}'
            folder_small = f'wallpaper_small_{nb_file}'

            # Params for the creation of the video.
            tmp_video = "tmp.mp4"
            final_name = f'wallpaper part {nb_file}.mp4'

            # Paths.
            p1 = f'{default_folder}/{folder_big}'
            p2 = f'{default_folder}/{folder_small}'

            f1 = "./logo_video/logo_anime_land.png"
            f2 = "./logo_video/whos next logo.png"
            f3 = "./logo_video/watermark_done.png"


            # Name of the resized images.
            name_big = "anime_big_"
            name_small = "anime_small_"


            # All the path from to.
            path_source_big = f'./{folder_big}'
            path_source_small = f'./{folder_small}'
            path_destination =  f'../wallpapers/wallpaper {nb_file}'
            path_video_from = f'./{final_name}'
            path_video_to = f'../not posted'

            # # function that contain all the paramas to use other function to make a video
            make_video(default_folder, folder_big, name_big, big_width, big_height,
                            folder_small, name_small, small_width, small_height,
                            path_source_big, path_destination,
                            path_source_small,
                            p1, p2, tmp_video, final_name, f1, f2, f3,
                            path_video_from, path_video_to)
            break
        
        elif answer == 2:
            # The folders names for the clips, the quotes and the where is the video saved at the end
            clips = "clips"
            quotes = "quotes"
            dst_folder = "not posted"

            # Make a video with a clip of anime and a quote from it
            make_clip_quote(clips, quotes, dst_folder)
            break

        elif answer == 3:
            process_anime_updated()
            break
                
        else: 
            print("\nWrong choice!\n>> Choose between producing a wallpaper video, a quote video, or entering anything to quit :\n>> 1. Wallpaper video.\n>> 2. Quote Video.\n>> Anything else to quit.\n>> Answer : ")
    
    except FileNotFoundError as error_file:
        print(error_file)
        break
    
    except ValueError as error_value :
        print(error_value)
        break
      

