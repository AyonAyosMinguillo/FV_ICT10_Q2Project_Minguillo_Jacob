from pyscript import document, display # type: ignore

# Dictionary containing weather instrument information
# instrument name, measurement, unit of measurement, purpose
Weather = {
    "Thermometer": ("Thermometer", "Air Temperature", "Degrees Celsius (°C)", "Measures how hot or cold the air is"),
    "Barometer": ("Barometer", "Atmospheric Pressure", "Hectopascals (hPa)", "Measures air pressure to help monitor weather changes."),
    "Anemometer": ("Anemometer", "Wind Speed", "Kilometers per hour (km/h)", "Measures how fast the wind is blowing."),
    "Hygrometer": ("Hygrometer", "Relative Humidity", "Percent (%)", "Measures the amount of moisture in the air."),
    "Rain Gauge": ("Rain Gauge", "Precipitation", "Millimeters (mm)", "Measures the amount of rainfall in an area."),
    "Wind Vane": ("Wind Vane", "Wind Direction", "Cardinal Directions", "Identifies the direction from which the wind is blowing."),
    "Weather Balloon": ("Weather Balloon", "Atmospheric Conditions", "Varies", "Collects atmospheric data at different altitudes."),
    "Pyranometer": ("Pyranometer", "Solar Radiation", "Watts per square meter (W/m²)", "Measures incoming solar radiation."),
}

# the thing to find the things
def find(e=None):
    # convert to title case
    Weeder = document.getElementById("Weather").value.strip()
    symbol = Weeder.title() if Weeder else ""

    # the code looks at the dictionary for weather and if the inputted thing is not there, it will display:
    result = Weather.get(symbol, ("Not Found", "Unsupported Instrument", "N/A", "N/A"))

    # these are displayed in the html
    document.getElementById("msr").innerText = result[1]
    document.getElementById("uom").innerText = result[2]
    document.getElementById("prp").innerText = result[3]

    document.getElementById("result1").style.display = "block" # When button is pressed reveal result

    document.getElementById("result1").style.display = "block"