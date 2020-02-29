# SWN Generators
A small set of generators for Stars Without Number Revised Edition. 12/29/2017 Edition.

Mainly made as a test to see if I could do it. I wanted originally to just have CLI scripts, but after finding the amazingly wonderful [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) I decided to lump it all in to a GUI program. Jury is still out on whether or not that was a good decision, since I am the worst at UX. Just look at it. Ugh.

![Oh god it's ugly](screenshot.PNG "Oh god it's ugly")

This should be cross-platform, but I have yet to test it on anything other than Windows. I have included a standalone .exe as a release, as the installation procedure as it stands leaves a lot to be desired as an end user. If you don't trust it, [do it yourself](https://pysimplegui.readthedocs.io/#creating-a-windows-exe-file). I don't blame you! 

## Prerequisites

To install, you first need to install [Python 3.6+](https://www.python.org/downloads/). Download and install whichever version your computer needs. Linux users should have it pre-installed, but ```python3``` might not be up-to-date.

Second, you need to install [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI):

```pip install --upgrade PySimpleGUI```

or

```pip3 install --upgrade PySimpleGUI```

That should be run from command line. Windows users may need to preface the command with ```py -m```, assuming you selected that option during installation:

```py -m pip install --upgrade PySimpleGUI```

If ```py``` does not work, then you'll need to find where Python was installed and run the command there:

```python -m pip install --upgrade PySimpleGUI```

Windows users likely also need to run the command prompt as administrator (right clicking the Command Prompt and selecting Run as administrator).

I have yet to try to install and run this on Linux. I should be able to eventually refine that process and update this.

## Running the SWN Generator

Running the generator is fairly straightforward from here. You have two options currently: either running it through the executable, or running gengui.py directly.

### Running the Executable

Download the latest [release](https://github.com/Atreusion/SWN-Generators/releases) and run the .exe file. It's super simple. It's standalone, which means it doesn't need an installer or any other files.

### Running the Code Directly

Download both [gengui.py](https://github.com/Atreusion/SWN-Generators/raw/master/gengui.py) and [name_container.py](https://github.com/Atreusion/SWN-Generators/raw/master/name_container.py) and either double-click gengui.py or run it through ```py``` or ```python3```.

## FAQs

### Why Python 3.6+?

This code uses [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings), or formatted string literals, a cool feature added in Python 3.6 that allows expressions to be evaluated at run time. I wanted to play around with them, so I did.

### Why a separate container for the names?

I don't know if there's a preferred Pythonic style for annoyingly long lists. The first_names list has 2,000 names, and the last_names list has 1,000. I could have it be two incredibly long lines, but for sanity's sake I like to break longer lists like that up to make it (usually) easier to work with. But, breaking those lists up at 80 characters made them total 400 lines long. That's over 1/3 of the length of gengui.py! To make editing gengui.py easier, I moved those two lists to name_container.py and call it in as a separate module.

For all I know, this is the worst way of doing this. I make no claims that I'm a good programmer. ¯\\\_(ツ)_/¯

### Has anyone actually asked you these questions?

nope

## Permission

Made with [permission from Kevin Crawford himself](https://old.reddit.com/r/SWN/comments/av868q/random_generator/ehdm603/). All SWN content is owned by [Kevin Crawford, Sine Nomine Publishing](https://sinenominepublishing.com/).
