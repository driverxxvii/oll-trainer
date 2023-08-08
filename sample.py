import random
import streamlit as st


def oll_scrambles():
    scrambles = {
        1: "L  F'  L'  U2  B  L  F'  L  F2  L2  B'  U",
        2: "U  R  B  U  F'  L'  B  L  B2  F  U'  R'",
        3: "R'  U'  R  B  U  B  D  F'  L  F  D'  B2",
        4: "F'  U'  L'  U  L  F  R'  F'  U'  F  U  R",
        5: "D  U  L  U  L2  B  L  B2  U  B  D'  U",
    }

    return scrambles


def st_lit():
    selected = oll_checkboxes()
    display_scramble(selected)
    next_scramble()


def oll_checkboxes():
    """
    Draws the checkboxes and returns the selected checkboxes as a list
    """
    st.subheader("Select OLL's")

    cols = st.columns(5)
    checkbox_values = [False] * 5
    for i in range(5):
        checkbox_values[i] = cols[i].checkbox(f"{i+1}", key=i+1)

    # get a list of the checked checkboxes
    selected = [i + 1 for i, value in enumerate(checkbox_values) if value]
    return selected


def display_scramble(selected_olls):
    scrambles = oll_scrambles()
    if selected_olls:       # True if list is not empty (i.e. at least one checkbox is checked)
        key = random.choice(selected_olls)
        st.title(f"OLL - {key}")
        st.title(scrambles[key])
    else:
        st.write("No OLL's selected")


def next_scramble():
    st.button("Next Scramble")


def main():
    st_lit()


if __name__ == "__main__":
    main()
