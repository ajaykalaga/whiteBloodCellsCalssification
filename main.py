import streamlit as st


def main():
    st.title("file Upload Tutorial")
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])


if __name__ == '__main__':
    main()
