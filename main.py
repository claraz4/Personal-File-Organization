import os
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

    # PROGRAMS AND APPLICATIONS
    if extension == ".exe" or extension == ".msi":
        # shutil.move(source_file, destination)
        shutil.move(absolute, programs)

    # PIANO SHEETS
    if extension == ".pdf" and "piano" in file_name.lower():
        shutil.move(absolute, piano)

    # WORKOUT
    if extension == ".mp4" and is_workout(file_name):
        # Rename the file by changing the underscores
        new_file_name = replace_underscore(file_name)
        new_absolute = os.path.join(downloads, new_file_name + extension)
        os.rename(absolute, new_absolute)

        # Move the file to the workout folder
        shutil.move(absolute, workout)

    # LAU FILE (UNIVERSITY)
    course_folder = is_uni_file(file_name, courses)
    if course_folder != "":
        shutil.move(absolute, course_folder)
