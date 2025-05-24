import streamlit as st
import google.generativeai as palm

# Configuring API key (consider using environment variables instead)
palm.configure(api_key="AIzaSyAxM5D5fy2eIbpZNbqVBvsrMVjdPLycHYs")

# Defining Model of use
model_name = "models/text-bison-001"  # Updated to current recommended model

# Function to translate code (updated API call)
def translate_code(code_snippet, target_language):
    prompt = f"Translate the following code to {target_language}:\n\n{code_snippet}"
    response = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=0.2,
        max_output_tokens=2000
    )
    return response.result

# Function to explain code (updated API call)
def explain_code(code_snippet):
    prompt = f"Explain the following code:\n\n{code_snippet}"
    response = palm.generate_text(
        model=model_name,
        prompt=prompt,
        temperature=0.3,
        max_output_tokens=1000
    )
    return response.result

# Streamlit application (keeping original structure)
def main():
    st.title("CodeXchange: AI-Powered Code Translation Tool")

    st.markdown("""
    <h2>Project Description</h2>
    <p>CodeXchange is an innovative web application designed to streamline code translation and facilitate seamless collaboration among developers.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Scenario 1: Platform Transition</h2>
    <p>CodeXchange assists developers in transitioning applications from one platform to another. For instance, a team working on an application written in Python can seamlessly translate their code to JavaScript using CodeXchange, enabling smoother cross-platform development and collaboration.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Scenario 2: Mutlilingual Collaboration</h2>
    <p>In a collaborative project where team members use different programming languages, CodeXchange facilitates seamless integration by translating code between languages, ensuring compatibility and efficient collaboration across diverse development environments.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Scenario 3: Code Reusability Across Projects</h2>
    <p>CodeXchange promotes code reusability by enabling developers to translate existing code into different languages for new projects. For example, a developer can take a Python script from a data analysis project and convert it to R for a new project, thereby saving time and effort in rewriting the code from scratch.</p>
    """, unsafe_allow_html=True)

    st.subheader("Code Translation")
    source_code_snippet = st.text_area("Enter the code snippet you want to translate: ")
    target_language = st.selectbox("Select the target programming language:", ["Python","Java","C++"])
    
    if st.button("Translate Code"):
        if source_code_snippet.strip():
            with st.spinner("Translating code..."):
                try:
                    translated_code = translate_code(source_code_snippet, target_language)
                    st.success("Code translation successful!")
                    st.code(translated_code, language=target_language.lower())
                    explanation = explain_code(source_code_snippet)
                    st.markdown(f"**Explanation:** {explanation}")
                    st.download_button(
                        label="Download Translated Code",
                        data=translated_code,
                        file_name=f"translated_code_{target_language.lower()}.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"Error Translating code: {e}")   
        else:
            st.error("Please enter a code snippet.")

if __name__ == "__main__":
    main()
