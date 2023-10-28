# My Study Planner

This Python script uses the Google Calendar API to create a study plan by adding study events to your Google Calendar. You can customize your study plan by defining tasks for each day and time slot, and the script will create corresponding events in your calendar.

## Prerequisites

Before you can use this script, you need to set up your Google Calendar API credentials and install the required libraries. Follow these steps:

1. Create a Google Cloud Project:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project if you don't have one already.

2. Enable the Google Calendar API:
   - In the Cloud Console, navigate to "APIs & Services" > "Library."
   - Search for "Google Calendar API" and enable it for your project.

3. Create OAuth 2.0 Client ID:
   - In the Cloud Console, navigate to "APIs & Services" > "Credentials."
   - Click "Create credentials" and choose "OAuth client ID."
   - Select "Desktop App" as the application type.
   - Download the JSON file that contains your client secrets.

4. Save the JSON file:
   - Save the downloaded JSON file to a location on your computer.
   - Update the `CLIENT_SECRETS_FILE` variable in the script with the file path.

5. Install the required libraries:
   - Run the following command to install the necessary Python libraries:
     ```
     pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```

## Usage

1. Customize Your Study Plan:
   - Modify the `get_study_plan` function in the script to define your study plan. You can specify tasks for different days and times.

2. Run the Script:
   - Execute the script by running it in your Python environment.

3. Authenticate Your Google Account:
   - If you haven't authorized the application before, the script will open a web page for you to authenticate and grant access to your Google Calendar.

4. Study Events Creation:
   - The script will create study events in your Google
