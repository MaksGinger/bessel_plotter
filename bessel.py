import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib.widgets import TextBox,Button


class Bessel:
    def _numerator(self,p,v,x):
        return ((-1)**p)*((x/2)**(2*p+v))

    def _denominator(self,p,v):
        return sp.gamma(p+1)*sp.gamma(p+v+1)

    def bessel_of_first_kind(self,v,x):
        _sum = 0
        for p in range(0,110,1):
            _sum += self._numerator(p,v,x)/self._denominator(p,v)
        return _sum

bessel=Bessel()

def plot_2D(graph_axes,fig,v):
    x = np.linspace(0, 30, 1000)
    graph_axes.plot(x,bessel.bessel_of_first_kind(v,x)) 
    plt.draw()


def plot_3D():
    x = np.linspace(0, 20, 100)
    y = np.linspace(0, 20, 100)

    x, y = np.meshgrid(x, y)

    z=bessel.bessel_of_first_kind(y,x)

    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(111,projection='3d')

    h = ax.plot_surface(x, y, z, cmap='jet',edgecolor='k')
    plt.colorbar(h)

    ax.set_xlabel('X',fontweight='bold')
    ax.set_ylabel('Y',fontweight='bold')
    ax.set_zlabel('Z',fontweight='bold')

    plt.show()


def main():

    def onButtonClearClicked(event):
        graph_axes.clear()
        graph_axes.grid()
        graph_axes.set_xlabel('x')
        graph_axes.set_ylabel('${J}_n(x)$')
        graph_axes.set_xlim([0,30])
        graph_axes.set_ylim([-1.1,1.1])
        plt.draw()

    def onButton3DClicked(event):
        plot_3D()

    def submit(text):
        val=eval(text)
        plot_2D(graph_axes,fig,val)


    fig, graph_axes = plt.subplots()
    graph_axes.grid()
    graph_axes.set_xlabel('x')
    graph_axes.set_ylabel('${J}_n(x)$')
    graph_axes.set_xlim([0,30])
    graph_axes.set_ylim([-1.1,1.1])
    fig.subplots_adjust(left=0.13, right=0.95, top=0.95, bottom=0.4)


    axes_button_clear = plt.axes([0.05, 0.10, 0.4, 0.075])
    button_clear = Button(axes_button_clear, 'Очистить')
    button_clear.on_clicked(onButtonClearClicked)

    axes_button_3D = plt.axes([0.55, 0.10, 0.4, 0.075])
    button_3D = Button(axes_button_3D, '3D')
    button_3D.on_clicked(onButton3DClicked)
    
    axes_textbox = plt.axes([0.13, 0.20, 0.85, 0.08])
    text_box = TextBox(axes_textbox,'Порядок',initial=0)
    text_box.on_submit(submit)

   
    plt.show()

if __name__=='__main__':
    main()