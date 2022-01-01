# supermemo-to-anki

Simple project to parse cards from [Supermemo](https://app.supermemo.com/) to txt file, which later could be imported into Anki.  
Currently, only plain text content parsed: HTML tags are cleared, no newlines allowed.

## Usage flow

1. Customize envs;
2. Run 'main.py';
3. Parse cards into {course_title}.txt files;
4. Go to Anki, press 'Import', select files, specify delimiter (semicolon by default).

## Technical flow

1. Auth into Supermemo by Selenium;
2. Copy Obtained cookies into requests Session object;
3. Get information about courses and cards by Supermemo API;
4. Parse cards content via BeautifulSoup (currently trims to simple text);
5. Write cards to {course_title}.txt files at the same dir as 'main.py'.

# Environment variables

Variables could be passed separately and by '.env' file thanks to [python-dotenv](https://pypi.org/project/python-dotenv/) package.  
Env file must be located at the same dir as 'main.py'.

| Name               | Type   | Default value | Description                                                                                                  |
|--------------------|--------|---------------|--------------------------------------------------------------------------------------------------------------|
| DRIVER_PATH        | string |               | Path to Selenium webdriver.                                                                                  |
| EMAIL              | string |               | Email to auth into Supermemo.                                                                                |
| PW                 | string |               | Password to auth into Supermemo.                                                                             |
| USER_ID            | string |               | User id from Supermemo. Could be obtained from borswer network tab.                                          |
| DELIMITER          | string | ;             | Delimiter to separate front and back of card. Anki supports custom delimiters, but semicolon is recommended. |
| LOGGING_LEVEL_ROOT | string | INFO          | Default log level. Debug for verbose logs.                                                                   |
