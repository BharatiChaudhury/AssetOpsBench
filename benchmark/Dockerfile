FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements files
COPY basic_requirements.txt .
COPY extra_requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r basic_requirements.txt

# Create conda environment (simulating the original setup)
RUN pip install conda-pack
RUN conda create -n assetopsbench python=3.12 -y

# Install additional packages that would be in the extra image
RUN pip install --no-cache-dir \
    jupyter \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    transformers \
    torch \
    langchain \
    termcolor

# Set environment variables
ENV CONDA_DEFAULT_ENV=assetopsbench
ENV PATH="/opt/conda/envs/assetopsbench/bin:$PATH"

# Copy the source code
COPY ../src /app/src

# Set the default command
CMD ["bash"] 