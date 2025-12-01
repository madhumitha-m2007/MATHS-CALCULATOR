import streamlit as st
import sympy as sp

st.set_page_config(page_title="Cayley–Hamilton Calculator")

st.title("Calculator")
st.write("Enter a square matrix. Rows may be separated by newlines; entries by spaces or commas.")

matrix_input = st.text_area("Matrix (each row on a new line):", "2 1\n1 2")

if st.button("Compute Cayley–Hamilton"):
    try:
        # Parse matrix
        rows = [r.strip() for r in matrix_input.split("\n") if r.strip()]
        mat = [ [sp.sympify(e) for e in row.replace(",", " ").split()] for row in rows ]
        
        A = sp.Matrix(mat)

        if A.rows != A.cols:
            st.error("Matrix must be square.")
        else:
            st.subheader("Input matrix (A)")
            st.write(A)

            # Characteristic polynomial
            x = sp.symbols("x")
            charpoly = A.charpoly(x)
            poly_expr = sp.expand(charpoly.as_expr())

            st.subheader("Characteristic polynomial p(x)")
            # IMPORTANT: no p(x) calling of Symbol — only plain LaTeX output
            st.latex("p(x) = " + sp.latex(poly_expr))

            # Evaluate p(A)
            coeffs = charpoly.all_coeffs()  # highest degree first
            n = A.rows
            pA = sp.zeros(n)

            for i, c in enumerate(coeffs):
                power = len(coeffs) - i - 1
                if power == 0:
                    pA += c * sp.eye(n)
                else:
                    pA += c * (A ** power)

            st.subheader("Matrix p(A)")
            st.write(pA)

            if pA == sp.zeros(n):
                st.success("Cayley–Hamilton verified exactly: p(A) = 0.")
            else:
                st.warning("p(A) is not zero. Something unexpected happened.")

    except Exception as e:
        st.error(f"Error: {e}")

