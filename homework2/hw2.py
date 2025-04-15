# 1) Suppose your current working directory is ~/Desktop/classes/python_decal/. What command would allow you to navigate directly to ~/Desktop?
# cd ../../

# 2) What does ~/ mean?
# ~/ refers to the user's home directory

# 3) What's the difference between and abolute and a relative path in your terminal?
# An absolute path starts from the root directory and gives the complete path to a file/directory, while a relative path starts from the current directory and gives the path relative to where you are.

# 4) What command would bring you back to your home directory?
# cd ~ or cd

# 5) If you called rm ./ in your current working directory, what would it do? 
# it would give an error because rm cannot remove a directory without additional flags

# 6) In your current working directory, what does calling "git add" do? What about "git commit"? What about "git push"?
# - git commit: MAkes a snapshot of the staged changes with a message describing what changed
# - git push: Uploads committed changes to the remote repository

# 7) Let's say you call "git add" in your current working directory and then "git status". What message would appear? What is it telling you?
# (base) isaactsai@wifi-10-40-189-249 python_decal % git add
# Nothing specified, nothing added.
# hint: Maybe you wanted to say 'git add .'?
# hint: Turn this message off by running
# hint: "git config advice.addEmptyPathspec false"
# (base) isaactsai@wifi-10-40-189-249 python_decal % git status
# On branch main
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#        modified:   homework2/hw2.py
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         Astron98Hw1.py
#         Astron98Hw2.py
#         brianna_repo/
# no changes added to commit (use "git add" and/or "git commit -a")- git add: Stages changes for commit


# 8) What has been the most frustrating error or bug you've encountered in this class so far? How did you troubleshoot and resolve it?
# When I reference git repositories that don't exist. To resolve this, I simply initialize the corresponding git repository and commit the changes accordingly.

# 9) How does cloning a repository differ from pulling from a repository?
# Cloning creates a new local copy of an entire repository, while updates an existing local repository with changes from the remote repository

# 10) Tell me a fun fact!
# Git was created by Linus Torvalds in 2005, and named it "git", which in British English slang means "a silly, incompetent, stupid, annoying, or childish person"!
