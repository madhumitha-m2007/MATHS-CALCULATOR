import streamlit as st
import numpy as np
from math import sin, cos, tan, exp, sqrt, pi

st.title("Double Integral Calculator (No SciPy Needed)")
st.write("Compute double integrals in polar coordinates including cardioid regions")

# Allowed safe names for eval
safe = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "exp": np.exp,
    "sqrt": np.sqrt,
    "pi": np.pi
}

# User inputs
func_str = st.text_input("Enter function f(r,θ):", "r*sin(theta)")
r_min = st.text_input("r minimum:", "0")
r_max = st.text_input("r maximum:", "1 + cos(theta)")  # cardioid example
theta_min = st.text_input("θ minimum:", "0")
theta_max = st.text_input("θ maximum:", "2*pi")

n = st.slider("Integration resolution (higher = more accuracy)", 200, 2000, 800)

if st.button("Compute Integral"):
    try:
        # Convert strings into functions
        def f(r, theta):
            return eval(func_str, {**safe, "r": r, "theta": theta})

        def r_lower(theta):
            return eval(r_min, {**safe, "theta": theta})

        def r_upper(theta):
            return eval(r_max, {**safe, "theta": theta})

        t1 = eval(theta_min, safe)
        t2 = eval(theta_max, safe)

        # Create theta grid
        theta_vals = np.linspace(t1, t2, n)
        total = 0

        # Numerical integration (Riemann sum)
        for th in theta_vals:
            rl = r_lower(th)
            ru = r_upper(th)
            r_vals = np.linspace(rl, ru, n)
            # Polar area element = r dr dθ
            integrand = f(r_vals, th) * r_vals
            total += np.trapz(integrand, r_vals)

        # Multiply by Δθ
        total *= (t2 - t1) / n

        st.success(f"Result of the double integral = **{total:.5f}**")

    except Exception as e:
        st.error(f"Error: {e}")
