#To test that Python can successfully find and read the CSV
import pandas as pd
import matplotlib.pyplot as plt

#Load UV-Vis Data
uvvis_data = pd.read_csv("../data/raw/nickel_chloride_uvvis.csv")

#Create Figure
fig, ax = plt.subplots(figsize=(10,6),dpi=150)

#Plot UV-Vis Spectrum
ax.plot(
    uvvis_data["Wavelength (nm)"],
    uvvis_data["Absorbance"],
    linewidth=2
)
plt.plot(uvvis_data["Wavelength (nm)"], uvvis_data["Absorbance"])

#Add Axis Labels
ax.set_xlabel("Wavelength (nm)", fontsize=12)
ax.set_ylabel("Absorbance", fontsize=12)

#Title
ax.set_title("UV-Vis Spectrum of Nickel (II) Chloride Hexahydrate", fontsize=14)

#Improve Appearance
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#Make Layout Fit Nicely
plt.tight_layout()

#Save Figure
plt.savefig("../figures/nickel_chloride_uvvis.png",
            dpi=300,
            bbox_inches="tight"
     )

#Display the Graph
plt.show()

from scipy.signal import find_peaks

#Extract Wavelength and Absorbance from Each Peak
wavelength = uvvis_data["Wavelength (nm)"]
absorbance = uvvis_data["Absorbance"]

#Find Peaks
peaks, properties = find_peaks(absorbance)

#Print Peak Positions
for peak in peaks:
    print(f"Peak at {wavelength.iloc[peak]:.2f} nm, " 
    f"Absorbance = {absorbance.iloc[peak]:.4f}")



