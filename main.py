import os
import datetime
import shutil
from helpers import replace_underscore, is_workout, get_courses, is_uni_file

# Store all the needed path's folders
downloads = "C:\\Users\\Admin1\\Downloads"
programs = "C:\\Users\\Admin1\\Desktop\\Programs"
piano = "C:\\Users\\Admin1\\Desktop\\Music\\music sheets"
workout = "C:\\Users\\Admin1\\Desktop\\Workout"
uni_folder = "C:\\Users\\Admin1\\Desktop\\LAU"

# Get the names of all the files in the downloads directory
files = os.listdir(downloads)

# Open the file to keep track of the actions done
actions = open("actions.txt", "a")
actions.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")

# Check if the downloads file is empty (there's always the desktop.ini
if len(files) <= 1:
    actions.write("Downloads folder is empty\n")


# Check each file and see whether the conditions fit to move it
for file in files:
    # Get the file extension
    extension = os.path.splitext(os.path.abspath(file))[1]

    # Get the absolute path of the file
    absolute = os.path.join(downloads, file)

    # Get the file name
    file_name = os.path.basename(file).replace(extension, "")

    # Get the list of all the courses objects you have (in uni), so I can have the keywords to check for uni files
    courses = get_courses(uni_folder)
    # Get the course folder if the file a uni file
    course_folder = is_uni_file(file_name, courses)

    # PROGRAMS AND APPLICATIONS
    if extension == ".exe" or extension == ".msi":
        # shutil.move(source_file, destination)
        shutil.move(absolute, programs)
        actions.write(file_name + " was moved to " + programs + "\n")

    # PIANO SHEETS
    elif extension == ".pdf" and "piano" in file_name.lower():
        shutil.move(absolute, piano)
        actions.write(file_name + " was moved to " + piano + "\n")

    # WORKOUT
    elif extension == ".mp4" and is_workout(file_name):
        # Rename the file by changing the underscores
        new_file_name = replace_underscore(file_name)
        new_absolute = os.path.join(downloads, new_file_name + extension)
        os.rename(absolute, new_absolute)
        if file_name != new_file_name:
            actions.write(file_name + " was renamed to " + new_file_name + "\n")

        # Move the file to the workout folder
        shutil.move(new_absolute, workout)
        actions.write(new_file_name + " was moved to " + workout + "\n")

    # LAU FILE (UNIVERSITY)
    elif course_folder != "":
        shutil.move(absolute, course_folder)
        actions.write(file_name + " was moved to " + course_folder + "\n")

    else:
        actions.write(file_name + " still in downloads folder\n")

actions.write("\n")
actions.write("-" * 20)
actions.write("\n\n")
actions.close()
