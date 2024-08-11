import streamlit as st

# Sample database of movies and web series
media_database = {
    "Horror": ["The Conjuring", "Stranger Things", "The Haunting of Hill House", "Hereditary"],
    "Romantic": ["The Notebook", "Pride and Prejudice", "La La Land", "Outlander"],
    "Suspense": ["Inception", "Sherlock", "Gone Girl", "Dark"],
    "Thriller": ["Breaking Bad", "Se7en", "Zodiac", "Shutter Island"],
    "Comedy": ["Friends", "The Office", "Brooklyn Nine-Nine", "The Big Bang Theory"],
    "Drama": ["The Crown", "The Godfather", "The Sopranos", "Schindler's List"]
}

# Function to suggest media based on type
def suggest_media(media_type):
    return media_database.get(media_type, ["No recommendations available for this genre."])

# Streamlit App
def main():
    st.title("Media and Entertainment Recommendations")

    # Input fields
    st.write("Enter the name of a movie or web series you like:")
    media_name = st.text_input("Movie or Web Series Name:")

    st.write("Select the type of entertainment you're interested in:")
    media_type = st.selectbox("Type of Entertainment:", list(media_database.keys()))

    # Button to submit
    if st.button("Show Recommendations"):
        st.subheader(f"Recommendations based on your interest in {media_type}:")

        # Suggest media based on type
        recommendations = suggest_media(media_type)
        for rec in recommendations:
            st.write(f"- {rec}")

if __name__ == "__main__":
    main()
