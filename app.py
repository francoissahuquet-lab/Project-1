"""Interfaz Streamlit para la calculadora."""
import streamlit as st

from src.calculator import add, subtract, multiply, divide

st.title("Calculadora")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Primer valor", value=0.0)
with col2:
    b = st.number_input("Segundo valor", value=0.0)

col_sum, col_sub, col_mul, col_div = st.columns(4)
sumar = col_sum.button("Sumar")
restar = col_sub.button("Restar")
multiplicar = col_mul.button("Multiplicar")
dividir = col_div.button("Dividir")

resultado = None
error = None

if sumar:
    resultado = add(a, b)
elif restar:
    resultado = subtract(a, b)
elif multiplicar:
    resultado = multiply(a, b)
elif dividir:
    try:
        resultado = divide(a, b)
    except ValueError:
        error = "No se puede dividir por cero. Introduce un valor distinto de cero."

if error:
    st.error(error)
elif resultado is not None:
    st.markdown(f"## Resultado: {resultado}")
