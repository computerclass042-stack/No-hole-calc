```python
import streamlit as st

st.title("🧮 My First Calculator Again")

st.write("For starting calculator press any alphabet or number")

# Start input
e = st.text_input("Press number/alphabet to start")

if e != "":

    st.write("If you want to exit the calculator press 5")

    # First number
    a = st.text_input("Enter your first number")

    # Second number
    b = st.text_input("Enter your second number")

    # Choice
    st.write("1 = plus '+'")
    st.write("2 = Minus '-'")
    st.write("3 = multiply '*'")
    st.write("4 = divide '/'")
    st.write("5 = Exit")

    c = st.text_input("Enter your choice")

    # Button
    if st.button("Submit"):

        try:
            # Convert numbers
            a = float(a)
            b = float(b)

            # Convert choice
            c = float(c)

            if c == 5:
                st.warning("Calculator closed")

            elif c == 1:
                q = a + b
                st.success(f"Your answer is = {q}")

            elif c == 2:
                q = a - b
                st.success(f"Your answer is = {q}")

            elif c == 3:
                q = a * b
                st.success(f"Your answer is = {q}")

            elif c == 4:

                if b != 0:
                    q = a / b
                    st.success(f"Your answer is = {q}")

                else:
                    st.error("Denominator cannot be zero")

            else:
                st.error("Please choose a choice between 1 - 5")

        except ValueError:
            st.error("Please choose only number not alphabets")
```
