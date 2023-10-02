import os
from course_file import CourseFile


def replace_underscore(title):
    """
    _ --> replace by a space
    __ --> replace by ,space
    ___ --> replace by space - space
    
    """
    title = title.replace("___", " - ").replace("__", ", ").replace("_", " ")
    return title


def is_workout(title):
    # Check if the title contains a keyword related to workouts
    keywords = ["arms", "legs", "abs", "lower", "upper", "core", "workout", "cardio", "calisthenics", "body weight",
                "hiit", "pilates", "stretch", "yoga", "warm up", "full body", "back", "glute", "chest"]

    for k in keywords:
        if k in title.lower():
            return True
    return False


def get_courses(main_folder_path):
    """
    My LAU folder contains:
    the list of the semesters --> the list of courses with their folders --> the content of each course

    1) Get the path of all the semesters folder
    2) Get a list of all the courses
    """
    semesters = os.listdir(main_folder_path)
    types_of_semesters = ["fall", "spring", "summer"]
    semesters_paths = []
    courses = []

    # Get the paths of each semester
    for s in semesters:
        for t in types_of_semesters:
            if t in s.lower():
                semesters_paths.append(os.path.join(main_folder_path, s))

    # Get the abbreviation of the courses
    for semester_path in semesters_paths:
        # The name of all the files and folders in each semester folder
        files = os.listdir(semester_path)

        for f in files:
            file_path = os.path.join(semester_path, f)

            # Checking that it is a folder
            if os.path.isdir(file_path):
                course = f.split(" - ")[0]
                courses.append(CourseFile(semester_path, file_path, course))

    return courses


def is_uni_file(file_name, courses):
    # RETURNS THE FOLDER'S PATH ELSE RETURNS ""
    for c in courses:
        course = c.course
        # Check whether the file name has the name of the course in it (without caring about the whitespace)
        if course.replace(" ", "") in file_name.replace(" ", ""):
            return c.folder_path
    return ""
