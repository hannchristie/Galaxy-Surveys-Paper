import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle
import numpy as np



# Import your data
df = pd.read_csv('survey_dat.txt', delimiter='\t', header=0, nrows=50)

surveys = df.iloc[:, 0]
year = df.iloc[:, 1]
print(year)
wave = df.iloc[:, -2]
s_type = df.iloc[:, -1]


# Define your data
wavelength_bands = wave.unique()  # Use unique() to keep the order
years = sorted(year.unique())  # Replace with your years

# Create a mapping from wavelength bands to numerical values for the x-axis
wave_mapping = {band: i for i, band in enumerate(wavelength_bands)}

# Create a plot
fig, ax = plt.subplots()

# Define a color map based on unique 'Wavelength' values
color_map = plt.cm.get_cmap('Spectral', len(wavelength_bands)+2)


# Iterate through the data and plot points with labels
for i in range(len(surveys)):
    survey_name = surveys[i]
    survey_year = year[i]
    survey_band = wave[i]
    survey_type = s_type[i]

    x = wave_mapping[survey_band]
    y = survey_year
    #label = f'{survey_name}'  # Adjust this label format as needed

    color = color_map(x / len(wavelength_bands))  # Assign a unique color based on the 'Wavelength' label
    ax.scatter(x, y, s=80, marker= 'o', color=color, zorder=1)
    ax.scatter(x,y, s=85,  marker = 'o', facecolors='none', edgecolors='black', alpha = 0.75)

    if survey_type == 'Imaging':
        marker_style = 'o'  # Circle marker for 'imaging'
        size = 25
        label = 'Imaging'
    elif survey_type == 'Spec':
        marker_style = 'x'  # X marker for 'Spec'
        size  = 30
        label = 'Spec'

    elif survey_type == 'Both':
        marker_style = '*'  # Star marker for 'both'
        size = 25
        label = 'both'
    #ax.scatter(x, y, s=size, label=label, marker=marker_style, color='black', zorder=2, alpha = 0.5)

    survey_name = surveys[i]
    survey_year = year[i]
    survey_band = wave[i]

    x = wave_mapping[survey_band]
    y = survey_year
    label = f'{survey_name}'  # Adjust this label format as needed

    color = color_map(x / len(wavelength_bands))  # Assign a unique color based on the 'Wavelength' label
    
    #ax.scatter(x, y, s=50, label=label, marker=marker_style, color=color)

# Set labels and ticks
ax.set_xticks(range(len(wavelength_bands)))
ax.set_xticklabels(wavelength_bands)
ax.set_xlabel('Wavelength Bands')
ax.set_ylabel('Years')
ax.set_title('Observed Wavelength Bands')
ax.grid(True, alpha=0.5)

# Add a legend
label_handles = ['Imaging', 'Spec', 'Both']
#legend = ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Types of Surveys', fontsize=8)
#legend.set_bbox_to_anchor((1.01, 0.8))
#plt.legend()

plt.tight_layout()
#plt.show()
plt.savefig('obs_bands.png', dpi = 200)

#%%
min_num = min(num_G)
