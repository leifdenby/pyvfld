# Below were parsed from
# https://github.com/Hirlam/Monitor/blob/514cbefe0bbe6cd3e92404216e84443c3eae5577/scr/plotdefs.pm

MONITOR_PLOTDEFS_VARIABLES = {
    "VI": {
        "TEXT": "Visibility",
    },
    "NN": {
        "TEXT": "Cloud cover",
    },
    "PS": {
        "TEXT": "Mslp",
    },
    "SPS": {
        "TEXT": "Station pressure",
        "UNIT": "hPa",
    },
    "TTHA": {
        "TEXT": "T2m, height corr.",
        "UNIT": "deg C",
    },
    "TT": {
        "TEXT": "T2m",
    },
    "TN": {
        "TEXT": "Min T2m",
        "ACC": 12,
    },
    "TX": {
        "TEXT": "Max T2m",
        "ACC": 12,
    },
    "TD": {
        "TEXT": "Td2m",
        "TEXT_TEMP": "Dew point T",
    },
    "TDD": {
        "TEXT": "Td2m deficit",
        "UNIT": "deg C",
    },
    "FI": {
        "TEXT_TEMP": "Geopotential",
    },
    "FF": {
        "TEXT": "U10m",
    },
    "FX": {
        "TEXT": "Max U10m",
    },
    "GG": {
        "TEXT": "Wind Gust",
    },
    "GX": {
        "TEXT": "Max Wind Gust",
        "ACC": 1,
    },
    "DD": {
        "TEXT": "Wind direction",
    },
    "PE1": {
        "TEXT": "1h Precipitation",
        "ACC": 1,
        "UNIT": "mm/1h",
    },
    "PE3": {
        "TEXT": "3h Precipitation",
        "ACC": 3,
        "UNIT": "mm/3h",
    },
    "PE6": {
        "TEXT": "6h Precipitation",
        "ACC": 6,
    },
    "PE12": {
        "TEXT": "12h Precipitation",
        "ACC": 12,
        "UNIT": "mm/12h",
    },
    "PE24": {
        "TEXT": "24h Precipitation",
        "ACC": 24,
        "UNIT": "mm/24h",
    },
    "CH": {
        "TEXT": "Cloud base",
        "UNIT": "m",
    },
    "ISS": {
        "TEXT": "Relative humidity over ice",
        "UNIT": "%",
    },
    "N75": {
        "TEXT": "clouds <7500m",
        "UNIT": "octas",
    },
    "DSN": {
        "TEXT": "Snow depth",
        "UNIT": "cm",
    },
    "LC": {
        "TEXT": "Low clouds",
        "UNIT": "octas",
    },
    "QQ": {
        "TEXT": "Q2m",
    },
    "RH": {
        "TEXT": "Rh2m",
        "TEXT_TEMP": "Relative humidity",
    },
    "GR": {
        "TEXT": "Global radation",
        "TWIND_SURF": 1,
    },
    "WT": {
        "TEXT": "Sens heat flux",
        "TWIND_SURF": 1,
    },
    "WQ": {
        "TEXT": "Lat heat flux",
        "TWIND_SURF": 1,
    },
    "UW": {
        "TEXT": "Momentum flux",
        "TWIND_SURF": 1,
    },
    "TZ": {
        "TEXT": "dT/dz",
        "TWIND_SURF": 1,
    },
    "LU": {
        "TEXT": "Long wave up",
        "TWIND_SURF": 1,
    },
    "TMAST": {
        "TEXT": "Temperature",
        "UNIT": "deg C",
    },
    "RHMAST": {
        "TEXT": "Relative hum",
        "UNIT": "%",
    },
    "FFMAST": {
        "TEXT": "Wind speed",
        "UNIT": "m/s",
    },
}


MONITOR_PLOTDEFS_VARIABLES["PE"] = MONITOR_PLOTDEFS_VARIABLES["PE12"]

VARIABLES = MONITOR_PLOTDEFS_VARIABLES
