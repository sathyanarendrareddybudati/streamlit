import streamlit as st

def main():

    page_index = st.session_state.get("page_index", 0)

    if page_index == 0:
        enter_title_and_text()
    elif page_index == 1:
        interactive_gaps_adder()
    elif page_index == 2:
        settings_and_preview()

def enter_title_and_text():
    st.write("ENTER TITLE AND TEXT")

    title_and_instructions = st.text_area("Enter the title and instructions (optional):")

    questions = st.text_area("Enter a test or a list of questions:")

    question_list = questions.split('\n')

    st.session_state["title_and_instructions"] = title_and_instructions
    st.session_state["questions"] = question_list

    if st.button("Next Page"):
        st.session_state["page_index"] = 1


def interactive_gaps_adder():
    st.write("INTERACTIVE GAPS ADDER")
    st.write("Click on the words to make them gaps")

    if st.button("Previous Page"):
        st.session_state["page_index"] = 0
    elif st.button("Next Page"):
        st.session_state["page_index"] = 2


def settings_and_preview():
    question_list = st.session_state.get("question_list", [])
    st.write("SETTINGS AND PREVIEW")

    gap_options = st.checkbox("Show only first letter", value=False)
    student_name = st.text_input("Student Name:")
    date = st.text_input("Date:")

    
    st.markdown(
        "Copyright © John's ESL Community: Gap Fill Generator FREE at: "
        "[http://www.johnsesl.com](http://www.johnsesl.com)"
    )

    preview_question_list = apply_gap_options(question_list, gap_options)

    if st.button("Previous Page"):
        st.session_state["page_index"] = 1
    elif st.button("Print"):
       
        title_and_instructions = st.session_state.get("title_and_instructions", "")
        questions = st.session_state.get("questions", [])
        print_result(preview_question_list, student_name, date, title_and_instructions, questions)


def apply_gap_options(question_list, show_only_first_letter):
    
    modified_questions = []
    for question in question_list:
        if show_only_first_letter:
            modified_question = " ".join([word[0] if word.isalpha() else word for word in question.split()])
        else:
            modified_question = question
        modified_questions.append(modified_question)
    return modified_questions

def preview_and_print(question_list, student_name, date):
 
    st.write("Preview:")
    for i, question in enumerate(question_list):
        st.write(f"Question {i + 1}:")
        st.markdown(question, unsafe_allow_html=True)

    st.write("Student Name:", student_name)
    st.write("Date:", date)

def print_result(question_list, student_name, date, title, instructions):

    printable_content = f"{title}\n\n\n"
    printable_content += "Student Name: {}\nDate: {}\n\n\n".format(student_name, date)
    printable_content += f"{instructions}"
    printable_content += "\n".join(question_list)

    st.text_area("Printable Version", value=printable_content)


if __name__ == "__main__":
    main()
