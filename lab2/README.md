# Introduction
The aim of this lab exercise is to develop a system model from the problem domain to function model and finally object model. This will include the design of a use case and class diagram which are defined by the UML(unified modelling language).
# Problem domain
You have been tasked with designing the software system for a simple weather-station. A
weather station records local weather information and periodically transfers this to a
weather information system using a satellite link. Currently the system keeps track of
temperature, wind speed (Anemometer) and pressure (barometer) but must be flexible
enough to be expanded at a later stage.
The system is composed of a basic Micro-controller, a single temperature sensor, a display,
memory bank and user buttons.
The system displays temperature readings in real time on the display. It also keeps track of
historical information on an hourly and daily basis. This historical data can be pulled up on
the display at the request of the user by pressing the appropriate button.
## Actors identified
* primary actors:
    * Micro-controller
    * User
* secondary actors:
    * display
    * memory bank
    * temperature sensor
## use cases identified
* read sensors
* get data
* save data
* read temperature
* update display
* view history
