# Landau levels
Some functions that plot, on the same canvas, both the density of states and the fermi level (for 2D and 3D landau levels).

Even though the landau levels' energies depend on the magnetic field $B$ and the area of the sheet (or the cross section in 3D) separately, we choose to normalize
the energy $\epsilon$ in such a way that it becomes dimensionless and the landau levels depend only on the flux of the $B$ field:
$$\tilde{\epsilon}_{n,n_z}= Z(\frac12 + n)+\pi n_z^2$$
where $Z=\frac{\Phi}{\Phi_0}$ is the number of quantum fluxes that pass through the system.\\
So the normalized landau levels are dimensionless and depend just on the flux $\Phi$.

## Visualization of $g(\epsilon)$ and $\epsilon_f$
### "plot_density2D(Z,n_max)" or "plot_density3D(Z,n_max)"
Plots the densiy of states $g(\epsilon)$ as a function of the normalized _dimensionless energy_ $\tilde{\epsilon}$, for a system
with $Z$ quantums of magnetic flux, until the energy of the $n_{max}$-th energy level.
- 2D_\\
AAA
