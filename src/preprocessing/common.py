import os, shutil


# For any path and extension, this function returns an array of full paths for all files in the directory or its
# subdirectories containing the string extension provided in the function call.
#
# root The root directory to search in
# extension The substring to search for in filenames
# limit This is a safety in case you accidentally point this function at '/'. You must manually increase this to
#       search through more than 10,000 files. Note, this applies to how many files you search NOT how many are
#       returned.
# ignore_files_beginning_with_dot This option is used to conveniently ignore '._' files of which there are many.
def list_files_in_subdirectories_by_extension(root, extension, limit=10000, ignore_files_beginning_with_dot=True):
    # Initialize a buffer to store the files when we find them
    files = []

    # Initialize a counter to ensure we don't exceed limit number of searches
    i = 0

    # os.walk() does the magic for this function. It finds all the files in a directory.
    for path, subdirs, dir_files in os.walk(root):
        # Fail if we exceed limit files
        if i >= limit:
            print 'limit'
            raise Exception(
                'Could not complete listing within the specified limit. Change the root to point at fewer files or\
                    increase the limit.')
        # Increment the safety counter
        i += 1

        # For all the files in this directory, check if it matches search criteria, and add it to the buffer if it does
        for name in dir_files:
            # Apply search criteria (see function docs) and store the file's full path if it matches them
            if ((not ignore_files_beginning_with_dot) or (name[0] != '.')) and (extension in name):
                files.append(os.path.join(path, name))

    # Return the files we found
    return files


# Moves files based on an array of their paths from one location in the file system to a single destination. Great for
# aggregating data. Basically just wraps shutil.copy2.
#
# files An array containing the paths of the files to move
# dest The destination directory to copy the files to
def copy_files(files, dest):
    for file in files:
        shutil.copy2(file,dest)