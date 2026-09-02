#PERCENTAGE YIELD CALCULATIONS:

#STAGE 1: Synthesis of Nickel (II) Ammine Complex

#1. Starting material, nicl2_6h2o = Nickel (II) chloride hexahydrate
mass_of_nicl2_6h2o = 2.97 #g
molar_mass_of_nicl2_6h2o = 237.69 #g/mol
#Calculate moles of Nickel (II) chloride hexahydrate
moles_of_nicl2_6h2o = mass_of_nicl2_6h2o / molar_mass_of_nicl2_6h2o #mol
print(f"Moles of Nickel (II) chloride hexahydrate: {moles_of_nicl2_6h2o:.3g}")

#2. Reactant, nh4bf4 = Ammonium tetrafluoroborate
mass_of_nh4bf4 = 2.55 #g
molar_mass_of_nh4bf4 = 104.85 #g/mol
#Calculate moles of Ammonium tetrafluoroborate
moles_of_nh4bf4 = mass_of_nh4bf4 / molar_mass_of_nh4bf4 #mol
print(f"Moles of Ammonium tetrafluoroborate: {moles_of_nh4bf4:.3g}")

#3. Product, nickel_ammine = Nickel (II) Ammine Complex
actual_mass_of_nickel_ammine = 2.65 #g
molar_mass_of_nickel_ammine = 334.49 #g/mol
#Calculate moles of Nickel (II) Ammine Complex
actual_moles_of_nickel_ammine = actual_mass_of_nickel_ammine / molar_mass_of_nickel_ammine #mol
print(f"Moles of Nickel (II) Ammine Complex: {actual_moles_of_nickel_ammine:.3g}")

#4. Limiting Reagent Calculations
#Calculate the maximum number of moles of product each reactant can produce
theoretical_moles_from_nicl2_6h2o = moles_of_nicl2_6h2o
theoretical_moles_from_nh4bf4 = moles_of_nh4bf4 / 2

#The smaller value determines the limiting reagent
theoretical_moles_of_nickel_ammine = min(theoretical_moles_from_nicl2_6h2o, theoretical_moles_from_nh4bf4)
print(f"Theoretical moles of Nickel (II) Ammine Complex: {theoretical_moles_of_nickel_ammine:.3g}")

#Calculating the theoretical mass of Nickel (II) Ammine Complex
theoretical_mass_of_nickel_ammine = theoretical_moles_of_nickel_ammine * molar_mass_of_nickel_ammine
print(f"Theoretical mass of Nickel (II) Ammine Complex: {theoretical_mass_of_nickel_ammine:.3g}")

#Percentage Yield Calculation:
percentage_yield = (actual_mass_of_nickel_ammine / theoretical_mass_of_nickel_ammine) * 100
print(f"Percentage yield of Nickel (II) Ammine Complex is {percentage_yield:.3g} percent.") #%

####################

#STAGE 2: Synthesis of Ni(HDMG)2
#1. Starting material, nac = Nickel (II) Ammine Complex
actual_portion_mass_of_nickel_ammine = 0.28 #g
molar_mass_of_nickel_ammine = 334.49 #g/mol
portion_moles_of_nickel_ammine = actual_portion_mass_of_nickel_ammine / molar_mass_of_nickel_ammine
print(f"The moles of 0.28g of Nickel (II) Ammine Complex: {portion_moles_of_nickel_ammine:.3g}")

#2. Product, nihdmg = Ni(HDMG)2
actual_mass_of_nihdmg = 0.14 #g
molar_mass_of_nihdmg = 288.92 #g/mol
#Calculate moles of Ni(HDMG)2
moles_nihdmg = actual_mass_of_nihdmg / molar_mass_of_nihdmg #mol
print(f"Moles of Ni(HDMG)2: {moles_nihdmg:.3g}")

#Calculating the theoretical mass of Ni(HDMG)2
theoretical_mass_of_nihdmg = portion_moles_of_nickel_ammine * molar_mass_of_nihdmg
print(f"Theoretical mass of Ni(HDMG)2: {theoretical_mass_of_nihdmg:.3g}")

#Percentage Yield Calculation:
percentage_yield = (actual_mass_of_nihdmg / theoretical_mass_of_nihdmg) * 100
print(f"Percentage yield of Ni(HDMG)2 is {percentage_yield:.3g} percent.") #%