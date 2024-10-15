import streamlit as st
import numpy as np

def convert_to_number(num_str):
    try:
        # Try converting the string to an integer
        num = int(num_str)
    except ValueError:
        # If conversion fails, convert to a large integer using numpy
        num = np.frombuffer(num_str.encode(), dtype=np.uint8).sum()
    return num

def add_until_single_digit(num):
    # Keep adding until the sum becomes a single digit
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def main():
    st.title("Final Single Digit Number")
    
    # number = st.number_input("Enter a number:", min_value=0, step=1, key="input_number")
    number = st.text_input("Enter a number:", max_chars=64, key="numberInput")
    result = add_until_single_digit(convert_to_number(number))
    st.markdown(f"<h1 style='text-align: center;'>{result}</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

