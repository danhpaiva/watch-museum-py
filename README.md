<p align="center">
  <a href="#">
    <img src="logo/Watch-Museum.png" width="500" alt="Watch Museum">
  </a>
</p>
<p align="center">
    BackEnd of the mobile application for museum management
</p>

<p align="center">
 <a href="#status">Status</a> • 
 <a href="#objetivo">Objective</a> •
 <a href="#instalacao">Installation</a> • 
 <a href="#tecnologias">Technologies</a> • 
 <a href="#autor">Author</a> • 
 <a href="#licenca">Licence</a> 
</p>

<h2 align="center" id=status> 
	⌛ Concluded ⌛
</h2>

<h2 id=objetivo>:scroll: Objective</h2>

This project aims to build the backend of the mobile application, using the language: Python.<br>
The codes <strong>"arduino.py"</strong> simulate the humidity and temperature records that a physical Arduino can record.<br>
The file <strong>"backup_broker_local.py"</strong> saves the data to the local broker made in SQLite.<br>
And the other backup files send this data to the remote broker (ThingSpeak).<br>

This logic saves data from 03 museum rooms in the cloud and locally.<br>
If the system is without internet, as there is a verification system, it will act so that as soon as the Internet is re-established, verify the data that should go up to the remote broker.<br>
The system also records the average temperature on a daily basis.

<h2 id=instalacao>:clipboard: Installation</h2>

* Clone the repository.
* Run the file named:
> backup_broker_local.py

It records local backup data in half an hour interval.<br>
* Now run the file called:
> backup_broker_remoto.py

Every minute it will check the data locally to send it to the cloud.

* Choose the time and run the file:
> backup_broker_remotoMaxMin.py

For the system to back up the daily average.

For the frontend of the application see this repository:
[Watch Museum - React Native](https://github.com/danhpaiva/watch-museum-react-native) .

<h2 id=tecnologias>:toolbox: Technologies</h2>

The following tools were used in the construction of the project:

- IDE: <a href="https://code.visualstudio.com/">Visual Studio Code</a>
- Python 3.7.9 - <a href="https://www.python.org/downloads/release/python-379/"> Download </a>
- Remote Database: <a href="https://thingspeak.com/">ThingSpeak</a>
- Local Database: <a href="https://www.sqlite.org/download.html">SQLite 3</a>
- React Native - <a href="https://reactnative.dev/"> Download </a>

<h2 id=autor>:grin: Author</h2>

Developed by <a href="https://www.linkedin.com/in/danhpaiva/" target="_blank">Daniel Paiva</a>,
<a href="https://www.linkedin.com/in/francisco-fontoura/" target="_blank">Francisco Fontoura</a>,
<a href="https://github.com/gab-gomes" target="_blank">Gabriel Gomes</a> and 
<a href="https://www.linkedin.com/in/guilhermepujoni/" target="_blank">Guilherme Pujoni</a> .

<h2 id=licenca>:lock: Licence</h2>
<a href="https://github.com/danhpaiva/watch-museum-py/blob/main/LICENSE" target="_blank">MIT</a>
