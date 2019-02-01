# coding=utf8
from os import system
from random import choice
from subprocess import Popen

from Tkinter import BOTH, Tk, Label

SAY_VOICE = 'Satu'
SIDES = (
    (u'VASEN', 'left'),
    (u'OIKEA', 'right'),
)
LIMBS = (
    (u'JALKA', 'foot'),
    (u'KÄSI', 'hand')
)
COLORS = (
    ('#C00', u'PUNAINEN', 'red'),
    ('#FB3', u'KELTAINEN', 'yellow'),
    ('#09C', u'SININEN', 'blue'),
    ('#690', u'VIHREÄ', 'green'),
)


def instruction():
    side, side_en = choice(SIDES)
    limb, limb_en = choice(LIMBS)
    color, color_text, color_en = choice(COLORS)
    return color, u' '.join([side, limb, color_text])


def main():
    root = Tk()
    root.overrideredirect(True)
    root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(),
                                       root.winfo_screenheight()))
    root.focus_set()

    color, text = instruction()

    label = Label(root, text=text, fg=color, font='-size 100 -weight bold')
    label.pack(fill=BOTH, expand=1)

    root.after(0, lambda: Popen(['say', '--voice', SAY_VOICE, text]))
    root.after(5000, lambda: root.quit())
    root.mainloop()


if __name__ == '__main__':
    main()
