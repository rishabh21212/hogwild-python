FROM python:3.12.3

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential autoconf libtool pkg-config && \
    apt-get clean

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Ensure clean environment by creating a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set environment variable to indicate Docker usage
ENV USE_DOCKER=true

# Copy the necessary files
COPY src /hogwild-python/src/
COPY setup.py /hogwild-python/

# Install the package with the specified trusted hosts
RUN cd /hogwild-python/ && pip install -e . --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org
