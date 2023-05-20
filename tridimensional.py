from bidimensional import *

def landau3D(Z,n,nz):
    """(Dimensionless) Energy of the n-th landau level"""
    return Z*(0.5+n) + np.pi*nz**2
def fermi_level3D(Z,N):
    """Fills the states and finds the fermi level"""
    # Fill the states 'from below' with the N electrons
    n = 0
    nz = 0
    while N > 0:
        N = N - deg2D(Z)
        if nz != 0:
            N = N - deg2D(Z)
        if landau3D(Z,n,nz+1) > landau3D(Z,n+1,0):
            nz = 0
            n = n + 1
        else:
            nz = nz + 1
    fermi_energy = landau3D(Z,n,nz)
    return fermi_energy
def density(Z,num_levels):
    """Returns g(\epsilon) for the first 'num_levels' energy levels \epsilon_{n,nz}
    Note: The derivative dN/dE is extimated as a ratio between distance from two levels and degeneracy of the new level,
          where the energy associated to g(epsilon) is the one of the NEW level
    """
    g = np.zeros(num_levels)    #g(E) function
    energy_levels = np.zeros(num_levels)    #Values of E where we calculate g(E)
    # Fill the states 'from below' and save number of added particles x each new energy level filled
    n = 0
    nz = 1  # Start from filling the second level (to avoid dE=0, see below)
    level_index = 1
    E_old = 0
    while level_index < num_levels:
        # Calc energy (dE) and states (dN) gained increasing energy to the next level
        # and so the g(E)=dN/dE
        dE = landau3D(Z,n,nz) - E_old
        dN = deg2D(Z)
        if nz != 0:
            dN = dN + deg2D(Z)
        g[level_index] = dN/dE
        E_old = landau3D(Z,n,nz)
        energy_levels[level_index] = E_old
        # Go to the next level
        if landau3D(Z,n,nz+1) > landau3D(Z,n+1,0):
            nz = 0
            n = n + 1
        else:
            nz = nz + 1
        level_index = level_index + 1
    return energy_levels, g
def plot_density3D(Z,num_levels):
    """Plot the density of states for the first 'num_levels' levels"""
    # Calculate dimensionless energy of each landau level
    energies, g = density(Z,num_levels)
    fig, ax = plt.subplots()
    ax.plot(energies,g)
    ax.set_ylabel("g($\epsilon$)")
    ax.set_xlabel("Dimensionless Energy $\epsilon$")
    ax.set_title("$Z=\Phi/\Phi_0=$"+str(Z))
    return fig, ax
def plot_fermi_over_density3D(Z,N,num_levels):
    """Plot Fermi level over the density plot"""
    fermi_energy = fermi_level3D(Z,N)
    fig, ax = plot_density3D(Z,num_levels)
    ax.axvline(fermi_energy, color="black")
    ax.set_title("The vertical lines are $\delta$ with the\nheight specified in the plot\nThe black line is at $\epsilon_f$\n$Z=\Phi/\Phi_0=$"+str(Z))
    return fig, ax