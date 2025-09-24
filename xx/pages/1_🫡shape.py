import streamlit as st

st.title("claculator area of shapes")
st.write("This is a simple calculator app built with Streamlit.")

shape = st.selectbox("Select a shape", ["Circle", "Square", "Rectangle"])

if shape == "Circle":
    radius = st.number_input("Enter the radius of the circle", min_value=0.0)
    if st.button("Calculate Area"):
        area = 3.14159 * radius * radius
        st.write(f"The area of the circle is {area:.2f}")
elif shape == "Square":
    side = st.number_input("Enter the side length of the square", min_value=0.0)
    if st.button("Calculate Area"):
        area = side * side
        st.write(f"The area of the square is {area:.2f}")
elif shape == "Rectangle":
    length = st.number_input("Enter the length of the rectangle", min_value=0.0)
    width = st.number_input("Enter the width of the rectangle", min_value=0.0)
    if st.button("Calculate Area"):
        area = length * width
        st.write(f"The area of the rectangle is {area:.2f}")


