import streamlit as st

def main():

    # Get the current page from session state, default to 0 if not set
    page_index = st.session_state.get("page_index", 0)

    if page_index == 0:
        # Page 1: ENTER TITLE AND TEXT
        enter_title_and_text()
    elif page_index == 1:
        # Page 2: INTERACTIVE GAPS ADDER
        interactive_gaps_adder()
    elif page_index == 2:
        # Page 3: SETTINGS AND PREVIEW
        settings_and_preview()

def enter_title_and_text():
    st.write("ENTER TITLE AND TEXT")

    # Create input fields for the title and instructions
    title_and_instructions = st.text_area("Enter the title and instructions (optional):")

    # Create input fields for the list of questions
    questions = st.text_area("Enter a test or a list of questions:")

    # Split questions into a list
    question_list = questions.split('\n')

    # Set the title_and_instructions and questions in session state
    st.session_state["title_and_instructions"] = title_and_instructions
    st.session_state["questions"] = question_list

    # Custom pagination bar
    if st.button("Next Page"):
        # Move to the next page
        st.session_state["page_index"] = 1


def interactive_gaps_adder():
    st.write("INTERACTIVE GAPS ADDER")
    st.write("Click on the words to make them gaps")

    # Custom pagination bar
    if st.button("Previous Page"):
        # Move back to the previous page
        st.session_state["page_index"] = 0
    elif st.button("Next Page"):
        # Move to the next page
        st.session_state["page_index"] = 2


def settings_and_preview():
    question_list = st.session_state.get("question_list", [])
    st.write("SETTINGS AND PREVIEW")

    # Create input fields for settings
    gap_options = st.checkbox("Show only first letter", value=False)
    student_name = st.text_input("Student Name:")
    date = st.text_input("Date:")

    # Copyright notice
    st.markdown(
        "Copyright © John's ESL Community: Gap Fill Generator FREE at: "
        "[http://www.johnsesl.com](http://www.johnsesl.com)"
    )

    # Preview the result
    preview_question_list = apply_gap_options(question_list, gap_options)

    # Custom pagination bar
    if st.button("Previous Page"):
        # Move back to the previous page
        st.session_state["page_index"] = 1
    elif st.button("Print"):
        # Print the result on the last page
        title_and_instructions = st.session_state.get("title_and_instructions", "")
        questions = st.session_state.get("questions", [])
        print_result(preview_question_list, student_name, date, title_and_instructions, questions)


def apply_gap_options(question_list, show_only_first_letter):
    # Implement logic to apply gap word options
    # For simplicity, we will just show the first letter if the option is selected
    modified_questions = []
    for question in question_list:
        if show_only_first_letter:
            modified_question = " ".join([word[0] if word.isalpha() else word for word in question.split()])
        else:
            modified_question = question
        modified_questions.append(modified_question)
    return modified_questions

def preview_and_print(question_list, student_name, date):
    # Implement logic to preview and print the final result with student name and date
    st.write("Preview:")
    for i, question in enumerate(question_list):
        st.write(f"Question {i + 1}:")
        st.markdown(question, unsafe_allow_html=True)

    st.write("Student Name:", student_name)
    st.write("Date:", date)

def print_result(question_list, student_name, date, title, instructions):
    # Implement logic to print the final result
    # Include title and instructions at the top center
    printable_content = f"{title}\n\n\n"
    printable_content += "Student Name: {}\nDate: {}\n\n\n".format(student_name, date)
    printable_content += f"{instructions}"
    printable_content += "\n".join(question_list)

    st.text_area("Printable Version", value=printable_content)


if __name__ == "__main__":
    main()


st.markdown("---")

if st.session_state.get("page_index", 0) == 0:
    st.write("➡️ Move to Page 2")
elif st.session_state.get("page_index", 0) == 1:
    st.write("⬅️ Go Back to Page 1")
    st.write("➡️ Move to Page 3")
else:
    st.write("⬅️ Go Back to Page 2")