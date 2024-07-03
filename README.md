# File-Similarity-Comparison-with-Natural-Language-Processing
This Flask web app compares uploaded text against existing files using FlagEmbedding's BGEM3 model, encoding text into dense vectors for fast similarity analysis.

# Text Similarity Comparison Web Application

This web application is built using Flask, a Python web framework, to compare the similarity of textual content uploaded by users against a set of pre-existing files. The core functionality utilizes FlagEmbedding's BGEM3 model for natural language processing, encoding text into dense vectors to facilitate efficient similarity calculations.

## Features

- **File Upload**: Users can upload text files through the web interface.
- **Text Encoding**: Utilizes BGEM3 model to convert text into dense vectors for similarity calculation.
- **Similarity Calculation**: Computes similarity scores between uploaded content and existing files.
- **User Interface**: Provides a user-friendly interface to view similarity results.

## Technologies Used

- **Flask**: Backend web framework for handling HTTP requests and rendering templates.
- **FlagEmbedding**: Natural language processing library for encoding text into vector representations.
- **numpy**: Essential for numerical operations, including vector calculations.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

