# magicicon
Created by Armaan Aggarwal on May 19, 2019

Last updated on May 26, 2019


A python module that can create .ico, .icns and .png files, regardless of the operating system!

****

### Usage:
* **iconmaker.py:**

	iconmaker.py has a function called convert(). 
	convert() takes three parameters: `filename`, `size` and `filetype`.
	
	****
	
	
	`filename`: This paramenters is the filename. It can be the full path, like `C:\example.png` or it can be just `example.png`.
	 
	 
	`size`: This is the parameters in which the size of the icon can be. Accepted arguments are:
		
	* `(16,16)`
	* `(32,32)`
	* `(48,48)`
	* `(64,64)`
	* `(128,128)`
	* `(256,256)`
	* `"Auto"`
		
		
		
		
	`filetype`: the parameter which tells the program which type of icon file you would want to convert your image into. Accepted 		arguments are:
	
	* `ico`
	* `icns`
	* `png`
	
	For example, if you want to convert your image into a ico file (Microsoft Icon File), you would set this parameter to `ico`.
	


* **gui.py**:
	
	Just run the program and follow the GUI instructions!
