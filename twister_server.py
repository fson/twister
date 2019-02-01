# coding=utf8
import sys
from os import system
from random import choice
from subprocess import Popen

from Tkinter import BOTH, X, Tk, Label, StringVar

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
    return color, u'{} {}, {}'.format(side, limb, color_text)


def main(interval):
    root = Tk()
    root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(),
                                       root.winfo_screenheight()))

    label_var = StringVar()
    label = Label(root, textvariable=label_var, font='-size 100 -weight bold')
    label.pack(fill=BOTH, expand=1)

    time_var = StringVar()
    time = Label(root, textvariable=time_var, font='-size 70 -weight bold')
    time.pack(fill=X)

    def next_instruction(event=None):
        color, text = instruction()
        label_var.set(text)
        label.config(fg=color)
        Popen(['say', '--voice', SAY_VOICE, text])

    def make_count_step(time_s):
        def step():
            time_var.set(time_s if time_s > 0 else '')
        return step

    def countdown(min, max):
        for n in range(min, max + 1):
            root.after(1000 * n, make_count_step(max - n))

    def step():
        next_instruction()
        countdown(1, interval)
        root.after(interval * 1000, step)

    def loop_instructions():
        countdown(0, 5)
        root.after(5000, step)

    def quit(event):
        root.quit()

    label.bind('<space>', next_instruction)
    label.bind('<Escape>', quit)
    label.focus_set()

    loop_instructions()
    root.mainloop()


if __name__ == '__main__':
    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    main(interval)
