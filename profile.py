import streamlit as st

# Define career options based on education level
def suggest_career(education):
    if education in ["High School", "Diploma"]:
        return ["Explore undergraduate programs", "Consider vocational training", "Look into entry-level positions"]
    elif education in ["Bachelor's Degree"]:
        return ["Pursue a Master's degree", "Apply for jobs in your field of study", "Consider internships"]
    elif education in ["Master's Degree"]:
        return ["Consider a Ph.D. program", "Apply for specialized roles in your field", "Explore teaching opportunities"]
    elif education in ["Ph.D."]:
        return ["Apply for postdoctoral positions", "Consider a career in academia", "Look into research and development roles"]
    else:
        return ["Consider upskilling or reskilling programs"]

# Streamlit App
def main():
    st.title("Student Profile")

    # Input fields
    name = st.text_input("Name:")
    education = st.selectbox("Education Level:", ["High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Ph.D."])
    age = st.number_input("Age:", min_value=0, max_value=100, step=1)

    # Button to submit
    if st.button("Show Career Options"):
        st.subheader(f"Hello, {name}!")
        st.write(f"Based on your education level ({education}) and age ({age}), here are some career options to consider:")

        # Suggest career based on education
        career_options = suggest_career(education)
        for option in career_options:
            st.write(f"- {option}")

if __name__ == "__main__":
    main()
