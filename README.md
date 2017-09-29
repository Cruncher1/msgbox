# msgbox
Purpose: to create a simple and memorable function for producing a native windows message box.

### 1 required field followed by 4 optional fields:
```
msgbox(message text, [title, buttons, default button, icon])  # Only message text is required. 
```

### Standard Usage Examples:

```
msgbox('Hello World')  # Produces Messagebox with single 'OK' button and no title.
msgbox('Hello World', 'My Title')
msgbox('Hello World', 'My Title', 'Yes No')  # Produces Messagebow with Yes and No buttons. 
msgbox('Hello World', 'My Title', 'Yes No Cancel', 'No')  # Indicates that 'No' will be the highlighted default button.
msgbox('Hello World', 'My Title', 'Ok Cancel', 'Cancel', '?')  # Adds '?' icon
msgbox('Hello World', 'My Title', 'YNC', 'C', '!')  # Instead of typing Yes, No and Cancel, YNC is also acceptable.
```

### Lazy Usage Examples:
All arguments can be placed in the first string so long as comma separated. Why? I get tired of typing all of those quotes. 
```
msgbox('Hello World, My Title, YN, , i')  # Produces Yes No Messagebox with text, title and the I info icon. 
msgbox('Hello\, World, My Title')  # Produces OK Messagebox with text "Hello, World" and title "My Title". 
```

### Buttons:
The third and fourth arugument are for button options and are optional. If none is indicted, 'OK' will be used. 

There are six options: 

* 'ok', 'ok cancel', 'abort retry ignore', 'yes no cancel', 'yes no', 'retry cancel'.
* Alternately, initials may be used: 'o', 'oc', 'ari', 'ync', 'yn', 'rc'.
* Case and spacing are ignored. 
* All of these are treated the same: 'Y N C', 'yesnocancel', 'YEsNocanCEL', 'YES NO CANCEL'

The fourth argment specifies the default button. If none is provided, the first button is the default. 

Examples: 

* msgbox('Hello', 'My Title', 'YN')  # Yes button is default
* msgbox('Hello', 'My Title', 'YN', 'N')  # No button is default


### Icons:
The fifth argument is for the icon and is optional. 

* Allowed: 'x', '?', '!', 'i', '*'.
* Alternately, you may spell out the icon descriptions: 
* 'error', 'stop', 'hand','question', 'questionmark', 'exclamation', 'exclamationpoint', 'info', 'information', 'asterisk'.

### Using the return string:
```
user_response = msgbox("Would you like ice cream?", "Ice Cream", "YNC", 'Y', '?')
msgbox("You clicked: %s" % user_response)

user_response = msgbox("Tornado Warning Today!", "Weather Alert", '', '', '!')
msgbox("You clicked: %s" % user_response)
```

### Concept

I like the simplicity and functionality of AHK Script (autohotkey) which allows for 
```
MsgBox , Hello World
```
as well as providing additional fields to customize the native windows message box. 
I wanted to create something similar for python. I did some research and found that 
PyQt, ctypes, tkinter and others can do this, but with some complication. @asweigart 
developed a very nice cross platform pymsgbox module, but the native windows features 
were limited. What I would like to accomplish is available in ctypes, but requies 
passing hex code and other non-intuitive arguments. I intend to use ctypes import.

I wanted to allow the user to name the buttons rather than remember message box types.
So, the user can choose "Yes No Cancel" or even just "YNC". The same with choosing which button
is defaulted "Cancel". I wanted the function to return the string of the button name pressed. 
So, if "Cancel" is pressed, the function returns the string "Cancel". 

I am only working on a windows desktop and am not interested at this time in cross-
platform functionality. For that, one should use pymsgbox @asweigart.

### Things to add

* HWND field so that msgbox can have a parent window
* Optional timeout feature

