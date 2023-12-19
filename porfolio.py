import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Enrique's Web Page", page_icon="./dev.png")
    
    st.title("Enrique's Web Page")

    # Header
    st.image("./dev.jpeg", caption="Imagen de cabecera", use_column_width=True)
    st.write("¡Bienvenido a mi blog personal!")

    # About Me
    st.header("Sobre mí")
    about_text = """
    Tengo experiencia en tecnologías como **Django**, **HTML**, **CSS**, **Git**, **SQL**, **Linux**, **Pandas**, **Numpy**, **Machine Learning** y **Deep Learning**. 
    Me especializo en la construcción y mantenimiento de sistemas escalables de alto rendimiento y estoy siempre en busca de maneras de mejorar mis habilidades y conocimientos.
    """
    st.markdown(about_text)

    # Education & Career
    st.header("Educación y Experiencia Laboral")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Educación")
        st.write("- Master of Engineering in Information Technology and Communications, Autonomous University of Guadalajara, SEP OF 2020 - SEP OF 2022 (GPA 4.0)")
        st.write("- Engineer in Communications and Electronics, Military School of Engineers, SEP OF 2012 - SEP OF 2018 (GPA 3.7)")

    with col2:
        st.subheader("Experiencia Laboral")
        st.write("- Sr. Backend Developer, SDN, 2018 - Actualidad")

    # Lenguajes y Tecnologías
    st.header("Lenguajes y Tecnologías que Manejo")

    lenguajes_tecnologias = {
        'Python': 50,
        'PostgreSQL': 20,
        'AWS': 15,
        'Pandas': 25,
        # Agrega otros lenguajes y tecnologías con sus porcentajes aquí
    }

    fig, ax = plt.subplots()
    ax.pie(lenguajes_tecnologias.values(), labels=lenguajes_tecnologias.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title('Lenguajes y Tecnologías')
    st.pyplot(fig)

    # Contacto
    st.header("Contacto")
    with st.expander("Información de Contacto"):
        st.write("¡Si quieres ponerte en contacto conmigo, puedes hacerlo a través de:")
        st.write("- Correo electrónico: backup202dos@gmail.com")
        st.write("- LinkedIn: [Mi perfil de LinkedIn](https://www.linkedin.com/in/h3nr7sr/)")

if __name__ == "__main__":
    main()
