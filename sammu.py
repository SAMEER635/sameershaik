import streamlit as st
import math

# Title of the app
st.title("2305a21l61-PS08")
st.write("Calculate the winding resistance(R1) and winding reactance (X1)  based on short circuit measurements like we VSC ISC and WSC")

# Function to calculate R1 and X1
def Tran_Eff(VSC, ISC, WSC):
    ZSC = VSC / ISC  # impedance
    R1 = WSC / (ISC ** 2)  # resistance
    X1 = math.sqrt(ZSC**2 - R1**2)  # reactance
    return R1, X1

# Streamlit app
def main():
    col1, col2 = st.columns(2)

    with col1:
        # User inputs
        st.subheader("input parameters")
        VSC = st.number_input("Enter VSC:", value=100.0)
        ISC = st.number_input("Enter ISC:", value=100.0)
        WSC = st.number_input("Enter WSC:", value=100.0)
        a=st.button("Calculate")

    with col2:
        
        # Calculate and display results when the user presses the button
        if a:
            st.subheader("output parameters")
            R1, X1 = Tran_Eff(VSC, ISC, WSC)
            st.write(f"R1: {R1:.2f} ohms")
            st.write(f"X1: {X1:.2f} ohms")

if __name__ == "__main__":
    main()