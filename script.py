#Code is originally written by Professor Richard Pattis' of
#of University Of Califorina, Irvine. I made no modifications
#in this module.

#The script is what runs the program
import view
import controller

#The game starts out easy and progressively becomes more difficult

controller.repeater(view.root)
view.root.mainloop()
