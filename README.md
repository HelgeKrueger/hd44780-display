# hd44780-display

Implementation of a daemon that displays messages on a
HD44780 LCD display using a Rasperry Pi. The first line
of the display is being used to display the date and
time. The second line is used to display an updating
message.

## Configuration

After connecting the display to the Raspberry PI, the
numbers of the GPIO pins connected need to be entered
in the **config.yaml** file.

## Running

Start **run.py stop** as root and **run.py stop**.

## Displaying messages

A message can be displayed by writing it into a file
in the directory configured in _messages.messageFolder_.
Once the message has been displayed, the corresponding
file is deleted. By regularly updating a file, one can
display a changing message.

## Example

An example of usage is included that displays the
current heartrate captured using an ANT+ heartrate
sensor and the openant package.

The openant is available at http://github.com/Tigge/openant.
