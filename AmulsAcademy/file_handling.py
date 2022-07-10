#using open keyword will create a file along with the path of the file and mode of the file
import os

#remove the files
# os.remove('C:/Shivani/text1.txt')
# os.remove('C:/Shivani/text2.txt')
txt_file = open('C:/Shivani/text1.txt', 'w')
txt_file.write('Hello Shivani\n')
txt_file.write('Hello Ayan\n')
txt_file.write('Hello world\n')
txt_file.write('interview prep\n')
txt_file.write('Hello python')
txt_file.close()
txt_file = open('C:/Shivani/text1.txt', 'r')
print(txt_file.read())
txt_file.close()

# rename method
os.rename('C:/Shivani/text1.txt', 'C:/Shivani/text1.txt')

# creating a directory
os.mkdir('C:\\Shivani\\mkngdir')
# os.remove('C:\\Shivani\\mkngdir')
# to know the current directory path
print(os.getcwd())
os.chdir('C:\\Shivani\\mkngdir')
print(os.getcwd())
(os.listdir('C:\\'))