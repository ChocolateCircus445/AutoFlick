# AutoFlick
A utility for playing Rhythm Heaven on emulators
<hr></hr>

### This requires pynput to work.

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
By default, this is assigned to `Grave/Tilde`. This button is called Love because it is only used with games that have "Love" in the title (i.e. Love Lizards, Love Lab). When this is held down, it changes the mode of Tap and Flick. Tap now moves the cursor to the base point, and Flick moves it away from the base point. In other words, to do a dance in Love Lizards, hold down Love and type: 

`]` `[` `]` `[`

This assumes that `[` is Tap and `]` is Flick.

## Base
By default, this is assigned to `\`. Near the bottom of your emulated Touch Screen, press this button. The location on the screen you pressed Base at determines where your cursor will return after a flick is done.
