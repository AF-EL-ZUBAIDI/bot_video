from libraries import *


""" Get the number of quote to take for the day.
    The number of the quote to take is in the first line 
    in the file quote.txt."""

def get_the_quote_nb():

    # Go into the Folder quotes
    folder_path = '../quotes'
    os.chdir(folder_path)

    # open the file
    with open('quote.txt', 'r') as file:
        # read the first line of the file
        first_line = file.readline()

        # split the line by the word 'number' and take the second part
        parts = first_line.split(':')
        number_string = parts[1]

        # remove any whitespace from the beginning and end of the string
        number_string = number_string.strip()

        # try to convert the string to an integer
        try:
            nb = int(number_string)
        except ValueError:
            # if the string is not a number, print a message
            print("No number was found in the first line of the file.")
        else:
            # if the string was converted to a number successfully, return the value of the `nb` variable
            return nb




""" Update the quote number so I never get the same quote twice. """

def update_quote_number():

    # Go into the Folder quotes
    folder_path = '../../quotes'
    os.chdir(folder_path)

    # Change the value of the quote number
    nb = get_the_quote_nb() + 1
    with open('quote.txt', 'r') as file:
        lines = file.readlines()

    # change the line -> update the number at the end of the line
    lines[0] = f"quote number : {nb}\n"
       
    # Write all the changes
    with open('quote.txt', 'w') as file:
        file.writelines(lines)

    file.close()




""" Read the file that contain the quotes.
    I store all the quotes in a list then I return the quote of the day. 
    I get this quote from the quote number that is in the beginning of the file.
    Param : display : boolean to print or no the messages on the quote details.
            quotes : the folder where are the quotes. """

def read_file(display, quotes):
    
    # Variables for quotes
    quote_list = []
    quote_str = ""

    # Go into the Folder quotes
    folder_path = f'../{quotes}'
    os.chdir(folder_path)

    # Open the file in read mode
    with open('quote.txt', 'r') as file:
    
        # Initialize a counter
        line_count = 0

        # Iterate over the lines in the file
        for line in file:

            # reset quote_str to stock a new quote
            quote_str = ""

            # It's not an empty return line 
            if line != "\n":
                quote_str += line
           
            # if the quote is not empty then I will added to the list
            if quote_str != "":
                quote_list.append(quote_str)

            # update the counter
            line_count += 1

        # Get the number for the quote of the day
        quote_day = get_the_quote_nb()
        
        valid_nb = False

        # Get the quote of the day
        for i in range(len(quote_list)):
            
            if quote_day == i: 
                # Remove the nb# then I remove the extra spaces
                res = quote_list[i].split("#")
                res[1] = res[1].strip()
                val = res[1]
                valid_nb = True

        if valid_nb == True:
            if display == True:
                print("\nThe quote of the day is number : ", quote_day)
                print("\nToday the quote is ", val)
            file.close()
            return val

        else:
            if display == True:
                print("No more quotes.")
            file.close()
            return None    



""" Create a list that each element of it is a line to display
    quote correctly in the rectangle.
    Param : quotes : the folder where are the quotes. """

def quote_list(quotes):
    
    # If there is more new quotes
    try:
        # Get the quote of the day
        quote = read_file(True, quotes)
                
        # Store each word in the list words
        words = quote.split(' ')

        # Res will contain each line that will appear in the rectangle alone 
        res = []

        # It's of each word in the list words
        len_words = 0

        # Iterator i on the length of the list words and loss take the number of word that didn't get into res
        i = 0

        # Store temporary stock words for each sentence on each line
        tmp = ""

        # While there is words in word list 
        while i < len(words) :

            # The length of sentence must be not over 45 to always fit in the rectangle box
            if len(tmp) + len(words[i]) + 1 < 45:
                # Reset every time I'm in a new sentence
                last_word = ""

                # Adding the word + space beteween words for the sentence 
                tmp += words[i] + " "

                # Update the sentence the len_words length and update the i
                len_words += len(words[i]) + 1
                i += 1

            # The sentence is more than 45 characters (inluded spaces means) I should return to the line
            else:
                res.append(tmp)
                # Reset tmp 
                tmp = ""

        # if the rest of the words length < 45 in the end of the quote I have 
        # to added after the while loop because at the end theif condition
        # was always right so I didn't the last line stored int tmp to res
        res.append(tmp)

        print("\nQuote resized correctly!")
        return res

    except AttributeError:
        print("Attribute Error : No more quotes today!")

    except UnboundLocalError:
        print("Unbound Local Error : forgot to bind something ? Maybe words")




""" Return the anime name of the quote of the day.
    Param : display : boolean to print or no the messages on the quote details.
            quotes : the folder where are the quotes. """

def get_anime_name(display, quotes):
    
    # Get the quote of the day
    quote = read_file(display, quotes)
    
    # Get the name of the anime at the end of the quote with regex
    match = re.search(r'\(([^)]+)\)', quote)
    
    # Name of the anime
    name = match.group(1)
    print("\nThe anime is", name)
    return name



""" Create an image from a quote file each time different.
    It update automatically every time a quote is used so 
    I never need get the same quote twice. """

def quote_img(quotes):

    # if there is more new quotes
    try:
        # Get the number of the quote to put it in the name of the image saved
        nb = get_the_quote_nb()

        res = quote_list(quotes)

        # Create an image with a transparent background
        image = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        # Set the font and draw the text on the image
        font = ImageFont.truetype('/Users/abedelzubaidi/Downloads/go3v2.ttf', 33)

        rect_size_height = 1700 - (len(res) + 1) * 80

        # Draw a rectangle
        draw.rectangle((100, rect_size_height, 950, 1650), fill=(0, 0, 0, 191), outline=(0, 0, 0, 191))

        space_line = rect_size_height + 50
        for i in range(len(res)):
            
            draw.text((150, space_line), res[i], font=font, fill='white')
            
            space_line += 75

        # Save the image to a file
        image.save(f'image {nb}.png')

    except TypeError:
        print("THERE IS NO MORE QUOTES TODAY COME BACK TOMORROW!!!")



""" Make the final clip.
    Param : folder_name : I take a clip from this folder,
            quotes : the name where are the image of the quote, 
            dst_folder : The folder destination of the result of the video. """

def make_clip(folder_name, quotes, dst_folder):

    # Get the number of the quote of the day
    nb = get_the_quote_nb()
    
    # Get the folder name of the anime. False to don't print the details of the quote
    name = get_anime_name(False, quotes)

    # Go into the Folder clips
    folder_path = f'../{folder_name}'
    os.chdir(folder_path)
    
    # List contains all the images name to resize
    clip_list = []

    # Add all the images to the list of images
    for image in os.listdir(name):
        if image.endswith(".mp4"):
            clip_list.append(image)

    # Chose a random number between 0 and the length of the folder
    rand = rd.randint(0,len(clip_list) - 1)

    # Go into the folder corresponding to the anime
    os.chdir(f'{name}')

    # Load the video clip
    clip = VideoFileClip(clip_list[rand])

    # Load the image
    image = ImageClip(f'../../{quotes}/image {nb}.png').set_duration(clip.duration)

    # Overlay the image on the video clip
    final_clip = CompositeVideoClip([clip, image])

    # Save the resulting video
    final_clip.write_videofile(f'../../{dst_folder}/{name} {nb}.mp4', fps=30)
    
    # Update the quote number of the number
    update_quote_number()



""" Make a video with a clip of an anime and a quote from it.
    Param : clips : the name of the folder that contain the clips. """

def make_clip_quote(clips, quotes, dst_folder):
    quote_img(quotes)
    make_clip(clips, quotes, dst_folder)
