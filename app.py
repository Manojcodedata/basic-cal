from helpers import *
import streamlit as st

st.title('Calculator of two number')

#n1 = int(input("Enter the first number :"))
n1 = int(st.number_input("Enter the first number :"))
#n2 = int(input("Enter the Second number :"))
n2 = int(st.number_input("Enter the second number :"))

operator = st.selectbox("Operation",['Multiply','Add','Subtraction','Divide','Power','Floor division'])

#a = st.button('click')
#st.write(a)

if st.button("Show Result"):

    if operator == 'Multiply':
        st.write(multiply(n1,n2))

    elif operator == 'Add':
        st.write(add(n1,n2))

    elif operator == 'Subtraction':
        st.write(sub(n1,n2))

    elif operator == 'Power':
        st.write(power(n1,n2))

    elif operator == 'Divide':
        st.write(divide(n1,n2))

    elif operator == 'Floor division':
        st.write(floor(n1,n2))

    else:
        st.write("Please select vaild Option")

