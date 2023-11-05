#import packages
import math as m
import statistics as stat
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from astropy.coordinates import SkyCoord, Galactic
from astropy.visualization.wcsaxes import SphericalCircle
import astropy.units as u

#%%
df = pd.read_csv('AllSkyLoc1.csv')

# Create a list to store valid SkyCoord objects
valid_coords = []

# Convert the coordinates to SkyCoord objects with error handling
for index, row in df.iterrows():
    try:
        if row['Type'] == 'hms':
            coord_str = f"{row['RA']} {row['Dec']}"
            coord = SkyCoord(coord_str,  unit=(u.hourangle, u.deg))
        else:
            coord = SkyCoord(row['RA'], row['Dec'], unit=(u.deg, u.deg))
        valid_coords.append(coord)
    except Exception as e:
        print(f"Error parsing coordinates at index {index}: {str(e)}")
        continue

#valid_coords.galactic
# Create a 'SkyCoord' column in the DataFrame
df['SkyCoord'] = valid_coords

#%%
# Create a projection plot
fig, ax = plt.subplots(figsize = (8,10), subplot_kw={'projection': 'aitoff'})

# Extract RA and Dec from the SkyCoord objects in the DataFrame
ra = [coord.ra.wrap_at(180 * u.deg) for coord in df['SkyCoord']]
dec = [coord.dec for coord in df['SkyCoord']]


ra_vals = []
dec_vals = []

for i in range(0, len(ra)):
    ra_vals.append(ra[i].value)
    dec_vals.append(dec[i].value)
# Plot the points
ax.scatter(ra_vals, dec_vals, s=10, label='Astronomical Coordinates', alpha = 0.5)


# Define the galactic coordinates for the galactic plane
l_value = np.linspace(0, 360-0.01, 100)
b_value = [0] * 100 



# Convert galactic coordinates to equatorial coordinates
gal_plane = SkyCoord(l=l_value, b=b_value, frame=Galactic, unit = 'deg').icrs

# Get the corresponding equatorial coordinates


#gal_ra = gal_ra*u.deg
#gal_dec = gal_dec*u.deg

print(gal_plane[0])

# Plot the galactic plane
plt.plot(gal_plane.ra*u.rad, gal_plane.dec*u.rad, linestyle='-', color='b')



# Customize the plot as needed
ax.set_title('Survey Coverage')
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid()

plt.show()

#plt.savefig('skyPlot.png', bbox_inches = 'tight', dpi = 200)