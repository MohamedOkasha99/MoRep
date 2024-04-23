# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install nltk

# Download NLTK data (stopwords and tokenizer)
RUN python -m nltk.downloader stopwords punkt

# Command to run your Python script
CMD ["python", "text_analysis.py"]