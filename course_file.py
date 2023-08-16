class CourseFile:
    def __init__(self, semester_path, folder_path, course):
        self.semester_path = semester_path
        self.folder_path = folder_path
        self.course = course

    def __str__(self):
        return f"Person(semester_path={self.semester_path}, file_path={self.folder_path}, course={self.course})"
