
import streamlit as st

st.title("🧮 My First Calculator Again")

st.write("For starting calculator press any alphabet or number")

e = st.text_input("Press number/alphabet to start")

if e != "":

    st.write("If you want to exit the calculator press 5")

    # Inputs
    a = st.text_input("Enter your first number")
    b = st.text_input("Enter your second number")

    # Menu
    st.write("1 = plus '+'")
    st.write("2 = Minus '-'")
    st.write("3 = multiply '*'")
    st.write("4 = divide '/'")
    st.write("5 = Exit")

    c = st.text_input("Enter your choice")

    if st.button("Submit"):

        error = False

        # First number validation
        try:
            a = float(a)

        except ValueError:
            st.error("❌ First number should contain numbers only")
            error = True

        # Second number validation
        try:
            b = float(b)

        except ValueError:
            st.error("❌ Second number should contain numbers only")
            error = True

        # Choice validation
        try:
            c = float(c)

        except ValueError:
            st.error("❌ Choice should contain numbers only")
            error = True

        # Run calculator only if no errors
        if error == False:

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
                    st.error("❌ Denominator cannot be zero")

            else:
                st.error("❌ Please choose a choice between 1 - 5")
