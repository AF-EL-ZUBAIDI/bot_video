from moviepy.editor import CompositeVideoClip, ImageClip, ColorClip
from moviepy.video.fx import margin
from moviepy.editor import clips_array
import moviepy.editor as mp
import os
import re

# Paths
base_directory = "../anime series"
txt_file_path = os.path.join(base_directory, "anime_book.txt")
image_path = "../tools/cardre twitter.png"  


def find_next_episode():
    """Find the next episode to process from the txt file."""
    with open(txt_file_path, "r") as file:
        lines = file.readlines()

    anime_name = None
    season_name = None
    for i, line in enumerate(lines):
        
        # Check for anime name
        if re.match(r"^#\s+", line):
            anime_name = line[2:].strip()

        # Check for season
        elif re.match(r"^@\s+", line):
            season_name = line[3:].strip()

        # Check for episode not done
        elif re.match(r"^\*\s+", line) and "done" not in line:
            episode_name = line[2:].split()[0]
            print(f"Anime in process: {anime_name} - {season_name} - {episode_name}")  # Debug print
            return anime_name, season_name, episode_name, i

    return None, None, None, None


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
    
    # Ensure each part is at least 3 minutes long
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
        final_video.write_videofile(output_name, fps=30,codec="mpeg4", audio_codec='aac')

def process_anime_updated():
    anime_name, season_name, episode_name, line_index = find_next_episode()

    # If no episode is found, exit
    if not episode_name:
        print("All episodes processed!")
        return

    video_path = os.path.join(base_directory, anime_name, season_name, f"{anime_name} {season_name} {episode_name}.mp4")
    title = f"{anime_name} {season_name} {episode_name}"
    
    divide_and_save(video_path, title, image_path)

    # Mark this episode as done in txt file
    with open(txt_file_path, "r") as file:
        lines = file.readlines()
    lines[line_index] = f"*{episode_name} done\n"
    with open(txt_file_path, "w") as file:
        file.writelines(lines)

    print(f"Finished processing {title}!")

# run 
# process_anime_updated()
