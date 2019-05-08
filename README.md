# greased-lighting
Software to control the LED strips built into the set of the Gonzaga Dramatic Association's 2019 production of Grease.

Co-authors - Andrew Farabow and Matthew Dukes

### Project Status
Currently, this program is setup to only do the cues required for the show for which it was designed. However, I have plans to convert it into a general-purpose LED controller.

### Roadmap
- move show-specific preprogrammed cues into a seperate branch for historical reasons, remove from main
- implement a command-line sytax to set the lights to pre-defined colors or RGB input
   - ex: `greased-lighting serial-device color`
- debug Arduino blinking code
- add fade option
- create PCB schematic and get some printed

### Dependencies
- pySerial
