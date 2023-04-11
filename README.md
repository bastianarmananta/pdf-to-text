# pdf-to-text

The outcome of this project is a web application capable of converting PDF files into TXT data. Additionally, the application features a text cleaning functionality based on predetermined patterns. The final result of this project is a clean and easily processable TXT data, which can be subsequently utilized to develop artificial intelligence models.

## Installation

To install and run the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip. You can do this by running the following command in your terminal:
`pip install -r requirements.txt`
3. Run the web app using the following command: `streamlit run app.py`
4. Access the web app by opening your web browser and navigating to `http://localhost:8501`.

## Usage

The application's user interface features a simple and intuitive drag-and-drop functionality that facilitates the conversion of PDF files to TXT data. The subsequent cleaning of the data is also effortless, achieved by a straightforward drag-and-drop process that results in the delivery of clean data.

## Example

Here's an example of how to use the web app:

1. Open your web browser and navigate to `http://localhost:8501`.
2. Drag on drop PDFs data.
3. Click the "Download all data" button.
4. The web app should downloaded converted PDF into TXT data .

## Issues

This project was developed for use in my thesis. Consequently, the predetermined patterns used in the text cleaning process were tailored specifically to my use case. It is important to note that for alternative use cases, different patterns may be required.

## Acknowledgements

This project was built using scikit-learn and Streamlit framework.
