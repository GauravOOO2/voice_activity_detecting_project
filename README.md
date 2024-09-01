# Voice Activity Detection (VAD) Web Application

## Overview

This project is a web application that allows users to upload audio files and detect periods of silence within the audio. It leverages a React frontend and a Flask backend to handle file uploads, process audio, and return results indicating timestamps where silence is detected.

## Tech Stack

- **Frontend**: 
  - **React**: A JavaScript library for building user interfaces.
  - **Tailwind CSS**: A utility-first CSS framework for styling.
  - **Axios**: A promise-based HTTP client for making requests.

- **Backend**:
  - **Flask**: A lightweight Python web framework for building APIs.
  - **pydub**: A Python library for audio processing.
  - **ffmpeg**: A multimedia framework used by `pydub` for audio manipulation.
  - **flask_cors**: A Flask extension for handling CORS (Cross-Origin Resource Sharing).

## Features

- **Audio Upload**: Users can upload audio files via a file input field.
- **Silence Detection**: The backend analyzes the audio to detect periods of silence.
- **Results Display**: The frontend displays timestamps where silence is detected.
- **User-Friendly Interface**: Styled using Tailwind CSS for a responsive and clean design.

## How It Works

1. **Frontend**:
   - Users select an audio file using the file input.
   - The selected file is sent to the backend as a `multipart/form-data` request.
   - The backend processes the audio file and detects silence periods.
   - Results are returned to the frontend and displayed to the user.

2. **Backend**:
   - The backend receives the uploaded audio file and saves it to a specified directory.
   - The audio file is then processed using `pydub` to detect periods of silence.
   - The silence detection algorithm identifies timestamps where the audio is silent based on a specified threshold and minimum silence length.
   - The results are sent back to the frontend as a JSON response.

## Setup and Installation

### Prerequisites

- **Python 3.6+**: Ensure Python is installed on your system.
- **Node.js**: Required for running the React frontend.

### Backend Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/GauravOOO2/voice_activity_detecting_project_Backend.git
   ```

2. **Navigate to backend**
```bash
cd voice_activity_detecting_project_backend/backend
```

3. **Create and Activate a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install Backend Dependencies:**

```bash
pip install -r requirements.txt
```

5. **Create an env file**

```bash
FLASK_ENV=development
UPLOAD_FOLDER=./uploads
```

6. **Run Backend**

```bash
py app.py
```

