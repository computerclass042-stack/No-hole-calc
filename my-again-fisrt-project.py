

import streamlit as st

# Title
st.title("🧮 My First Calculator Again")

# Starting Message
st.write("For starting calculator press any alphabet or number")

# Start Input
start = st.text_input("Press number/alphabet to start")

# Run only if something entered
if start != "":

    st.write("If you want to exit the calculator press 5")

    # Number Inputs
    first = st.text_input("Enter your first number")

    second = st.text_input("Enter your second number")

    # Choices
    st.write("1 = plus '+'")
    st.write("2 = Minus '-'")
    st.write("3 = multiply '*'")
    st.write("4 = divide '/'")
    st.write("5 = Exit")

    choice = st.text_input("Enter your choice")

    # Submit Button
    if st.button("Submit"):

        valid = True

        # First Number Validation
        try:
            first = float(first)

        except ValueError:
            st.error("❌ Please enter numbers only in First Number")
            valid = False

        # Second Number Validation
        try:
            second = float(second)

        except ValueError:
            st.error("❌ Please enter numbers only in Second Number")
            valid = False

        # Choice Validation
        try:
            choice = int(choice)

        except ValueError:
            st.error("❌ Choice should contain numbers only")
            valid = False

        # Run Calculator only if all inputs are valid
        if valid:

            # Exit
            if choice == 5:
                st.warning("Calculator Closed")
                st.info("Thanks for using our calculator ❤️")

            # Addition
            elif choice == 1:
                answer = first + second
                st.success(f"Your answer is = {answer}")

            # Subtraction
            elif choice == 2:
                answer = first - second
                st.success(f"Your answer is = {answer}")

            # Multiplication
            elif choice == 3:
                answer = first * second
                st.success(f"Your answer is = {answer}")

            # Division
            elif choice == 4:

                if second == 0:
                    st.error("❌ Denominator cannot be zero")

                else:
                    answer = first / second
                    st.success(f"Your answer is = {answer}")

            # Invalid Choice
            else:
                st.error("❌ Please choose between 1 to 5")
