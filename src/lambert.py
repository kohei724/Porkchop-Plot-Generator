import numpy as np
import matplotlib.pyplot as plt
from poliastro.plotting.static import StaticOrbitPlotter
from poliastro.bodies import Earth, Sun
from poliastro.maneuver import Maneuver
from poliastro.util import time_range
from poliastro import ephem

# TLEデータを使って軌道を計算 (一例)
orbital_data = ephem.readtle('ISS', '1 25544U 98067A   22337.54041071  .00002113  00000-0  51544-4 0  9999')
orbital_plot = StaticOrbitPlotter(plt.gca())
orbital_plot.plot(orbital_data, label="Orbit")

plt.show()
