import random
import os
import pathlib
import collections
import streamlit as st


def oll_scrambles():
    scrambles = {
        1: "L  F'  L'  U2  B  L  F'  L  F2  L2  B'  U",
        2: "U  R  B  U  F'  L'  B  L  B2  F  U'  R'",
        3: "R'  U'  R  B  U  B  D  F'  L  F  D'  B2",
        4: "F'  U'  L'  U  L  F  R'  F'  U'  F  U  R",
        5: "D  U  L  U  L2  B  L  B2  U  B  D'  U",
        6: "U2  L  F  U'  R  U  R'  U  F'  U'  L'  U'",
        7: "D  B'  U'  B  L  F  U2  F'  U'  L'  D'  U'",
        8: "U  L  R2  F2  R  F2  L'  R2  B'  R'  B  U",
        9: "R'  L  D  F  D'  R  L'  U  F  U2  F'  U2",
        10: "L  F2  L'  U  F'  U'  L  D  F  D'  L'  F",
        11: "R  B2  U  L'  B'  L  B  L  U'  L'  B2  R'",
        12: "F'  U'  R  B2  D  L'  D'  B2  R'  U2  F  U'",
        13: "F'  U'  L'  U  L2  F2  L'  U2  L'  U2  L  F'",
        14: "R  U  R'  B'  U2  F'  U'  F  R  U2  R'  B",
        15: "U2  R  U2  R'  U'  F'  L'  B'  U'  B  L  F",
        16: "R'  F2  L  D'  F'  D  F  L'  F2  R2  U'  R'",
        17: "U'  F'  R  U2  L'  B  U2  B'  L  U2  R'  F",
        18: "R'  U2  R  B  L  F  U  F'  U  L'  B'  U'",
        19: "R'  F'  U2  F2  U  R  U'  R'  F'  U2  R  U",
        20: "R  L  B  D2  R2  U2  R2  D2  L2  B'  R'  L'",
        21: "F  U  R'  D  R2  U'  R2  D'  R  F2  U2  F",
        22: "U'  B'  U2  B  F'  U  L2  U  L2  U'  L2  F",
        23: "R2  F  U2  F  D'  F'  U2  F  D  F2  R2  U2",
        24: "R  D  L2  D'  R  D'  U2  R2  D'  L2  D2  U2",
        25: "L'  D2  L'  D2  L  U'  L'  D2  L  D2  U  L",
        26: "B  F'  L  B  L'  F'  L  B'  L'  B'  F2  U2",
        27: "F  D'  F2  D'  B2  D'  U2  B2  D'  F2  U2  F'",
        28: "U'  B'  R'  B'  R  B'  D2  F  L'  F'  D2  B'",
        29: "B'  L  U  F  U2  F'  U  L'  B'  U  B2  U'",
        30: "U'  R'  F  R  U2  F'  U'  F'  U  F2  U2  F'",
        31: "U2  L  B'  L'  U  R'  U  R  U'  L  B  L'",
        32: "F  U'  F'  U2  F  U  R  U'  R'  U'  F'  U'",
        33: "F'  U  L  F  R  U'  R'  U  F'  L'  F  U'",
        34: "R  U'  B'  R2  F'  R'  B  R'  U'  R2  F  R",
        35: "L'  U2  L  F'  L  F'  R'  L'  F2  R2  U2  R'",
        36: "U2  R  U  R'  U  R  U2  B  U  B'  U'  R'",
        37: "D  U'  R  B  R  U  R'  B'  R  U'  R2  D'",
        38: "B'  R'  U'  F'  R  B  R'  F  R  B'  U  B",
        39: "D  L  U2  L'  U'  B'  U'  R'  U'  R  B  D'",
        40: "U  F  B'  U  R  U'  R'  U'  B  U  F'  U2",
        41: "B  U2  B'  R  B2  R  F  R'  B2  R2  F'  R",
        42: "U  F  B2  D'  R  D  F'  B2  L  U'  L'  U'",
        43: "D  U  B'  R'  U  F'  U'  F  R  B  D'  U2",
        44: "U  R'  U2  R2  B'  R'  B'  L'  B'  L  B'  U'",
        45: "U  F'  U'  L'  R  B  L'  B'  L2  R'  U  F",
        46: "R  U  R'  U'  R'  U'  F  U  R  U'  F'  U'",
        47: "U'  B'  U'  R'  U  R  U'  R'  U  R  B  U2",
        48: "U2  F  R2  B2  R  F'  R2  B2  L  U2  L'  R'",
        49: "R'  U2  B  L2  F  L2  B  L'  R  D2  B2  L",
        50: "L  F  R  U2  R'  U  F'  L  F'  L'  F  L'",
        51: "R'  U2  R2  B  R'  U'  B  L  U  L'  B2  U",
        52: "F'  U'  F2  R'  F'  R2  U'  B  U  B'  U'  R'",
        53: "F'  U'  F2  R'  F2  U'  F  R2  U'  R2  U2  R",
        54: "R  U  F'  U2  F  R2  B'  R2  B2  U'  B'  R'",
        55: "U'  B  L'  B'  R  B  L2  U'  L'  U  B'  R'",
        56: "R  F'  U'  L'  U  F  R2  F'  L  F  R  U",
        57: "U2  F2  L  F  L'  F  R  U  R'  F'  U'  F",

    }
    return scrambles


def st_lit():
    selected = select_olls()
    display_scramble(selected)
    next_scramble()


def select_olls():
    """
    Draws the checkboxes and returns the selected checkboxes as a list
    """
    st.subheader("Select OLLs")

    cols = st.columns(10)

    checkbox_values = [False] * 57
    for row_num in range(0, 5):
        for i in range(1, 11):
            # 10*row_num + i will number the checkboxes from 1 to 50
            checkbox_values[10*row_num + i - 1] = cols[i-1].checkbox(f"{10 * row_num + i}", key=10 * row_num + i)

    # Create 7 additional checkboxes numbered 51 to 57
    for i in range(51, 58):
        checkbox_values[i-1] = cols[i-51].checkbox(f"{i}", key=i)

    selected = [i + 1 for i, value in enumerate(checkbox_values) if value]
    return selected


def display_scramble(selected_olls):
    st.toast(selected_olls)
    scrambles = oll_scrambles()
    key = random.choice(selected_olls)
    st.title(key)
    st.title(scrambles[key])


def next_scramble():
    st.button("Next Scramble")


def main():
    st_lit()


if __name__ == "__main__":
    main()
