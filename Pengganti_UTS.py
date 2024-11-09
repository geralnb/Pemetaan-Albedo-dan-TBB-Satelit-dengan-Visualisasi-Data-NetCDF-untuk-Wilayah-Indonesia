import os
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from datetime import datetime
from matplotlib.colors import LinearSegmentedColormap

# Atur lingkungan Cartopy
os.environ["CARTOPY_USER_BACKGROUNDS"] = "C:/Users/Geral/Downloads/Documents/ne_10m_coastline"

# Daftar file NetCDF yang ingin digunakan
file_paths = [
    'C:/Users/Geral/Documents/Data_Himawari/NC_H09_20240102_1200_R21_FLDK.02401_02401.nc',
    'C:/Users/Geral/Documents/Data_Himawari/NC_H09_20240102_1210_R21_FLDK.02401_02401.nc',
    'C:/Users/Geral/Documents/Data_Himawari/NC_H09_20240102_1220_R21_FLDK.02401_02401.nc',
    'C:/Users/Geral/Documents/Data_Himawari/NC_H09_20240102_1230_R21_FLDK.02401_02401.nc',
    'C:/Users/Geral/Documents/Data_Himawari/NC_H09_20240102_1240_R21_FLDK.02401_02401.nc',
    'C:/Users/Geral/Documents/Data_Himawari/NC_H09_20240102_1250_R21_FLDK.02401_02401.nc'
]

# Atur koordinat
lon_min, lon_max = 118, 125.5
lat_min, lat_max = -6.0, 6.0

# Buat colormap kustom untuk gradasi warna dengan RGBA
colors = [(1, 1, 1, 1), (224/255, 178/255, 69/255, 1)]  # dari putih ke rgb(224, 178, 69) dengan opacity penuh
cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

# Buat subplots, satu untuk setiap file
fig, axs = plt.subplots(1, len(file_paths), figsize=(15, 5), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot data untuk setiap file
for i, file_path in enumerate(file_paths):
    # Ekstrak waktu dari nama file (misalnya, "1200" dari "NC_H09_20240102_1200_R21_FLDK.02401_02401.nc")
    time_str = os.path.basename(file_path).split('_')[3]
    
    ds = xr.open_dataset(file_path)
    ax = axs[i]
    ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
    
    # Plot band 'albedo_03' dengan colormap kustom dan colorbar vertikal di sebelah kanan
    p = ds['albedo_03'].plot(ax=ax, transform=ccrs.PlateCarree(), add_colorbar=False, cmap=cmap)
    
    # Tambahkan garis pantai dan judul
    ax.coastlines(resolution='10m')
    ax.set_title(f"{time_str}")
    
    # Tambahkan gridlines tanpa garis tetapi dengan label koordinat
    gl = ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree())
    gl.xlines = False  # Nonaktifkan garis bujur
    gl.ylines = False  # Nonaktifkan garis lintang
    gl.top_labels = False  # Hapus label di atas
    gl.right_labels = False  # Hapus label di sebelah kanan
    gl.xlabel_style = {'size': 8, 'color': 'black'}
    gl.ylabel_style = {'size': 8, 'color': 'black'}
    
    # Tambahkan colorbar vertikal di samping kanan setiap plot
    cbar = plt.colorbar(p, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)

# Tambahkan label "Longitude" di bagian bawah dan "Latitude" di sisi kiri
fig.text(0.5, 0.02, "Longitude", ha='center', fontsize=12, color='black')
fig.text(0.04, 0.5, "Latitude", va='center', rotation='vertical', fontsize=12, color='black')

# Tambahkan waktu saat ini di pojok kanan bawah
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
fig.text(0.95, 0.01, f"{current_time}", ha='right', fontsize=10, color='black')

# Sesuaikan layout
plt.tight_layout()

# Simpan plot sebagai satu gambar
plt.savefig('albedo_03_Fix.png', dpi=300)

plt.show()
