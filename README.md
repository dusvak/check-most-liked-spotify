# Spotify Liked Songs Analyzer

A web application built with Python and Flask that allows users to analyze their Spotify 'Liked Songs' library, identifying top artists and genres, and visualizing these insights.

This project was developed as a portfolio item to demonstrate a set of back-end, data-visualization and web development skills, including:
- Consumption of REST APIs (Spotify Web API) and handling OAuth 2.0 authentication flows
- Building web applications with the Flask framework
- Template rendering with Jinja2
- Data processing and analysis in Python (e.g., frequency counting)
- Data visualization using Matplotlib and Seaborn
- Modular code design and environment management

## Features

*   **Secure Spotify Authentication:** Utilizes Spotify's OAuth 2.0 Authorization Code Flow for secure user login and data access.
*   **Liked Songs Retrieval:** Fetches all saved tracks from the user's Spotify library.
*   **Top Artists Analysis:** Identifies and ranks the most frequently appearing artists in the user's liked songs.
*   **Top Genres Analysis:** Determines and ranks the most common music genres associated with the artists in the user's liked songs, requiring additional API calls for artist genre data.
*   **Interactive Web Interface:** A simple Flask web application provides a user-friendly interface to connect with Spotify and view the analysis results.
*   **Data Visualization:** Presents the top artists and genres as professional-looking bar charts generated using Matplotlib and Seaborn, embedded directly into the web page.

## Live Demo

*   (Coming Soon) - A live demo will be available here once deployed.

## Demo

*   (Coming Soon) - A gif demo will be available here once deployed.

## How to Run the Project Locally

### Prerequisites

*   Python 3.8 or higher
*   Git

### Installation

1.  Clone the repository to your machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/check-most-liked-spotify.git
    ```

2.  Navigate to the project directory:
    ```bash
    cd check-most-liked-spotify
    ```

3.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    ```

    # Activate on Windows 
    ```bash
    .\venv\Scripts\activate
    ```

    # Activate on macOS/Linux
    ```bash
    source venv/bin/activate
    ```

4.  Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configure Spotify API Credentials

To interact with the Spotify Web API, you need to register an application and obtain API credentials.

1.  Go to the [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard) and log in with your Spotify account.
2.  Click on "Create App" to create a new application.
3.  Give your application a name and description.
4.  After creating the app, you will see your **Client ID** and a button to show your **Client Secret**. Keep these secure!
5.  Click on "Edit Settings" for your application.
6.  Under "Redirect URIs", add the following URI:
    ```
    http://127.0.0.1:5000/callback
    ```
    Make sure this URI is exactly as shown, as it's where Spotify will redirect users after successful authentication. You **must** add this URI to your Spotify app settings.
7.  Save the settings.

### Create a `.env` File

In the root directory of your project (`check-most-liked-spotify/`), create a file named `.env` (note the leading dot). This file will store your sensitive API credentials and should **not** be committed to version control (it's already included in `.gitignore`).

Add the following lines to your `.env` file, replacing the placeholder values with your actual Spotify credentials and the correct redirect URI:

```ini
SPOTIPY_CLIENT_ID="YOUR_CLIENT_ID_HERE"
SPOTIPY_CLIENT_SECRET="YOUR_CLIENT_SECRET_HERE"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:5000/callback"
FLASK_SECRET_KEY="YOUR_RANDOM_SECRET_KEY_HERE"
```

For `FLASK_SECRET_KEY`, generate a long, random string. This is crucial for Flask's session management security.

### Execution

1.  With the virtual environment activated and `.env` file configured, you can now run the Flask application:
    ```bash
    python app.py
    ```

2.  Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Project Structure

```
check-most-liked-spotify/
├── .env
├── .gitignore
├── requirements.txt
├── app.py
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── spotify_client.py      # Manages Spotify API authentication and authorization flow.
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── data_analyzer.py     # Contains logic for processing raw Spotify data to extract insights.
│   └── visualization/
│       ├── __init__.py
│       └── plot_generator.py    # Responsible for generating data visualizations (bar charts).
├── templates/
│   ├── index.html               # Homepage template.
│   └── results.html             # Analysis results display template.
└── README.md
```

## Technologies Used

*   **Python:** The core programming language for the backend logic and data processing.
*   **Flask:** A lightweight Python web framework used to build the web application.
*   **Spotipy:** A Python library for the Spotify Web API, simplifying authentication and data retrieval.
*   **Matplotlib:** A comprehensive library for creating static, animated, and interactive visualizations in Python.
*   **Seaborn:** A data visualization library based on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.
*   **python-dotenv:** Used for loading environment variables from a `.env` file, ensuring secure handling of API credentials.
*   **HTML/CSS:** For structuring and styling the web interface.
