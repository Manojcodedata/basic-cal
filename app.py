from helpers import *
import streamlit as st

st.title('Calculator of two number')

#n1 = int(input("Enter the first number :"))
n1 = int(st.number_input("Enter the first number :"))
#n2 = int(input("Enter the Second number :"))
n2 = int(st.number_input("Enter the second number :"))

st.write("Select the operation to do on the two number")
st.write("Type 1 - Multiplication")
st.write("Type 2 - Addition")
st.write("Type 3 - Subtraction")
st.write("Type 4 - Power / exponential")
st.write("Type 5 - divide")
st.write('Type 6 - Floor division')

#operator = int(input("Enter the Option from above :"))
operator = int(st.number_input("Enter the Option from above :"))

if operator == 1:
    st.write(multiply(n1,n2))

elif operator == 2:
    st.write(add(n1,n2))

elif operator == 3:
    st.write(sub(n1,n2))

elif operator == 4:
    st.write(power(n1,n2))

elif operator == 5:
    st.write(divide(n1,n2))

elif operator == 6:
    st.write(floor(n1,n2))

else:
    st.write("Please select vaild Option")

