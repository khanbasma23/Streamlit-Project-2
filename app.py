import streamlit as st # type: ignore
from forex_python.converter import CurrencyRates # type: ignore


#Dark mode css
dark_mode = """ 
<style>
body {
background-color: #121212;
color:white;
}
.stTextInput, .stNumberInput, .stSelectBox {
background-color: #333;
color: white;
}
</style>
"""
st.markdown(dark_mode, unsafe_allow_html=True)

#Conversation Function
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "cm to inch": 0.393701,
        "inch to cm": 2.54,
        "m to feet": 3.28084,
        'km to miles': 0.621371,
        "miles to km": 1.60934
    }

    key = f"{from_unit} to {to_unit}"
    if key in conversion_factors:
        return round(value * conversion_factors[key], 4)
    else:
        return "Conversion not available"
    
    # streamlit ui
    st.title("Unit Converter")

    value = st.number_input("Enter value:" , min_value=0.0, step=0.1)
    from_unit = st.selectbox("From Unit", ["cm", "inch", "m", "feet","km", "miles"])
    to_unit = st.selectbox("To Unit",["cm", "inch", "m", "feet","km", "miles"])

    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"Converted Value:{result}")

    
# Currency Converter Function
def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        result = c.convert(from_currency, to_currency, amount)
        return round(result, 2)
    except:
        return "Invalid Currency Code"

#  Streamlit UI for Currency Converter
st.header("Currency Converter")
amount = st.number_input("Enter amount:", min_value=0.0, step=0.1)
from_currency = st.text_input("From Currency (e.g., USD)")
to_currency = st.text_input("To Currency (e.g., INR)")

if amount and from_currency and to_currency:
    currency_result = convert_currency(amount, from_currency, to_currency)
    st.success(f"Converted Amount: {currency_result}")

#  Temperature Converter Function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid Conversion"

#  Streamlit UI for Temperature Converter
st.header("Temperature Converter")
temp_value = st.number_input("Enter temperature value:")
temp_from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
temp_to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

if temp_value and temp_from_unit and temp_to_unit:
    temp_result = convert_temperature(temp_value, temp_from_unit, temp_to_unit)
    st.success(f"Converted Temperature: {temp_result}")
    

