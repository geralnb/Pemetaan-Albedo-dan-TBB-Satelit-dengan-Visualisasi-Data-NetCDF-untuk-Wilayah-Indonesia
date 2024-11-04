import os
os.environ["CARTOPY_USER_BACKGROUNDS"] = "C:/Users/Geral/Downloads/Documents/ne_10m_coastline"
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Buka file NetCDF
file_path = 'C:/data_himawari/Sesuai_Absen/NC_H09_20240102_1200_R21_FLDK.02401_02401.nc'
ds = xr.open_dataset(file_path)

# Atur koordinat wilayah Indonesia
lon_min, lon_max = 95, 140
lat_min, lat_max = -10, 10

# List of variables to plot
bands = ['albedo_01', 'albedo_02', 'albedo_03', 'albedo_04', 'albedo_05', 'albedo_06',
         'tbb_07', 'tbb_08', 'tbb_09', 'tbb_10', 'tbb_11', 'tbb_12', 'tbb_13', 'tbb_14', 'tbb_15', 'tbb_16']

# Create subplots (4 rows x 4 columns)
fig, axs = plt.subplots(4, 4, figsize=(15, 15), subplot_kw={'projection': ccrs.PlateCarree()})

# Flatten the axes array for easy iteration
axs = axs.flatten()

# Plot each band in the list
for i, band in enumerate(bands):
    ax = axs[i]
    ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
    
    # Plot data with colorbar
    p = ds[band].plot(ax=ax, transform=ccrs.PlateCarree(), add_colorbar=False)
    
    # Add coastlines
    ax.coastlines(resolution='10m')
    ax.set_title(band.replace('_', ' ').capitalize())

    # Add a colorbar to each plot
    cbar = plt.colorbar(p, ax=ax, orientation='horizontal', fraction=0.046, pad=0.04)

# Adjust layout
plt.tight_layout()

# Save the plot as a single image
plt.savefig('NC_H09_20240102_1200_R21_FLDK.02401_02401.png', dpi=300)

plt.show()
