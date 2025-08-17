<p align="center">
<img src="https://i.imgur.com/t1zgSyx.jpeg" alt="Microsoft Active Directory Logo" height="70%" width="70%"/>
</p>

<h1 align="center">Network Monitoring Dashboard 🖥️ </h1>

<h4 align="center"> Why is this helpful? </h4>
<p align="center"> This network monitoring dashboard allows us to view our network health with alerting capabilities and added visuals.  </p>

<br> </br> 


<h2 align="center"> 📦 Technologies & Libraries used and why </h2>

- Visual Studio Code (VSCode) - The editor where all the code was written, tested, and managed.
- Virtual Environment (Venv) - keeps the project dependencies separate from other Python projects on my pc. 
- Python - Simple and quick for building tools without a steep learning curve.
- Psutil - A cross-platform library. Tracks CPU, memory, and disk usage on the system.
- Ping3 - A simple library for testing ping latency. Measures how quickly my computer can talk to a server (network latency).
- Flask - Lightweight Python web framework. Turns the collected data into a simple web dashboard I can view in my browser.
- Speedtest-cli - A Python library. Checks internet download and upload speeds automatically.
- Git Bash - So I can run my Python app functions and push my project to GitHub more easily.
- Schedule – Runs the data collection at regular intervals without needing to start it manually.
- Chart.js - A JavaScript library. Creates interactive graphs to display network and system performance visually.
  <br> </br>

  <h4 align="center"> Walking Through My App </h4>
  
<p align="center"> First, I open git bash, then navigate to the folder that my network-monitoring-dashboard app is in. Then I proceed to activate venv. Venv is the Python environment that enables apps to function properly (in short terms).  </p>

<img src="https://i.imgur.com/SOEHYcs.png" alt="" align="center" height="70%" width="70%"/>
<br> </br>

  
<p align="center"> Then within the network-monitor-dashboard, I run the pyython "collect_data.py" which gathers the network information needed for display. I wait until it says data collected due to this process taking a bit of a while.</p>

<img src="https://i.imgur.com/SOEHYcs.png" alt="" align="center" height="70%" width="70%"/>
<br> </br>


<p align="center"> Once the data is collected, I then run the Python "app.py", which then displays the networking monitoring dashboard on the IP at (http://127.0.0.1:5000/). </p>

<img src="https://i.imgur.com/j0UDmNt.png" alt="" align="center" height="70%" width="70%"/>
<br> </br>


<p align="center">Although it's not that pretty, it still displays information to me that is useful. It also keeps track of the dates that this app was run in the past, which is helpful when comparing the network information now with what in the past to see what has changed. </p>

<img src="https://i.imgur.com/1Fq1LRQ.png" alt="" align="center" height="70%" width="70%"/>

<p align="center">This chat utilizes the ping3 command in Python to check if another computer/server is reachable on a network. And it displays the speed at which it is also available. </p>
<br> </br>

<p align="center"> If we scroll down to the second page.... </p>

<br> </br>

<p align="center">We can see the upload and download speeds in Mbps. Along with relative dates to the last time I ran this app. </p>

<img src="https://i.imgur.com/I2EfRMO.png" alt="" align="center" height="70%" width="70%"/>
<br> </br>

<br> </br>
<p align="center">Once I'm finished review the information provided, I hit "CTRL-C" to quit out of the app.</p>

<img src="https://i.imgur.com/Wj5UhPn.png" alt="" align="center" height="70%" width="70%"/>
<br> </br>





<p align="center"> (End of Demonstration) </p>

<br> </br>








