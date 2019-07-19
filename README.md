# magicicon
Created by Armaan Aggarwal on May 19, 2019

v2.0.1 released on July 18, 2019


A python module that can create .ico, .icns and .png files, regardless of the operating system! This project also has a GUI.

**Note this package requires PIL and CloudConvert, which can be installed via pip by calling**

`pip install Pillow cloudconvert`

**in your command line.**

****

### Usage:
* **magicicon.py:**

	magicicon.py has a function called convert().
	convert() takes two parameters: `filename` and `outputfile`.

	****


	`filename`: This paramenter is the filename. It can be the full path, like `C:\example.png` or it can be just `example.png`.


	`outputfile`: This parameter specifies the outputfile. **The ouput file must have the file extension of the type of icon file                         you want to convert your inputed file into.** Here is a list of valid extensions:

	* `.ico`: For a Windows Icon File
	* `.icns`: For a Apple Icon File
	* `.png`: For a PNG Icon File.




* **gui.py**:

	Just run the program and follow the GUI instructions!

## What's new?

1. Reduced dependability on `errorwindow.py`.
2. Made error messages more cleaner.
3. Made output more advanced
