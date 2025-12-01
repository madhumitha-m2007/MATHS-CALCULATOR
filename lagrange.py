import streamlit as st
import sympy as sp

st.set_page_config(page_title="Lagrange Multiplier Calculator", layout="wide")

st.title("Lagrange Method Calculator")
st.write("This app computes extrema of functions using the Lagrange multiplier method.")
st.write("You can use trigonometric functions (sin, cos, tan), log, exp, etc.")

# -----------------------------------------------------------
# Allowed SymPy functions
# -----------------------------------------------------------
allowed = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "log": sp.log,
    "exp": sp.exp,
    "sqrt": sp.sqrt,
    "pi": sp.pi
}

# -----------------------------------------------------------
# User Input
# -----------------------------------------------------------
st.header("Enter your functions")

var_count = st.selectbox("Number of variables", [2, 3])

if var_count == 2:
    x, y, lam = sp.symbols("x y lam")
    vars_ = [x, y, lam]

    f_str = st.text_input("Enter objective function f(x, y):", "x**2 + y**2")
    g_str = st.text_input("Enter constraint g(x, y) = 0:", "x + y - 1")

    try:
        f = sp.sympify(f_str, allowed)
        g = sp.sympify(g_str, allowed)
    except Exception as e:
        st.error(f"Error in expression: {e}")
        st.stop()

    # Lagrangian
    L = f + lam * g

    st.subheader("Lagrangian Function")
    st.latex(sp.latex(L))

    # Partial derivatives
    eq1 = sp.diff(L, x)
    eq2 = sp.diff(L, y)
    eq3 = sp.diff(L, lam)

    st.subheader("Equations to Solve")
    st.latex(sp.latex(eq1))
    st.latex(sp.latex(eq2))
    st.latex(sp.latex(eq3))

    # Solve
    sol = sp.solve([eq1, eq2, eq3], [x, y, lam], dict=True)

    st.subheader("Solutions")
    st.write(sol)


# ------------------------------------------------------------------------
#  THREE VARIABLES
# ------------------------------------------------------------------------
if var_count == 3:
    x, y, z, lam = sp.symbols("x y z lam")
    vars_ = [x, y, z, lam]

    f_str = st.text_input("Enter objective function f(x, y, z):", "x**2 + y**2 + z**2")
    g_str = st.text_input("Enter constraint g(x, y, z) = 0:", "x + y + z - 1")

    try:
        f = sp.sympify(f_str, allowed)
        g = sp.sympify(g_str, allowed)
    except Exception as e:
        st.error(f"Error in expression: {e}")
        st.stop()

    L = f + lam * g

    st.subheader("Lagrangian Function")
    st.latex(sp.latex(L))

    eq1 = sp.diff(L, x)
    eq2 = sp.diff(L, y)
    eq3 = sp.diff(L, z)
    eq4 = sp.diff(L, lam)

    st.subheader("Equations to Solve")
    st.latex(sp.latex(eq1))
    st.latex(sp.latex(eq2))
    st.latex(sp.latex(eq3))
    st.latex(sp.latex(eq4))

    sol = sp.solve([eq1, eq2, eq3, eq4], [x, y, z, lam], dict=True)

    st.subheader("Solutions")
    st.write(sol)


st.markdown("---")
st.info("You can type expressions like `sin(x)`, `log(x)`, `cos(y)`, `exp(z)`, `tan(x+y)` etc.")
st.subheader("Solutions")

# Convert sympy solution dict to JSON friendly format
if sol:
    formatted_solutions = []
    for s in sol:
        formatted_solutions.append({str(k): str(v) for k, v in s.items()})
    st.write(formatted_solutions)
else:
    st.write("No solution found.")
import sympy as sp

x, y, lam = sp.symbols('x y lam')

f = sp.sin(x) + sp.cos(x)
g = x + y - 10

eq1 = sp.diff(f, x) - lam * sp.diff(g, x)
eq2 = sp.diff(f, y) - lam * sp.diff(g, y)
eq3 = g

solution = sp.solve([eq1, eq2, eq3], [x, y, lam], dict=True)
print(solution)