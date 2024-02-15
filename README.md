# TikTok Video Creation Toolkit
This repository offers a versatile toolkit for creating various types of vertical videos, specifically designed for platforms like TikTok. With this toolkit, users can generate videos from images, quotes, or even break down existing videos into smaller segments for easy posting.

## Video Types
The toolkit supports the creation of three distinct types of videos:


1. **Wallpaper Background Videos:** Generate videos from images intended as phone wallpapers.
2. **Quote-Based Videos:** Create videos that visually present quotes.
3. **Segmented Videos from a Single Source:** Divide a longer video into multiple shorter segments suitable for TikTok posts.


## Prerequisites
Before using the toolkit, ensure the following setup is complete:

### For All Videos:

Create a folder named not_posted at the parent level of this repository's folder. This is where the newly created videos will be saved.
Prepare two images: one to display at the beginning and another for the end of your videos, along with an image for watermarks.

### For Quote-Based Videos:

- Outside the repository's folder, create a folder named quotes.
- Inside quotes, create a text file named quote.txt and format it as follows:
```
quote number: 1
1# “Your quote here” - Author (Source)
```
- Ensure the format is followed precisely to avoid errors. The quote number will update automatically.
- Create another folder at the same level as `quotes`, named `clips`. Within `clips`, create subfolders named after anime series and populate them with relevant video clips. 
The toolkit will select a clip randomly for each video.

### For Segmented Videos:

- Create a folder named `anime series` at the same level as `quotes`. Within this folder, create subfolders for each anime series (e.g., `S1`, `S2`, etc.).
- Additionally, create a text file named `anime_book` at the same parent level, formatting it as follows:

```
# one piece
@ s1
*E1 done
*E2 done
...
```
Follow the format strictly for proper operation.

## Getting Started
With the prerequisites in place, you're ready to create videos with a single click. This toolkit is designed to streamline the video creation process for TikTok content creators, offering a range of customization options to suit different themes and preferences.

Contribution
Feedback and contributions to this project are welcome.
