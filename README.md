# msgbox
Create simple intuitive functionality for native windows message box functionality.
Based on ctypes import and inspired both AHK and by pymsgbox whose creator is @asweigart.

### 1 required field followed by 4 optional fields:
```
msgbox(Text, Title, Buttons, Default Button, Icon)
```

### Usage Examples:

```
msgbox('Hello World')
msgbox('Hello World', 'My Title')
msgbox('Hello World', 'My Title', 'Yes No')
msgbox('Hello World', 'My Title', 'Yes No Cancel', 'No')
msgbox('Hello World', 'My Title', 'Ok Cancel', 'Cancel', '?')
msgbox('Hello World', 'My Title', 'YNC', 'C', '!')
msgbox('Hello World', 'My Title', 'ARI', '', 'X')
msgbox('Hello World', '', '', '', 'I')
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
were limited. 

I am only working on a windows desktop and am not interested at this time in cross-
platform functionality. For that, one should use pymsgbox @asweigart.

### Things to add

* HWND field so that msgbox can have a parent window
* Timeout feature

