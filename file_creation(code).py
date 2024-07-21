import os

# Define the directory name
directory = "Python_Beginner_Course"

# Define the list of filenames
filenames = [
    "Python_Beginner_Course#1_Introduction.mp4",
    "Python_Beginner_Course#2_Variables_and_Data_Types.mp4",
    "Python_Beginner_Course#3_Setup_and_Installation.mp4",
    "Python_Beginner_Course#4_Basic_Syntax.mp4",
    "Python_Beginner_Course#5_Strings.mp4",
    "Python_Beginner_Course#6_Lists.mp4",
    "Python_Beginner_Course#7_Tuples.mp4",
    "Python_Beginner_Course#8_Dictionaries.mp4",
    "Python_Beginner_Course#9_Sets.mp4",
    "Python_Beginner_Course#10_Functions.mp4",
    "Python_Beginner_Course#11_Conditionals.mp4",
    "Python_Beginner_Course#12_Loops.mp4",
    "Python_Beginner_Course#13_Classes_and_Objects.mp4",
    "Python_Beginner_Course#14_Lambda_Functions.mp4",
    "Python_Beginner_Course#15_List_Comprehensions.mp4",
    "Python_Beginner_Course#16_Regular_Expressions.mp4",
    "Python_Beginner_Course#17_Modules.mp4",
    "Python_Beginner_Course#18_Packages.mp4",
    "Python_Beginner_Course#19_Exception_Handling.mp4",
    "Python_Beginner_Course#20_File_Handling.mp4"
]

# Create the directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create each file in the directory
for filename in filenames:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        pass  # Create an empty file

print(f"Files created in the directory '{directory}'")
