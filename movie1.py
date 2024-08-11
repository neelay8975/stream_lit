import streamlit as st

# Sample database of movies and web series categorized by genres
media_database = {
    "Horror": ["The Conjuring", "Stranger Things", "The Haunting of Hill House", "Hereditary", "A Quiet Place"],
    "Romantic": ["The Notebook", "Pride and Prejudice", "La La Land", "Outlander", "To All the Boys I've Loved Before"],
    "Suspense": ["Inception", "Sherlock", "Gone Girl", "Dark", "Prisoners"],
    "Thriller": ["Breaking Bad", "Se7en", "Zodiac", "Shutter Island", "The Girl with the Dragon Tattoo"],
    "Comedy": ["Friends", "The Office", "Brooklyn Nine-Nine", "The Big Bang Theory", "Parks and Recreation"],
    "Drama": ["The Crown", "The Godfather", "The Sopranos", "Schindler's List", "12 Years a Slave"]
}

# Function to suggest media based on the selected genre
def suggest_media(media_type):
    return media_database.get(media_type, ["No recommendations available for this genre."])

# Streamlit App
def main():
    st.title("Media and Entertainment Recommendations")

    # Instruction to the user
    st.write("Select the type of entertainment you're interested in, and get recommendations for movies and web series.")

    # Dropdown for selecting the type of entertainment
    media_type = st.selectbox("Type of Entertainment:", list(media_database.keys()))

    # Button to submit and get recommendations
    if st.button("Show Recommendations"):
        st.subheader(f"Recommendations for {media_type}:")
        
        # Fetch and display recommendations based on selected genre
        recommendations = suggest_media(media_type)
        for rec in recommendations:
            st.write(f"- {rec}")

if __name__ == "__main__":
    main()
