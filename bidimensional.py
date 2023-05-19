import numpy as np
import matplotlib.pyplot as plt

def deg2D(Z):
    """Degeneracy of each landau level"""
    return Z
def landau2D(Z,n):
    """(Dimensionless) Energy of the n-th landau level"""
    return Z*(0.5+n)
def fermi_level(Z,N):
    """Fills the states and finds the fermi level"""
    # Fill the states 'from below' with the N electrons
    n = 0
    while N > 0:
        N = N - deg2D(Z)
        n = n + 1
    fermi_energy = landau2D(Z,n)
    return fermi_energy
def plot_density(Z,n_max):
    """Plot the number of states for each value of energy (in 2D is discrete) UNTIL the n_max-th landau level"""
    # Calculate dimensionless energy of each landau level
    norm_levels = landau2D(Z,np.arange(0,n_max+1))
    fig, ax = plt.subplots()
    for n in np.arange(0,n_max):    
        ax.axvline(norm_levels[n],linewidth=4)
    ax.set_ylim(0,deg2D(Z))
    ax.set_ylabel("g($\epsilon$)")
    ax.set_xlabel("Dimensionless Energy $\epsilon$")
    ax.set_title("The vertical lines are $\delta$ with the\nheight specified in the plot\n$Z=\Phi/\Phi_0=$"+str(Z))
    return fig, ax
def plot_fermi_over_density(Z,N,n_max):
    """Plot Fermi level over the density plot"""
    fermi_energy = fermi_level(Z,N)
    fig, ax = plot_density(Z,n_max)
    ax.axvline(fermi_energy, color="black")
    ax.set_title("The vertical lines are $\delta$ with the\nheight specified in the plot\nThe black line is at $\epsilon_f$\n$Z=\Phi/\Phi_0=$"+str(Z))
    return fig, ax