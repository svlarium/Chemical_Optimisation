#To test that Python can successfully find and read the CSV
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#LOAD UV-VIS DATA

uvvis_data = pd.read_csv("../data/raw/nickel_chloride_uvvis.csv")

#SEPARATE THE DATA/ EXTRACT WAVELENGTH AND ABSORBANCE FROM EACH PEAK
wavelength = uvvis_data["Wavelength (nm)"]
absorbance = uvvis_data["Absorbance"]

#FIND PEAKS
peaks, properties = find_peaks(absorbance)

#Store detected peak information:
peak_data = []

#PRINT DETECTED PEAK POSITIONS
for peak in peaks:
    print(
        f"Peak at {wavelength.iloc[peak]:.2f} nm, " 
        f"Absorbance = {absorbance.iloc[peak]:.4f}"
    )

#CREATE UV-VIS PLOT FIGURE
fig, ax = plt.subplots(figsize=(10,6),dpi=150)

#PLOT EXPERIMENTAL UV-VIS SPECTRUM
ax.plot(
    uvvis_data["Wavelength (nm)"],
    uvvis_data["Absorbance"],
    linewidth=2
)
plt.plot(uvvis_data["Wavelength (nm)"], uvvis_data["Absorbance"])

# To add the peak labels, we can use Matplotlib's ax.annotate():
# AUTOMATICALLY MARK AND LABEL EVERY PEAK

for i, peak in enumerate(peaks, start=1):
    peak_wavelength = wavelength.iloc[peak]
    peak_absorbance = absorbance.iloc[peak]

    # PLOT THE PEAK MARKER
    ax.scatter(
        peak_wavelength,
        peak_absorbance,
        s=60
    )

    # VERTICAL DASHED LINE THROUGH PEAK
    ax.axvline(
        peak_wavelength,
        linestyle="--",
        alpha=0.5
    )
    # INDIVIDUAL LABEL POSITIONING
    if i == 1:
        label_position =(15,-20)
    elif i == 2:
        label_position =(2,15)
    else:
        label_position =(10,15)

    # ADD PEAK LABEL
    ax.annotate(
        f"Peak {i}\n"
        f"{peak_wavelength:.0f} nm\n"
        f"A = {peak_absorbance:.2f}",
        xy=(peak_wavelength, peak_absorbance),
        xytext=label_position,
        textcoords="offset points"
    )

#MARK THE DETECTED PEAKS
    ax.scatter(
    wavelength.iloc[peaks],
    absorbance.iloc[peaks],
    s=60,
label = "Detected peaks"
)
    peak_data.append({
        "Peak": i,
        "Wavelength (nm)": peak_wavelength,
        "Absorbance": peak_absorbance
    })

    # Turn the saved peak data into a pandas DataFrame:
peak_data = pd.DataFrame(peak_data)
    # Display/Print the Results
print(peak_data)

    # Save as a CSV
peak_data.to_csv(
        "../data/processed/detected_uvvis_peaks.csv",
    index=False
    )
#index=False means that pandas won't add an extra numbered column

#FORMAT THE GRAPH:

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

#SAVE THE FIGURE
plt.savefig("../figures/nickel_chloride_uvvis_FINAL.png",
            dpi=300,
            bbox_inches="tight"
            )

#Display the Graph
plt.show()
