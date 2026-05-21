# My first calculator again
```python
import streamlit as st

st.title("🧮 Simple Calculator")

# Number Inputs
a = st.number_input("Enter first number")

b = st.number_input("Enter second number")

# Operation Choice
operation = st.selectbox(
    "Choose operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Button
if st.button("Calculate"):

    if operation == "Addition":
        st.success(f"Answer = {a + b}")

    elif operation == "Subtraction":
        st.success(f"Answer = {a - b}")

    elif operation == "Multiplication":
        st.success(f"Answer = {a * b}")

    elif operation == "Division":

        if b == 0:
            st.error("Cannot divide by zero")

        else:
            st.success(f"Answer = {a / b}")
```
