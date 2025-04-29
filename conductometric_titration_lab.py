import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Conductometric Titration Lab", layout="centered")

st.title("Conductometric Titration of HCl + CH₃COOH with NaOH")
st.write("""
This virtual lab simulates the titration of a strong acid (HCl) and a weak acid (CH₃COOH) mixture with NaOH.
""")

# Initial Inputs
sample_volume = st.slider("Volume of Acid Sample (mL)", 5.0, 20.0, 10.0)
naoh_normality = st.slider("NaOH Normality (N)", 0.05, 1.0, 0.1, 0.05)
va = st.slider("NaOH Volume for HCl Endpoint (mL)", 1.0, 4.0, 2.0)
vb = st.slider("NaOH Volume for CH₃COOH + HCl Endpoint (mL)", 5.0, 10.0, 6.5)

# Volume Range
volumes = np.arange(0, 8.1, 0.2)
conductance = []

# Simulated Conductance
for v in volumes:
    if v < va:
        c = 10 - v * 3  # Decreasing due to HCl
    elif v < vb:
        c = 4 + (v - va) * 1.5  # Gradual increase due to acetate salt
    else:
        c = 4 + (vb - va) * 1.5 + (v - vb) * 3  # Sharp increase due to OH⁻
    conductance.append(c)

# Plotting
fig, ax = plt.subplots()
ax.plot(volumes, conductance, marker='o')
ax.axvline(x=va, color='green', linestyle='--', label=f'HCl Endpoint ({va} mL)')
ax.axvline(x=vb, color='red', linestyle='--', label=f'CH₃COOH Endpoint ({vb} mL)')
ax.set_xlabel("Volume of NaOH Added (mL)")
ax.set_ylabel("Conductance (mS)")
ax.set_title("Conductometric Titration Curve")
ax.legend()
st.pyplot(fig)

# Calculations
n_hcl = (va * naoh_normality) / sample_volume
n_ch3cooh = ((vb - va) * naoh_normality) / sample_volume
w_hcl = n_hcl * 36.5
w_acetic = n_ch3cooh * 60.0

st.markdown("### Results")
st.write(f"**HCl in sample:** {w_hcl:.2f} g")
st.write(f"**Acetic Acid in sample:** {w_acetic:.2f} g")
