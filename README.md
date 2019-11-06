# PythonGUI
This project is a Python application that comprised of a GUI and a module of fractal figures. 


# PREREQUISITES
For this application to run, you will need python installed on your machine. IDLE 3.8 was used in the development of this project. 
You can download the latest python installer via the following website: https://www.python.org/downloads/release/python-380/

For Mac machines, PIP was installed via the CMD line with the following code:
$ sudo pip3.8 install pillow

Both files: GUI.py and turtlefigure.py must be in the same directory. 

## GUI.py
This is the file and code for the App itself. 

## turtlefigure.py
This is the python module with the fractal figures

# INSTRUCTIONS
This app has 3 inputs:
1. Order (an integer)
2. Length (in pixels)
3. A drop down of pre-defined figures

I would recommend to keep the Order below 5 (however feel free to put in any number you like). The higher the number, the longer it will take for the sketch to finish. 


# DESIGN CONSIDERATIONS & DECISIONS

## Random Module and colours

Importing the Random module and applying a specific set of random colours to generate on pen strokes was added to improve the overall artistic quality of the app while also improving the user experience due to contrasting colours that compliment each other and stay within a theme.
 
## Using a Label widget for text display
For appearance reasons and integration with the onDrawF function, I opted for using the Label widget for changing the Additional Info dialogue box. Label does not allow the text to be changed on the front end by the user, this way it appears more integrated and sound. As for the additional information being dynamic, I set a single textvariable and this then changes for every IF statement within the onDrawF function. I placed this textvariable.set() command before calling the figure drawing so that the user can read the information while the pen is drawing. 

## Pen location and functionality
A turtle.reset command was used and integrated with the onClearF function so that the canvas was cleared each time the Clear button was pressed. This was important so that the canvas did not become cluttered and so that each fractal was clearly visible when drawn, as long as the user previously selected Clear. I added a pen location so that the majority of fractals (depending on the value the user enters for Length) was as close to being entered on the canvas as possible. 

## Root geometry
Increasing root geometry for 2 primary reasons:
	1. So that the window will display all figures when L < 500
	2. The overall usability of the app is clearer and less cluttered. 

## Widget Configurations
Use of widget.config() options to improve usability. For example, I added a ‘takefocus=1’ to the turtleOptionMenu (dropdown) so that the user can interact with all elements using the TAB key on their keyboard. For example, the user can press the TAB key 3 times to arrive at the turtleOptionMenu, they then need to press SPACEBAR, scroll through the options with the UP and DOWN arrow keys and finally select an option with ENTER. 
_  http://python.6.x6.nabble.com/OptionMenu-Cannot-Receive-Keyboard-Focus-td1975837.html


## Save Drawing Button
I added a save drawing button inside of a label widget so that the user can take a screenshot of a predefined set of coordinates (that cover the span of the canvas)
The button saves the canvas as a .png file, the action of clicking or interacting with the Save Drawing button also creates a “Image Saved” print in the python shell. 
NOTE: An important note on this is that this image is a screenshot of the coordinates of the canvas (in relation to your screen or monitor). If this app is being used on a machine other than a MacBook Pro (13.3 inch, 2560 x 1600), then the coordinates will need to be adjusted on your machine. The coordinates that need to be edited are on line 133 of GUI.py. 

Additionally, I used the ‘time’ module in order to get the current epoch time (this is the number of seconds since midnight GMT, January 1st, 1970) and add this to the file name of the saved image. This is so that each image file had a unique name. 
Inspired by:
_ https://github.com/python-pillow/Pillow/issues/3293

## Cursor Pointers
I have set each button within the App to have a distinct cursor pointer when the user hovers the cursor over the button. Hopefully these pointers are somewhat intuitive. 

* Pencil Cursor = Draw Button
* Cancel Cursor = Clear Button
* Heart Cursor = Save Drawing Button

## Hide Pen
I chose to hide the turtle after each drawing has finished by calling the command pen.ht(). The reason for this was so that if a user does decide to save the image using the ‘Save Drawing’ button, the turtle will not overlap on the drawing. 



# OVERALL APP APPEARANCE

I applied a dark background colour (#160E2B) in order to create contrast between the light, interactive elements (widgets) and dark, non interactive elements (the background of the entire application). A colour combination was decided on and applied to all aspects of the application. For example, the headings of each widget are a light shade of purple while the root background is a dark, almost black shade of purple. 

Imported the ‘random’ module in order to apply random colours when generating the fractals. The code ‘pen.color(random.choice(colors))’ was applied to the original file that contained the 10 fractals so that after each iteration, the turtle colour would randomly change from a choice of 3 colours. This line of code was applied to the initial colour of the pen(turtle) after the clear function is applied so that the first stroke is also randomised for each drawing. 

Integrated text variable into the if loops in the onDrawF function so that the label changed according to what option was selected from the Option Menu. 

Developed a Save Drawing button so that the canvas can be saved as a .png file. An important note on this is that this image is a screenshot of the coordinates of the canvas. If this app is being used on a machine other than a MacBook Pro (13.3 inch, 2560 x 1600), then the coordinates will need to be adjusted on your machine. The coordinates that need to be edited or on line 133 of GUI.py. 

In order to improve the experience of the user, the Label widget entitled ‘Additional Info’ has default text when the canvas is not displaying a fractal. This default text contains some general instructions and tips on using the app

# SCREENSHOTS

<img width="600" alt="Screenshot 2019-11-05 at 16 54 39" src="https://user-images.githubusercontent.com/8673218/68345479-50ba7b80-00e9-11ea-96bc-414f2fdccee6.png">

<img width="600" alt="Screenshot 2019-11-05 at 16 55 14" src="https://user-images.githubusercontent.com/8673218/68345571-8d867280-00e9-11ea-91fd-0707d2ebcb93.png">
