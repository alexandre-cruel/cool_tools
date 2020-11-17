"""Example of python widgets that can be used in python notebooks"""

from ipywidgets import interact, interactive, fixed
from IPython.display import display
import ipywidgets as widgets


def func(x):
    return x


display(interact(func, x=10))


@interact(x=True, y=fixed(1.0))
# decorator allows to pass default values for x and fixed one for y
def g(x, y):
    return (x,y)


# pour definir les valeurs que je veux sur ma barre de valeur
interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))

# pour definir un dropdown menu
interact(func, x=["option1", "option2", "option3"])

w = widgets.IntSlider()
display(w)
w.value()  # returns the value set for that widget

#  widgets.IntProgress() barre de progression avec couleur en fonction de l'etat du produit


