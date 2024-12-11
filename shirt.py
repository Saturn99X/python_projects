import matplotlib.pyplot as plt
import numpy as np

# Paramètres du trou noir
radius = 33
event_horizon = 15.5 * radius

# Création de la figure et de l'axe
fig, ax = plt.subplots(figsize=(8, 8))

# Disque noir représentant le trou noir
black_hole = plt.Circle((0, 0), radius, color='blue')

# Anneau lumineux pour l'effet de lentille gravitationnelle
theta = np.linspace(0, 2 * np.pi, 100)
x = event_horizon * np.cos(theta)
y = event_horizon * np.sin(theta)

# Ajout des éléments à la figure
ax.add_patch(black_hole)
ax.plot(x, y, color='yellow', linewidth=2)

# Ajustement des axes
ax.set_xlim(-3 * radius, 3 * radius)
ax.set_ylim(-3 * radius, 3 * radius)
ax.set_aspect('equal', 'box')

# Suppression des axes
ax.axis('off')

# Affichage du trou noir
plt.show()