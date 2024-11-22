import streamlit as st

st.title("2205A21033-PS9")
st.subheader("Calculate the efficiency of DC shunt generator at various loads")

def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    Ish = V / Rsh
    Ia = K * IL - Ish
    CUL = (Ish ** 2) * Rsh + (Ia ** 2) * Ra
    Eff = (K * V * IL / (K * V * IL + CL + CUL)) * 100
    return Eff, CUL


col1, col2 = st.columns(2)

with col1:
    V = st.number_input("V (in Volt):", value=100.0)
    IL = st.number_input(" IL :(in Amps):", value=10.0)
    Rsh = st.number_input(" Rsh:( in ohms):", value=10.0)
    Ra = st.number_input(" Ra :(in ohms):", value=10.0)
    CL = st.number_input(" CL :(in Watts):", value=100.0)
    K = st.number_input("K :(Watts):", value=1.0)
    compute = st.button("Compute")

with col2:
    if compute:
       
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rsh, Ra)
        st.write(f"Eff: {Eff:.2f}%")
        st.write(f"CUL: {CUL:.2f}Watts")
