***What is file handling?***
<p>
File handling is a process through which we can create a file, store data in it, retrieve data from the file and also append more information in it. </p>

***Does python support file handling?***

<p>Like many other languages python also supports file handling.</p>

***What is file handling in python?***
<p>Python supports file handling and gives us many modes to operate a file. We can create a new file using python code, open existing files, write in files ,read data from files and many more such options.
We have many languages which supports file handling , in some languages this topic is a bit complicated, but in python file handling is very easy.</p>
<p>Python treats it's texts and binary differently in file handling.</p>
<p>Before we can start with reading data from a file, or writing some data into it, we need to open a file.</p>

<p><b><i>Working of open function for python file handling:</i></b></p>
<p>We use open function in python to open a file in different modes , read mode, write mode, etc.</p>

<p><b>Syntax:</b></p>
<p>file object = open(file_name,mode)</p>
<ul>
<li>file object - This is the object of the file. </li>
<li>open - open() is the function used to open a file in python.</li>
<li>file_name - file_name is the name of the file we want to open to edit data or read data from it.</p></li>
<li><p>mode - In python we have many modes in which we can operate a file. As python treats texts and binary differently in file handling , so the number of modes is more.</p></li>

<p>Let us take a look into the different types of modes to operate a file:</p>
<p>
<b><i>Modes in python:</b></i>
</p><br>
<p>1. <b><i>r</i></b> - This is the read mode. In this we can read the informaton the file has. The reading of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>2. <b><i>rb</i></b> - This is also a read mode , but here the information is read only in binary format. Here also, the reading of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>3.<b><i>r+</i></b> - This mode is for both reading and writing data. In this we can read data and write data in the same file simultaneously. Here too, the reading and writing of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>4.<b><i>rb+</i></b> -This mode is also for both reading and writing data , but here the information is read and written only in binary format.Here also, the reading and writing of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>5.<b><i>w</i></b> - This is the write mode. In this we can write data into the file. If there is already some information in the file , this mode overwrites it. If there is no file already with the specified name, it creates a new file. The writing of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>6.<b><i>wb</i></b> -This is also a write mode , but here the information can be written only in binary format. If there is already some information in the file , this mode overwrites it. If there is no file already with the specified name, it creates a new file. The writing of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>7.<b><i>w+</i></b> - This mode is for both reading and writing data. In this we can read data and write data in the same file simultaneously. If there is already some information in the file , this mode overwrites it. If there is no file already with the specified name, it creates a new file. The reading and writing of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>6.<b><i>wb+</i></b> -This mode is also for both reading and writing data , but here the information is read and written only in binary format. If there is already some information in the file , this mode overwrites it. If there is no file already with the specified name, it creates a new file. The writing of the data starts from the beginning of the file, i.e., the file pointer is at the beginning of the file.</p>
<br>
<p>7.<b><i>a</i></b> - This mode is called append mode. In this we write into the file without overwriting the previous data , i.e., if there is already some information in the file , unlike write mode , append does not overwrites it and it appends more information in the same file.  If there is no file already with the specified name, it creates a new file. The writing of the data starts from the end of the file, i.e., the file pointer is at the end of the file.</p>
<br>
<p>8.<b><i>ab</i></b> - This mode is also append mode, but here the information can be written only in binary format. In this we write into the file without overwriting the previous data , i.e., if there is already some information in the file , unlike write mode , append does not overwrites it and it appends more information in the same file.  If there is no file already with the specified name, it creates a new file. The writing of the data starts from the end of the file, i.e., the file pointer is at the end of the file.</p>
<br>
<p>9.<b><i>a+</i></b> - This mode is also append mode, but this mode is for both reading and writing data. In this we write into the file without overwriting the previous data , i.e., if there is already some information in the file , unlike write mode , append does not overwrites it and it appends more information in the same file.  If there is no file already with the specified name, it creates a new file. The reading and writing of the data starts from the end of the file, i.e., the file pointer is at the end of the file.</p>
<br>
<p>10.<b><i>ab+</i></b> - This mode is aldo append mode, but here the information can be written and can be read too , only in binary format. In this we write into the file without overwriting the previous data , i.e., if there is already some information in the file , unlike write mode , append does not overwrites it and it appends more information in the same file.  If there is no file already with the specified name, it creates a new file. The reading and writing of the data starts from the end of the file, i.e., the file pointer is at end of the file.</p>
<br>
<p><b><i>If no mode is specified , python considers 'r' as the default mode.</i></b></p>
<b><i>File object attributes:</i></b>
<br>
<p>We saw the different modes in python. Now, once the file is open we can get many information about the file. Let us look some attributes of the file object to get those information:</p>
<p>1.<b><i>file.mode</i></b> - It returns the access moe in which the file is opened.</p>
<p>2.<b><i>file.name</i></b> - It retuens the name of the file.</p>
<p>3.<b><i>file.close</i></b> - It is used to close the file.</p>
<p>4.<b><i>file.closed</i></b> - It returns whether the file is open or closed , i.e, it returns True if the file is closed.</p>
<p>5.<b><i>read([size])</i></b> - It reads the specified number of bytes(the size specified) from the file. </p>
<p>6.<b><i>readline([size])</i></b> - It is used to read one entire line from a file.</p>
<p>7.<b><i>tell() </i></b> - This returns the current position of file pointer.</p>
<p>8.<b><i>write(str)</i></b> - This writes a string into the file.</p>
<p>9.<b><i>writelines(sequence)</i></b> - This writes a sequence of strings into the file.</p>
<br>
<b><p>Example 1:</p></b>
<p>file = open("fname.txt","w")<br>
file.write("Python is a programming language!")<br>
file.close()</p>
<p>Here , a file is created first. The name of the file is "fname.txt" and it currently in "w" mode ,i.e., write mode. So, the given text is written in the file. And finally the file is closed.
<br>If we want to open the above file the contents we would see are:
<br>Python is a programming language!</p>
<br>
<b><p>Example 2:</p></b>
<p>s = open("fname.txt","r+")<br>
print("The read text is ",s)<br>
s.close()<br></p>
<p>Here, the name of the file is fname , the mode is r+ and we print the read text , finally the file is closed.<br>
Output:<br>
Pytho<p>


