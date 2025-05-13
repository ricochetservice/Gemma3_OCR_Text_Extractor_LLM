import streamlit as st  # Import the streamlit library for creating web apps
import ollama  # Import the ollama library for AI model interaction
from PIL import Image  # Import the Image class from PIL for image handling
import io  # Import io for file operations
import base64  # Import base64 for encoding the image as base64 string
import os  # Import os for path handling

# Page configuration
st.set_page_config(
    page_title="Gemma-3 OCR",  # Set the page title in the browser tab
    page_icon="🔎",  # Set the page icon in the browser tab
    layout="wide",  # Set the layout to wide for more space
    initial_sidebar_state="expanded"  # Start with the sidebar expanded
)

# Path to the image in the same directory as the script
image_path = os.path.join(os.getcwd(), "gemma3.png")

# Ensure the image exists in the specified location
if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
        st.markdown("""
            # <img src="data:image/png;base64,{}" width="50" style="vertical-align: -12px;"> Gemma-3 OCR
        """.format(base64.b64encode(img_file.read()).decode()), unsafe_allow_html=True)
else:
    st.error("Image 'gemma3.png' not found in the current directory.")

# Add clear button to the top right corner of the page
col1, col2 = st.columns([6, 1])  # Create two columns for layout purposes
with col2:  # Place the clear button in the second column
    if st.button("Clear 🗑️"):  # If the "Clear" button is clicked
        if 'ocr_result' in st.session_state:  # Check if OCR result exists in session state
            del st.session_state['ocr_result']  # Clear the OCR result
        st.rerun()  # Reload the app to reset the state

# Display a brief description of the app
st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Gemma-3 Vision!</p>',
            unsafe_allow_html=True)

# Separator line
st.markdown("---")

# Sidebar section for image upload
with st.sidebar:
    st.header("Upload Image")  # Header for the sidebar
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])  # Image uploader widget

    if uploaded_file is not None:  # If a file is uploaded
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        # Button to trigger text extraction from the image
        if st.button("Extract Text 🔍", type="primary"):
            with st.spinner("Processing image..."):  # Show a spinner while processing
                try:
                    # Send the uploaded image to the Gemma-3 AI model for text extraction
                    response = ollama.chat(
                        model='gemma3:12b',  # Specify the model to use
                        messages=[{
                            'role': 'user',  # The user's message content
                            'content': """Analyze the text in the provided image. Extract all readable content
                                        and present it in a structured Markdown format that is clear, concise, 
                                        and well-organized. Ensure proper formatting (e.g., headings, lists, or
                                        code blocks) as necessary to represent the content effectively.""",
                            'images': [uploaded_file.getvalue()]  # Pass the uploaded image data
                        }]
                    )
                    st.session_state['ocr_result'] = response.message.content  # Save OCR result to session state
                except Exception as e:  # If an error occurs during processing
                    st.error(f"Error processing image: {str(e)}")  # Show error message

# Main content area to display OCR results
if 'ocr_result' in st.session_state:  # If OCR result exists in session state
    st.markdown(st.session_state['ocr_result'])  # Display the OCR result
else:  # If no result is available
    st.info("Upload an image and click 'Extract Text' to see the results here.")  # Show a prompt message

# Footer section with a link to report an issue
st.markdown("---")
st.markdown(
    "Made with ❤️ using Gemma-3 Vision Model | [Report an Issue](https://github.com/SD7Campeon)")
