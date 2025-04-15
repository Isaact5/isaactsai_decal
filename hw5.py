# 1. You have been plopped into this directory system. What command will tell you what your working directory is?
# pwd (print working directory)

# 2. The command tells you ~/python_decal/judy_decal. What command will list all the files in your current working directory?
# ls (list files)

# 3. Brianna just sent out an announcement that there was a typo on homework.py. So you need to pull the updates. What commands will let you move to the correct repository and pull the latest changes?
# cd ../brianna_repo
    # git pull

# 4. How would you move this new homework.py to your personal repository homework directory?
# cp homework.py ../judy_decal/homework/

# 5. You want to see the contents of the homework.py in your terminal from your personal repository. 
# What command(s) will let you do this?
# cat homework.py

# 6. You want to edit the contents of the homework.py in your terminal from your personal repository. 
# What command will let you do this?
# vim homework.py

# 7. You have finished the homework. What commands will allow you to save the changes and push from your local repository to your remote repository?
# git add homework.py
# git commit -m "Updated homework.py"
# git push origin main

# 8. Oh no! Git gave you an error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did "Judy" do wrong?)
# git pull origin main
# git push origin main

# 9. What absolute path will allow you to move to Recent/?
# ~/Recent

#2.1

def checkDataType(input_value):
    return type(input_value).__name__

#print(checkDataType(3.14))
#print(checkDataType(True))

#2.2
def evenOrOdd(num):
    if num % 2 == 0:
        return 'Even'
    return 'Odd'

#print(evenOrOdd(7))
#print(evenOrOdd(10))

#3
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#print(sumWithLoop([1, 2, 3, 4, 5]))

#4.1
def duplicateList(lst):
    result = []
    for item in lst:
        result.extend([item, item])
    return result

#print(duplicateList(['a', 'b', 'c']))

#4.2: the function is missing a colon after the parameter. it should be:
def square(num):
    return num * num

#print(square(4))