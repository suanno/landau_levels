# Landau levels visualizator
Some functions that plot, on the same canvas, both the density of states and the fermi level (for 2D and 3D landau levels).

Even though the landau levels' energies depend on the magnetic field $B$ and the area of the sheet (or the cross section in 3D) separately, we choose to normalize
the energy in such a way that it becomes dimensionless and the landau levels become:
$$\tilde{\epsilon}_{n,n_z}= Z(\frac12 + n)+\pi n_z^2$$
so the normalized energy levels do not depend on the area of the system.
