import matplotlib.pyplot as plt
import pandas as pd
from itertools import cycle
from matplotlib.cm import get_cmap
# Import your data
df = pd.read_csv('survey_dat.txt', delimiter='\t', header=0, nrows=28)

surveys = df.iloc[:, 0]
year = df.iloc[:, 1]
wave = df.iloc[:, -1]

# Define your data
wavelength_bands = wave.unique()  # Use unique() to keep the order
years = sorted(year.unique())  # Replace with your years

# Create a mapping from wavelength bands to numerical values for the x-axis
wave_mapping = {band: i for i, band in enumerate(wavelength_bands)}

# Create a custom colormap with more than 30 distinct colors
custom_color_list = [
    '#4E79A7', '#A0CBE8', '#F28E2B', '#FFBE7D', '#59A14F',
    '#8CD17D', '#B6992D', '#F1CE63', '#499894', '#86BCB6',
    '#E15759', '#FF9D9A', '#79706E', '#BAB0AC', '#D37295',
    '#FABFD2', '#B07AA1', '#D4A6C8', '#9D7660', '#D7B5A6',
    '#61C0BF', '#B274B2', '#7A6FAC', '#C6A86B', '#465D61',
    '#DAE300', '#75ADAE', '#D4A76D', '#A574B2', '#99E600'
]
# Create the plot
fig, ax = plt.subplots()


#Get a colormap and create a cycle of distinct colors based on the number of data points
# Get a cycle of custom colors
colors = iter(custom_colors)


# Iterate through the data and plot points with labels
for i in range(len(surveys)):
    survey_name = surveys[i]
    survey_year = year[i]
    survey_band = wave[i]

    x = wave_mapping[survey_band]
    y = survey_year
    label = f'{survey_name}'   # Adjust this label format as needed
    
    color = next(colors)  # Assign a unique color to each data point'
    
    ax.scatter(x, y, s=50, label = label, color = color)

    # Add label text next to the data point with an offset
   # ax.annotate(label, (x, y), textcoords='offset points', xytext=(offset_x, offset_y), fontsize=10)

# Set labels and ticks
ax.set_xticks(range(len(wavelength_bands)))
ax.set_xticklabels(wavelength_bands)
ax.set_xlabel('Wavelength Bands')
ax.set_ylabel('Years')
ax.set_title('Observed Wavelenth Bands')
ax.grid(True)

# Add a legend
ax.legend(loc= [1, 0], title='Surveys', fontsize = 8)

plt.tight_layout()
plt.show()