import os.path

from streamlit_components import *

def main():
    st.image(os.path.join("image_procssing.jpg"), use_column_width= True)
    st.header("     ...Well Come to Image Processing Method..    ")

    st.sidebar.title("Image Processing using openCV")
    function_selected = st.sidebar.selectbox("Choose OpenCV function",
                                             ["Image Thresholding",
                                              "Morphological Transformations",
                                              "Canny Edge Detection",
                                              "Face Detection"])

    if function_selected == "Image Thresholding":
        image_thresholding()
    elif function_selected == "Morphological Transformations":
        morphological_transformation()
    elif function_selected == "Canny Edge Detection":
        canny()
    elif function_selected == "Face Detection":
        face_detection()
    else:
        st.write("Choose right option")


if __name__ == "__main__":
    main()