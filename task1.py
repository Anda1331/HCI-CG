import math

# Get input from the user
Wpx = int(input("Enter horizontal resolution (pixels): "))
Hpx = int(input("Enter vertical resolution (pixels): "))
Dinches = float(input("Enter physical diagonal size (inches): "))

# Calculate total pixels
total_pixels = Wpx * Hpx

# Calculate simplified aspect ratio
gcd = math.gcd(Wpx, Hpx)
aspect_width = Wpx // gcd
aspect_height = Hpx // gcd

# Calculate diagonal pixel count
diagonal_pixels = math.sqrt(Wpx**2 + Hpx**2)

# Calculate DPI/PPI
dpi = diagonal_pixels / Dinches

# Classify display density
if dpi < 100:
    density = "Low Density (Standard Monitor)"
elif dpi <= 200:
    density = "Medium Density (HD Display)"
else:
    density = "High Density (Retina / Mobile)"

# Display results
print("\n DISPLAY METRICS ANALYSIS ")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio : {aspect_width}:{aspect_height}")
print(f"Calculated DPI : {dpi:.2f} DPI")
print(f"Density Category : {density}")