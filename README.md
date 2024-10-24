<h1 align="center">Voice-Powered Note-Taking Application</h1>
<h3 align="center">A Python-based application that lets you take notes through voice commands</h3>

<h2>🔭 Overview</h2>
<p>The <strong>Voice-Powered Note-Taking Application</strong> allows you to take notes using voice commands in Python. You can say "next line" to move to the next line and "stop" to finish and save your notes as a <code>.txt</code> file. It uses speech recognition for converting speech to text and provides real-time voice feedback.</p>

<h2>🚀 Features</h2>
<ul>
  <li><strong>Voice-Activated Note-Taking:</strong> Capture notes by speaking into the microphone.</li>
  <li><strong>Real-Time Command Recognition:</strong> Use "next line" to move to the next line in your notes.</li>
  <li><strong>Automated Saving:</strong> Say "stop" to automatically save the notes as a timestamped <code>.txt</code> file.</li>
  <li><strong>Text-to-Speech Feedback:</strong> Provides real-time voice feedback for your commands.</li>
  <li><strong>Timestamped File Naming:</strong> Saved files are organized with a timestamped filename.</li>
</ul>

<h2>🌱 Technologies Used</h2>
<ul>
  <li><strong>Python 3.8+</strong></li>
  <li><strong>SpeechRecognition:</strong> Converts spoken audio to text.</li>
  <li><strong>Pyttsx3:</strong> Provides text-to-speech feedback.</li>
  <li><strong>Google Web Speech API:</strong> Ensures accurate voice recognition.</li>
  <li><strong>Datetime:</strong> Helps organize files by timestamp.</li>
</ul>

<h2>📦 Required Libraries</h2>
<ul>
  <li><strong>SpeechRecognition</strong></li>
  <li><strong>Pyttsx3</strong></li>
  <li><strong>Datetime</strong></li>
</ul>

<h2>⚙️ Installation</h2>
<ol>
  <li><strong>Clone the repository:</strong>
    <pre><code>git clone https://github.com/your-username/voice_note_taker.git
cd voice_note_taker</code></pre>
  </li>
  <li><strong>Set up a virtual environment:</strong> (optional but recommended)
    <pre><code>python -m venv venv
source venv/bin/activate  # For Linux/MacOS
# or
venv\Scripts\activate     # For Windows</code></pre>
  </li>
  <li><strong>Install dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><strong>Install PyAudio:</strong>
    <pre><code>pip install pyaudio</code></pre>
    <p><em>(For Windows, download PyAudio binaries <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio">here</a>. For Mac/Linux, use <code>brew install portaudio</code> or <code>sudo apt-get install python-pyaudio</code>.)</em></p>
  </li>
</ol>

<h2>🚀 Usage</h2>
<ol>
  <li><strong>Run the application:</strong>
    <pre><code>python main.py</code></pre>
  </li>
  <li><strong>Start note-taking:</strong>
    <ul>
      <li>Speak your notes into the microphone.</li>
      <li>Say <strong>"next line"</strong> to move to the next line in your notes.</li>
      <li>Say <strong>"stop"</strong> to save the notes as a <code>.txt</code> file with a timestamped filename.</li>
    </ul>
  </li>
</ol>

<h2>📂 Project Structure</h2>
<pre>
voice_note_taker/
├── main.py              # Main script for running the application
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
</pre>

<h2>💡 How It Works</h2>
<ul>
  <li><strong>Listening:</strong> The app listens for voice commands like "next line" and "stop".</li>
  <li><strong>Speech-to-Text:</strong> The voice input is converted into text using the Google Web Speech API.</li>
  <li><strong>Text-to-Speech Feedback:</strong> The app provides spoken feedback using <strong>Pyttsx3</strong>.</li>
  <li><strong>Saving Notes:</strong> When the "stop" command is recognized, the notes are saved as a text file with a timestamp.</li>
</ul>

<h2>📊 Example Output</h2>
<pre>
notes_20231016_113000.txt
--------------------------------------
Here are my notes for the meeting.
Next line.
We need to discuss the project timeline.
Next line.
Budget review is scheduled for next week.
Stop.
</pre>

<h2>📸 Demo Flow</h2>
<ol>
  <li><strong>Initialization:</strong> The system says, "I am ready to take notes. Say 'next line' to move to the next line, and 'stop' to finish."</li>
  <li><strong>Recording:</strong> You speak your notes, and the app converts your speech to text, printing it in the terminal.</li>
  <li><strong>Commands:</strong> Use "next line" to start a new line or "stop" to end the session and save the notes.</li>
  <li><strong>File Output:</strong> The notes are saved as a <code>.txt</code> file with a timestamped filename.</li>
</ol>

<h2>⚠️ Known Issues and Limitations</h2>
<ul>
  <li><strong>Internet Dependency:</strong> The app requires an internet connection to use the Google Web Speech API.</li>
  <li><strong>Ambient Noise:</strong> Background noise may interfere with speech recognition, although <code>adjust_for_ambient_noise()</code> helps reduce its impact.</li>
</ul>

<h2>🔧 Future Enhancements</h2>
<ul>
  <li><strong>Offline Mode:</strong> Use an offline speech recognition engine like <a href="https://alphacephei.com/vosk/">Vosk</a>.</li>
  <li><strong>Wake Word:</strong> Add a wake word (e.g., "Hey Assistant") to initiate note-taking.</li>
  <li><strong>Multi-Language Support:</strong> Add support for multiple languages.</li>
</ul>

<h2>🛠 Languages and Tools</h2>
<p align="left">
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40" />
  </a>
</p>

<h2>📝 License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>
