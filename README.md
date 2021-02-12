# Leak-Detect
Leak detection project for Raspberry Pi using Python 3. This project was used to monitor leaks from an aquarium tank external canister filter. When a leak is detected using a water level sensor, the RPi will send an SMS text to provided phone numbers using the smtplib library. A Twilio phone number was also created to send outgoing calls to provided phone numbers using the twilio library.

## sms.py

Requires the smtplib library:

```python
pip install smtplib
```

## voice.py

Requires the twilio library:

```python
pip install twilio
```
## leak-alert.py

Requires the time library for its sleep function, RPi.GPIO library, and the spidev library

```python
pip install sleep
pip install RPi.GPIO
pip install spidev
```


## Remote Access and Running the Program

To access the RPi and run the leak_alert.py script, we need to either ssh into the RPi or use a service like Dataplicity. Once you have remote access to the RPi, ensure you have tmux installed in order to close the remote connection and allow the program to continue running.

### Installing tmux

To check if tmux is installed, run the following code in RPi terminal:

```shell
tmux --version
```

If you do not have tmux installed, go ahead and install it (I am assuming you are using Raspberry Pi OS):

```shell
sudo apt upgrade && sudo apt update
sudo apt install tmux
```

### Using a tmux session to run the program

After installing tmux go ahead and start tmux:

```shell
tmux
```

Then navigate to the leak detection program's directory and run the following command to begin the program:

```shell
python3 leak_alert.py
```

Once you have confirmed that the program is running (you should see voltage readings being printed every 2 seconds or so), safely detach from the tmux session without exiting the remote jobs by pressing "CTRL-b" followed by "d". This will allow the program to continue running in that tmux session after you log out of your remote access platform.


To see what sessions in tmux are running:

```shell
tmux ls
```

You can reattach to the session running the leak detection program and confirm that it is still running by running:

```shell
tmux attach -t 0
```
Where 0 can be replaced by whichever session ID your leak detection program is running within.
