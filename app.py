
import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Food Recognition & Calorie Estimation", page_icon="🍱")

CALORIES = {
    "apple": 52, "banana": 89, "rice": 130, "pizza": 266,
    "burger": 295, "sandwich": 250, "chapati": 297, "roti": 297,
    "dal": 116, "dosa": 168, "idli": 58, "samosa": 262,
    "poha": 130, "upma": 209, "salad": 33, "orange": 47,
    "egg": 155, "chicken": 239, "paneer": 265, "potato": 77
}

st.title("🍱 AI Food Recognition & Calorie Estimation")
st.write("Upload a food image to estimate its food category and calories.")

uploaded = st.file_uploader("Upload food image", type=["jpg","jpeg","png"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded Food Image", use_container_width=True)

    st.info(
        "Demo version: choose the detected food below. "
        "For a full AI model, connect a trained Food-101/food image classifier."
    )
    food = st.selectbox("Select/confirm detected food", list(CALORIES.keys()))
    grams = st.number_input("Estimated serving size (grams)", min_value=1, value=100)

    kcal_per_100g = CALORIES[food]
    estimated = kcal_per_100g * grams / 100

    st.success(f"Food: {food.title()}")
    st.metric("Estimated Calories", f"{estimated:.0f} kcal")
    st.caption(f"Reference value: approximately {kcal_per_100g} kcal per 100 g.")

st.markdown("---")
st.caption("CEP Project: AI Food Recognition & Calorie Estimation")
