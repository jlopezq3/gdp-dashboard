import streamlit as st


# ---------------------------------------------------------------
# LÓGICA: la misma de su programa (regla de Sarrus, 3x3)
# ---------------------------------------------------------------
def cramer(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):
    restas = -1*(a3 * b2 * c1) - 1*(b3 * c2 * a1) - 1*(c3 * a2 * b1)
    sumas = (a1 * b2 * c3) + (b1 * c2 * a3) + (c1 * a2 * b3)
    determinante = restas + sumas

    restasX = -1*(d3 * b2 * c1) - 1*(b3 * c2 * d1) - 1*(c3 * d2 * b1)
    sumasX = (d1 * b2 * c3) + (b1 * c2 * d3) + (c1 * d2 * b3)
    determinanteX = restasX + sumasX

    restasY = -1*(a3 * d2 * c1) - 1*(d3 * c2 * a1) - 1*(c3 * a2 * d1)
    sumasY = (a1 * d2 * c3) + (d1 * c2 * a3) + (c1 * a2 * d3)
    determinanteY = restasY + sumasY

    restasZ = -1*(a3 * b2 * d1) - 1*(b3 * d2 * a1) - 1*(d3 * a2 * b1)
    sumasZ = (a1 * b2 * d3) + (b1 * d2 * a3) + (d1 * a2 * b3)
    determinanteZ = restasZ + sumasZ

    if determinante == 0:
        return determinante, determinanteX, determinanteY, determinanteZ, None, None, None

    return (determinante, determinanteX, determinanteY, determinanteZ,
            determinanteX / determinante,
            determinanteY / determinante,
            determinanteZ / determinante)


# ---------------------------------------------------------------
# INTERFAZ
# ---------------------------------------------------------------
st.set_page_config(page_title="Regla de Cramer", page_icon="🧮")
st.title("🧮 Regla de Cramer")
st.write("Resuelve un sistema de 3 ecuaciones con 3 incógnitas:  **ax + by + cz = d**")

with st.form("sistema"):
    datos = []  # filas: [a, b, c, d]
    for i in range(3):
        cols = st.columns(4)
        fila = []
        for col, nombre in zip(cols, ("a", "b", "c", "d")):
            fila.append(col.number_input(f"{nombre}{i+1}", value=0.0, step=1.0, key=f"{nombre}{i}"))
        datos.append(fila)
    resolver = st.form_submit_button("Resolver")

if resolver:
    a = [datos[i][0] for i in range(3)]
    b = [datos[i][1] for i in range(3)]
    c = [datos[i][2] for i in range(3)]
    d = [datos[i][3] for i in range(3)]

    det, dx, dy, dz, x, y, z = cramer(*(a + b + c + d))

    st.subheader("Sistema ingresado")
    for i in range(3):
        st.write(f"{datos[i][0]:g}x + {datos[i][1]:g}y + {datos[i][2]:g}z = {datos[i][3]:g}")

    st.subheader("Determinantes")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Δ", f"{det:g}")
    m2.metric("Δx", f"{dx:g}")
    m3.metric("Δy", f"{dy:g}")
    m4.metric("Δz", f"{dz:g}")

    st.subheader("Solución")
    if x is None:
        st.error("Δ = 0: el sistema no tiene solución única.")
    else:
        st.success(f"x = {dx:g} / {det:g} = {x:.4f}")
        st.success(f"y = {dy:g} / {det:g} = {y:.4f}")
        st.success(f"z = {dz:g} / {det:g} = {z:.4f}")
