from moviepy.editor import CompositeVideoClip, ImageClip, ColorClip
from moviepy.video.fx import margin
from moviepy.editor import clips_array
import moviepy.editor as mp

p = "/Users/abedelzubaidi/Desktop/all/tiktok/rent a girlfriend/s1/rent a girlfriend S1 E2.mp4"
image_path = "/Users/abedelzubaidi/Desktop/all/tiktok/tools/cardre twitter.png"  

def extract_info_from_title(title):
    """Extract anime name, season, and episode from the title."""
    parts = title.split(" ")
    anime_name = " ".join(parts[:-2])
    season = parts[-2][1]
    episode = parts[-1][1:]
    return anime_name, season, episode

def divide_and_save(video_path, title, image_path):
    """Divide the video into multiple parts and save them."""
    # Extract video info
    anime_name, season, episode = extract_info_from_title(title)
    
    # Load video
    clip = mp.VideoFileClip(video_path)
    
    # Ensure each part is at least 2 minutes long
    total_duration = clip.duration
    num_parts = int(total_duration / 180)  # Each part is 3 minutes (180 seconds)

    part_duration = total_duration / num_parts
    for i in range(num_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration

        # Extract and resize the video part
        video_part_resized = clip.subclip(start_time, end_time)
        video_part_resized = video_part_resized.resize(newsize=(1080, 1920))

        # Extract, resize and set the position of the video fit in
        video_part_fit_in = clip.subclip(start_time, end_time)
        video_part_fit_in = video_part_resized.resize(newsize=(962, 580))
        video_part_fit_in = video_part_fit_in.set_position((58, 660))
        
        # Load the image (assuming it has the same dimensions as the resized video)
        image_clip = ImageClip(image_path).set_duration(video_part_resized.duration)
        
        # Composite the resized video and the image (with the image on top)
        final_video = CompositeVideoClip([video_part_resized, video_part_fit_in, image_clip])

        # Export the final video
        output_name = f"{anime_name} S{season} E{episode} p{i+1}.mp4"
        final_video.write_videofile(output_name, fps=24,codec="mpeg4", audio_codec='aac')

# call
divide_and_save(p, "rent a girlfriend S1 E2", image_path)
