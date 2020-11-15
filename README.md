# AutoFlick
A utility for playing Rhythm Heaven on emulators
<hr></hr>

## Installation Tutorial


1. Click the green "Code" button in the Github repository. This downloads the code.
2. Double click on `AutoFlick-master.zip` to turn it into a folder.
3. Install Python 3 by following this guide: https://realpython.com/installing-python/
4. Type `pip install pynput` (`pip3 install pynput` on Mac) to install pynput.

**Windows users: If pip is not found: follow this guide:** https://phoenixnap.com/kb/install-pip-windows

5. Go into the `AutoFlick-master` folder. If you're running Windows, simply double click on `autoflick.py`. For Mac users, double click on `autoflick.command`.


## How to Use This Software



This uses 5 buttons. They will be known as the following:

* Tap
* Quick Tap
* Flick
* Love
* Base

## Tap
By default, this is assigned to `[`. You can use this button to hold down the stylus. As long as this button is down, the stylus is down.

## Quick Tap
By default, this is assigned to `=`. Unlike Tap, when you press this, it does not stay down. As the name implies, it is a quick tap. It is useful for games such as Moai Doo-Wop.

## Flick
By default, this is assigned to `]`. When this is held down, it charges a flick, and when it's released, it flicks. **If you meant to tap instead. of flick but hit the wrong button, while holding down Flick, hold down Tap, then release Flick.** The same goes for Tap.

## Love
By default, this is assigned to `Grave/Tilde`. This button is called Love because it is only used with games that have "Love" in the title (i.e. Love Lizards, Love Lab). When this is held down, it changes the functions of Tap and Flick. Tap now moves the cursor to the base point, and Flick moves it away from the base point. In other words, to do a dance in Love Lizards, hold down Love and type: 

`]` `[` `]` `[`

This assumes that `[` is Tap and `]` is Flick.

## Base
By default, this is assigned to `\`. Near the bottom of your emulated Touch Screen, press this button. The location on the screen you pressed Base at determines where your cursor will return after a flick is done.
