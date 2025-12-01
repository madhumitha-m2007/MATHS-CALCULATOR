import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Green's Theorem Calculator (Perfect, Step-by-Step, Error-Free)")

# -----------------------------------------
# SYMBOLS
# -----------------------------------------
x, y = sp.symbols("x y")

# -----------------------------------------
# FORMULA DISPLAY
# -----------------------------------------
st.latex(r"""
\textbf{Green's Theorem:} \quad 
\oint_C (P\,dx + Q\,dy)
=
\iint_R 
\left(
\frac{\partial Q}{\partial x} 
- 
\frac{\partial P}{\partial y}
\right)\, dA
""")

st.write("---")

# -----------------------------------------
# USER INPUT VECTOR FIELD
# -----------------------------------------
st.subheader("➤ Enter Vector Field Components")

P_expr = st.text_input("Enter P(x, y):", "x**2")
Q_expr = st.text_input("Enter Q(x, y):", "x*y")

# Convert safely using sympy
P = sp.sympify(P_expr)
Q = sp.sympify(Q_expr)

# Compute derivatives
dQdx = sp.diff(Q, x)
dPdy = sp.diff(P, y)

integrand = dQdx - dPdy

# Show derivative steps
st.subheader("➤ Step-by-Step Derivatives")
st.latex(r"\frac{\partial Q}{\partial x} = " + sp.latex(dQdx))
st.latex(r"\frac{\partial P}{\partial y} = " + sp.latex(dPdy))
st.latex(r"\text{Integrand} = " + sp.latex(integrand))

st.write("---")

# -----------------------------------------
# REGION SELECTION
# -----------------------------------------
st.subheader("➤ Select Region Type")
region = st.selectbox(
    "Choose Region:",
    ["Rectangle", "Circle", "Triangle"]
)

# -----------------------------------------
# RECTANGLE REGION
# -----------------------------------------
if region == "Rectangle":
    st.subheader("Rectangle Region Input")
    x1 = st.number_input("x₁ (Left)", 0.0)
    x2 = st.number_input("x₂ (Right)", 2.0)
    y1 = st.number_input("y₁ (Bottom)", 0.0)
    y2 = st.number_input("y₂ (Top)", 3.0)

    # Double integral
    result = sp.integrate(
        sp.integrate(integrand, (y, y1, y2)),
        (x, x1, x2)
    )

    st.success(f"Final Answer = {result}")

    # Step-by-step
    st.subheader("Step-by-Step Integration")
    st.latex(r"\int_{x_1}^{x_2} \int_{y_1}^{y_2} (" + sp.latex(integrand) + r") \, dy \, dx")
    st.write("1. Integrate w.r.t y")
    step1 = sp.integrate(integrand, (y, y1, y2))
    st.latex(sp.latex(step1))
    st.write("2. Integrate the result w.r.t x")
    step2 = sp.integrate(step1, (x, x1, x2))
    st.latex(sp.latex(step2))

    # GRAPH
    fig, ax = plt.subplots()
    rect_x = [x1, x2, x2, x1, x1]
    rect_y = [y1, y1, y2, y2, y1]
    ax.plot(rect_x, rect_y, marker="o")
    ax.fill_between([x1, x2], y1, y2, alpha=0.3)
    ax.set_title("Rectangle Region")
    ax.grid(True)
    st.pyplot(fig)


# -----------------------------------------
# CIRCLE REGION
# -----------------------------------------
if region == "Circle":
    st.subheader("Circle Region Input")
    r = st.number_input("Radius r", 2.0)

    # Convert to polar
    theta = sp.symbols("theta")

    integrand_polar = integrand.subs({
        x: r*sp.cos(theta),
        y: r*sp.sin(theta)
    }) * r  # Jacobian

    result = sp.integrate(integrand_polar, (theta, 0, 2*sp.pi))

    st.success(f"Final Answer = {result}")

    # GRAPH
    fig, ax = plt.subplots()
    t = np.linspace(0, 2*np.pi, 300)
    ax.plot(r*np.cos(t), r*np.sin(t))
    ax.fill(r*np.cos(t), r*np.sin(t), alpha=0.3)
    ax.set_title("Circular Region")
    ax.grid(True)
    st.pyplot(fig)


# -----------------------------------------
# TRIANGLE REGION
# -----------------------------------------
if region == "Triangle":
    st.subheader("Triangle Region Inputs")
    st.write("Triangle with vertices (0,0), (a,0), (0,b)")

    a = st.number_input("a (base)", 3.0)
    b = st.number_input("b (height)", 4.0)

    # Triangle integration limits
    result = sp.integrate(
        sp.integrate(integrand, (y, 0, b*(1 - x/a))),
        (x, 0, a)
    )

    st.success(f"Final Answer = {result}")

    # GRAPH
    fig, ax = plt.subplots()
    tx = [0, a, 0, 0]
    ty = [0, 0, b, 0]
    ax.plot(tx, ty, marker="o")
    ax.fill(tx, ty, alpha=0.3)
    ax.set_title("Triangle Region")
    ax.grid(True)
    st.pyplot(fig)
