import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="⭐",
    layout="centered"
)

st.title("Product Review Sentiment Analyzer")
st.write("Enter a product review and get instant sentiment prediction!")

# Input box
review = st.text_area("Enter your product review here", height=150)

# Predict button
if st.button("Analyze Sentiment"):
    if not review.strip():
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            try:
                # Call your Flask backend
                response = requests.post(
                    "https://sentimantal-project-1.onrender.com",
                    json={"reviews": review}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    # Fixed: Use 'predictions' to match Flask, and 'response' with an 's'
                    sentiment = result.get('predictions', 'unknown')

                    if "positive" in sentiment:
                        st.success(f"Sentiment: {sentiment}")
                    else:
                        st.error(f"Sentiment: {sentiment}")
                else:
                    st.error(f"Server error: Received status code {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the Flask server. Make sure it is running!")
                
