import matplotlib.pyplot as plt
import pandas as pd

# Import your data
df = pd.read_csv('survey_dat.txt', delimiter='\t', header=0, nrows=30)

surveys = df.iloc[:, 0]
year = df.iloc[:, 1]
wave = df.iloc[:, -1]

print(surveys)

# Define your data
wavelength_bands = wave.unique()  # Use unique() to keep the order
years = sorted(year.unique())  # Replace with your years

# Create a mapping from wavelength bands to numerical values for the x-axis
wave_mapping = {band: i for i, band in enumerate(wavelength_bands)}

# Create a plot
fig, ax = plt.subplots()

# Define a color map based on unique 'Wavelength' values
color_map = plt.cm.get_cmap('rainbow_r', len(wavelength_bands))

# Set a common symbol style for all data points
marker_style = 'X'  # Change to your preferred symbol style

# Iterate through the data and plot points with labels
for i in range(len(surveys)):
    survey_name = surveys[i]
    survey_year = year[i]
    survey_band = wave[i]

    x = wave_mapping[survey_band]
    y = survey_year
    label = f'{survey_name}'  # Adjust this label format as needed

    color = color_map(x / len(wavelength_bands))  # Assign a unique color based on the 'Wavelength' label
    
    ax.scatter(x, y, s=50, label=label, marker=marker_style, color=color)

# Set labels and ticks
ax.set_xticks(range(len(wavelength_bands)))
ax.set_xticklabels(wavelength_bands)
ax.set_xlabel('Wavelength Bands')
ax.set_ylabel('Years')
ax.set_title('Observed Wavelength Bands')
ax.grid(True, alpha=0.5)

# Add a legend

# legend = ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Surveys', fontsize=8)
# legend.set_bbox_to_anchor((1.01, 0.8))


plt.tight_layout()
plt.show()
