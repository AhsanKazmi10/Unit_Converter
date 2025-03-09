import streamlit as st

# Custom CSS for styling
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSelectbox div {
        font-size: 16px;
    }
    .stNumberInput input {
        font-size: 16px;
    }
    .stSuccess {
        font-size: 18px;
        color: #4CAF50;
    }
    .title {
        font-size: 30px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .icon {
        font-size: 24px;
        margin-right: 10px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #777;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🛠️ Settings")
    theme = st.selectbox("Select Theme", ["Light", "Dark"])
    st.markdown("---")
    st.markdown("### 📊 About")
    st.markdown("This app helps you convert units easily!")
    st.markdown("---")
    st.markdown("### 🔗 Links")
    st.markdown("[GitHub Repository](https://github.com/AhsanKazmi10)")
    st.markdown("[Streamlit Documentation](https://docs.streamlit.io)")

# Title with Icon
st.markdown('<p class="title">📏 Unit Converter</p>', unsafe_allow_html=True)

# Unit Conversion
conversion_type = ['Length', 'Weight', 'Temperature']
# User selects conversion type
conversion_choice = st.selectbox("Choose the conversion type:", conversion_type)

# Length Conversion
if conversion_choice == "Length":
    st.markdown('<p class="icon">📏</p>', unsafe_allow_html=True)
    Length_Units = ['Meters', 'Kilometers', 'Foot', 'Inch', 'Centimeters']
    input_value = st.number_input("Enter length value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit", Length_Units)
    to_unit = st.selectbox("To unit", Length_Units)

    # Conversion dictionary
    length_Conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Centimeters": 0.01
    }

    # Conversion Formula
    if st.button("Convert"):
        result = input_value * (length_Conversion[from_unit] / length_Conversion[to_unit])
        st.success(f"🎉 {input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# Weight Conversion
elif conversion_choice == "Weight":
    st.markdown('<p class="icon">⚖️</p>', unsafe_allow_html=True)
    Weight_Units = ['Kilograms', 'Grams', 'Pounds', 'Ounces']
    input_value = st.number_input("Enter weight value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit", Weight_Units)
    to_unit = st.selectbox("To unit", Weight_Units)

    # Conversion dictionary
    weight_Conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    # Conversion Formula
    if st.button("Convert"):
        result = input_value * (weight_Conversion[from_unit] / weight_Conversion[to_unit])
        st.success(f"🎉 {input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# Temperature Conversion
elif conversion_choice == "Temperature":
    st.markdown('<p class="icon">🌡️</p>', unsafe_allow_html=True)
    Temperature_Units = ['Celsius', 'Fahrenheit', 'Kelvin']
    input_value = st.number_input("Enter Temperature value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit", Temperature_Units)
    to_unit = st.selectbox("To unit", Temperature_Units)

    # Conversion Formula
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value

    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"🎉 {input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown(
    '<p class="footer">🚀 Made by Syed Ahsan | © 2025 All Rights Reserved</p>',
    unsafe_allow_html=True
)