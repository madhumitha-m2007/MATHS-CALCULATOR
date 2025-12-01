import streamlit as st
import sympy as sp

st.set_page_config(page_title="Maxima–Minima Calculator")

st.title("Maxima–Minima Calculator")
st.write("Enter a function of x to find critical points and classify maxima/minima.")

# Input function
func_input = st.text_input("Enter f(x):", "x**3 - 3*x + 2")

# Button to compute
if st.button("Compute Maxima/Minima"):
    try:
        # Define variable
        x = sp.symbols('x')

        # Convert input string to SymPy expression
        f = sp.sympify(func_input)

        st.subheader("Function f(x)")
        st.latex("f(x) = " + sp.latex(f))

        # First derivative
        f1 = sp.diff(f, x)
        st.subheader("First derivative f'(x)")
        st.latex("f'(x) = " + sp.latex(f1))

        # Second derivative
        f2 = sp.diff(f1, x)
        st.subheader("Second derivative f''(x)")
        st.latex("f''(x) = " + sp.latex(f2))

        # Solve f'(x) = 0 for critical points
        critical_points = sp.solve(f1, x)

        st.subheader("Critical Points (solutions of f'(x) = 0)")
        if len(critical_points) == 0:
            st.warning("No critical points found.")
        else:
            st.write(critical_points)

        # Classify critical points using second derivative test
        st.subheader("Classification of Critical Points")

        for cp in critical_points:
            second_deriv_value = f2.subs(x, cp)

            st.write(f"At x = {cp}:")

            if second_deriv_value > 0:
                st.success(f"Minimum at x = {cp}, since f''(x) > 0")
            elif second_deriv_value < 0:
                st.success(f"Maximum at x = {cp}, since f''(x) < 0")
            else:
                st.warning(f"Inconclusive (f''(x) = 0). Need further analysis.")

    except Exception as e:
        st.error(f"Error: {e}")
