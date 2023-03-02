# OpenAI Automator Translate
### A script for Mac Automator that allows you to translate any selected text
### Installation
1. Install Python if you don't have it already. You can download it from the official website: https://www.python.org/downloads/macos/
2. Install the OpenAI library by running pip install OpenAI in your terminal.
3. Open up Automator.
4. Click File -> New and create a new Quick Action. You can name this action whatever you like, such as "Translate with OpenAI".
5. Set "Workflow receives current" to "text in any application".
6. Check the box for "Output replaces selected text".
7. Drag the "Run Shell Script" action to the right side, and select "/usr/local/bin/python" or "/usr/local/bin/python3" as the shell depending on your Python version.
8. Set "Pass input" to "stdin".
9. Copy and paste the code from the translate.py file, and replace [YOUR OPENAI API KEY] with your OpenAI API Key. You can also change the language you wish to translate to.
10. Save the Quick Action, and it should now show up as a right-click option when you select text in any application.

### Screenshots
<img width="1000" alt="Screenshot 2023-02-28 at 1 37 56 PM" src="https://user-images.githubusercontent.com/8294014/221986626-5ecd9fb8-b7c6-4ed3-a153-03d601998849.png">

![ezgif-3-7afd5066ae](https://user-images.githubusercontent.com/8294014/221989021-035fa5f0-a3f2-4dd8-ab63-77283414d462.gif)
