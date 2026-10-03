
# AI Food Recognition & Calorie Estimation — CEP Project

## How to run
1. Install Python 3.10+.
2. Open Command Prompt in this folder.
3. Run: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`
5. Open the local URL shown by Streamlit.

## Important
This is a college-friendly prototype. The interface accepts a food image and uses a food/calorie reference table after the user confirms the detected category. For a production version, replace the confirmation step with a trained Food-101 image classification model.

## Formula
Estimated calories = (kcal per 100 g × serving size in g) / 100

Example:
Rice = 130 kcal/100 g
Serving = 150 g
Calories = 130 × 150 / 100 = 195 kcal
