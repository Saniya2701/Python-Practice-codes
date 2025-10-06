import os


os.mkdir("MyFolder")
print("Directory 'MyFolder' created.")


print("Current directory contents:", os.listdir())


os.rename("MyFolder", "NewFolder")
print("Directory renamed to 'NewFolder'.")


os.rmdir("NewFolder")
print("Directory 'NewFolder' removed.")

