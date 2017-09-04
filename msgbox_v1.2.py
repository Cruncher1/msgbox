from ctypes import windll


def msgbox(text, title='', buttons='ok', default_button='none', icon='none'):
    """
    creates a message box
    msgbox(text, [title='', buttons='ok', default_button='none', icon='none'])
    """
    if _test_for_ezmsg(text) == True:
        arg_list = _ezmsg(text)
        text,title,buttons,default_button,icon = arg_list
    buttons, icon, default_button = _format_args(buttons, icon, default_button)
    default_button = _convert_rc_default_buttons(default_button, buttons)
    user_response = _create_ctypes_messagebox(text, title, buttons, default_button, icon)

    # return the user response as a string:
    return user_response  # Example: "Yes"


def _test_for_ezmsg(str):
    """
    Tests initial text string for commas, assuming that commas indicate the ez version of entry for the
    msgbox function permitting all args to be entered as comma separated in a single string.
    """
    if ',' in str:
        _ezmsg(str)
        result = True
    else:
        result = False

    # Returns True to msgbox fxn if comma found in str.
    return result  # Example: True


def _ezmsg(str_complex):
    """
    Enables user to enter comma separated values in a single string. Why? Because I don't like having
    to type quotes over and over. The fxn parses the single string into args, then supplements any
    missing args with defaults and sends the result through the main funciton msgbox.
    Expected order of args: text, title, buttons, default_button, icon

    """
    arg_list = ['Hello', '', 'OC', 'none', 'none']  # default list
    ez_arg_list = str_complex.split(',')  # split ez string by commas into new list.
    for counter, arg in enumerate(ez_arg_list):
        arg_list[counter] = arg

    # returns list of args to msgbox. Used to assign values to vars when _ezmsg() is True.
    return arg_list  # Example: ['my text','my title','YNC','Y','*']


def _format_args(a1, a2, a3):
    """
	Accepts three args (buttons, icon, default_button) and makes them
	lowercase and removes whitespace.
	example: converts ' YES NO' to return 'yesno'
	"""
    a1, a2, a3 = a1.lower(), a2.lower(), a3.lower()
    a1, a2, a3 = a1.replace(" ", ""), a2.replace(" ", ""), a3.replace(" ", "")

    # returns to msgbox() arguments in lowercase and sans whitespaces.
    return a1, a2, a3  # Example: 'yesnocancel'


def _convert_rc_default_buttons(default_button, buttons):
    """
	Most buttons stay in the same places (Yes is always in position one for
	example), but two can vary. Cancel is always pos 2, except when in
	yesnocancel. Retry is pos 2 in retrycancel, pos 3 in abortretrycancel.
	So, if retry or cancel is provided as a string in default_button,
	then we clarify its position here:
    """
    if (default_button == 'r') | (default_button == 'retry'):
        if (buttons == 'rc') | (buttons == 'retrycancel'):
            default_button = 'r1'
        else:
            default_button = 'r2'
    elif (default_button == 'c') | (default_button == 'cancel'):
        if (buttons == 'ync') | (buttons == 'yesnocancel'):
            default_button = 'c3'
        else:
            default_button = 'c2'

    # returns to msgbox() string  r1, r2, c2, c3 or the
    # default_button as it was:
    return default_button  # Example: 'r2'


def _create_ctypes_messagebox(text, title, buttons, default_button, icon):
    """
    Uses ctypes messagebox function to create and display our msgbox.
    Converts the user_response to string format.
    Returns string of clicked button. "Yes", "No", "Cancel", etc.
    """

    # Hex dictionaries for buttons, default choices and icons:
    btns = {
        'ok': 0x0, 'o': 0x0, '': 0x0,
        'okcancel': 0x1, 'oc': 0x1,
        'abortretryignore': 0x2, 'ari': 0x2,
        'yesnocancel': 0x3, 'ync': 0x3,
        'yesno': 0x4, 'yn': 0x4,
        'retrycancel': 0x5, 'rc': 0x5
    }
    default = {
        '': 0x0, 'none': 0x0,
        'o': 0x0, 'ok': 0x0,
        'y': 0x0, 'yes': 0x0,
        'n': 0x100, 'no': 0x100,
        'a': 0x0, 'abort': 0x0,
        'i': 0x200, 'ignore': 0x200,
        'c2': 0x100, 'c3': 0x200,
        'r1': 0x0, 'r2': 0x100
    }
    icons = {
        '': 0x0, 'none': 0x0,
        'x': 0x10, 'error': 0x10, 'stop': 0x10, 'hand': 0x10,
        '?': 0x20, 'question': 0x20, 'questionmark': 0x20,
        '!': 0x30, 'exclamation': 0x30, 'exclamationpoint': 0x30,
        'i': 0x40, 'info': 0x40, 'information': 0x40,
        '*': 0x40, 'asterisk': 0x40
    }
    # string dictionary to convert user_response from int to string for return:
    response = {1: 'OK', 2: 'Cancel', 3: 'Abort', 4: 'Retry',
                5: 'Ignore', 6: 'Yes', 7: 'No'}

    # Handle incorrect entry of buttons or default_button:
    # if either the value of buttons or default_button is not allowed, replaces both with 'ok'.
    if (buttons not in btns)|(default_button not in default):
        buttons = 'ok'
        default_button = 'ok'

    # create messagebox and assign a value to the users response:
    user_response = windll.user32.MessageBoxW(0, text, title, btns.get(buttons)
                                              | default.get(default_button)
                                              | icons.get(icon)
                                              | 0x10000
                                              | 0x40000)
    # final hex sets messagebox as 'topmost'.

    # convert user_response from an int to a string containing
    # the name of the button pressed by the user:
    user_response = response.get(user_response)

    # return the user response to msgbox() as a string:
    return user_response # Example: "Yes"


# For Testing
if __name__ == '__main__':
    user_response = msgbox("Would you like ice cream?", "TEST MSGBOX", "YNC", 'Y', '?')
    msgbox("You clicked: {button}".format(button=user_response))
    user_response = msgbox("Tornado Warning Today!", "Weather Alert", '', '', 'X')
    msgbox("You clicked: {button}".format(button=user_response))

    # test of _ezmsg function:
    user_response = msgbox('This msgbox generated by the ezmsg function, TEST _EZMSG, YNC')
    msgbox("You clicked: {button}".format(button=user_response))
    user_response = msgbox('This tests _ezmsg for skipping params, _EZMSG evaluation,,,I')
    msgbox("You clicked: {button}".format(button=user_response))

    # test handling of improper buttons and default_button:
    user_response = msgbox('User entered buttons as ABC which gets re-evaluated to OK instead.' , 'WRONG BUTTONS MSGBOX' , 'ABC' , 'Y')
    msgbox("You clicked: {button}".format(button=user_response))
    user_response = msgbox('User entered buttons as ABC which gets re-evaluated to OK instead., WRONG BUTTONS EZMSG, ABC, Y')
    msgbox("You clicked: {button}".format(button=user_response))

    msgbox('Goodbye','Testing complete')

