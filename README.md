# Soccer Mine
Fifa 21 players index, created using [FifaIndex](https://www.fifaindex.com/). 

 1. `git clone git@github.com:terriblebassist/soccer_mine.git`
 2. `cd soccer_mine`
 3. `virtualenv -p python3 venv`
 4. `source venv/bin/activate`
 5. `pip install -r requirements.txt`
 6. `scrapy crawl fifa -o <filename>.json`



## Sample Output
[{
"name": "Lionel Messi",
"rating": "93",
"profile": {
    "name": "Lionel Messi",
    "Height": [
        "170 cm",
        "5'7\""
    ],
    "Weight": [
        "72 kg",
        "159 lbs"
    ],
    "Preferred Foot": "Left",
    "Birth Date": "June 24, 1987",
    "Age": "33",
    "Player Work Rate": "Medium / Low",
    "Value": [
        "€103.500.000",
        "$117.000.000",
        "£93.000.000"
    ],
    "Wage": [
        "€560.000",
        "$630.000",
        "£500.000"
    ]
},
"teams": [{
        "name": "Argentina",
        "details": {
            "Position": "RW",
            "Kit Number": "10"
        }
    },
    {
        "name": "FC Barcelona",
        "details": {
            "Position": "RF",
            "Kit Number": "10",
            "Joined Club": "July 1, 2004",
            "Contract Length": "2021"
        }
    }
],
"skills": {
    "Ball Skills": {
        "Ball Control": "96",
        "Dribbling": "96"
    },
    "Defence": {
        "Marking": "32",
        "Slide Tackle": "24",
        "Stand Tackle": "35"
    },
    "Mental": {
        "Aggression": "44",
        "Reactions": "94",
        "Att. Position": "93",
        "Interceptions": "40",
        "Vision": "95",
        "Composure": "96"
    },
    "Passing": {
        "Crossing": "85",
        "Short Pass": "91",
        "Long Pass": "91"
    },
    "Physical": {
        "Acceleration": "91",
        "Stamina": "72",
        "Strength": "69",
        "Balance": "95",
        "Sprint Speed": "80",
        "Agility": "91",
        "Jumping": "68"
    },
    "Shooting": {
        "Heading": "70",
        "Shot Power": "86",
        "Finishing": "95",
        "Long Shots": "94",
        "Curve": "93",
        "FK Acc.": "94",
        "Penalties": "75",
        "Volleys": "88"
    },
    "Goalkeeper": {
        "GK Positioning": "14",
        "GK Diving": "6",
        "GK Handling": "11",
        "GK Kicking": "15",
        "GK Reflexes": "8"
    },
    "Specialities": [
        "Dribbler",
        "Distance Shooter",
        "FK Specialist",
        "Acrobat",
        "Clinical Finisher"
    ],
    "Traits": [
        "Finesse Shot",
        "Long Shot Taker (CPU AI Only)",
        "Speed Dribbler (CPU AI Only)",
        "Playmaker (CPU AI Only)",
        "Outside Foot Shot",
        "One Club Player",
        "Team Player",
        "Chip Shot (CPU AI Only)"
    ]
},
"link": "https://www.fifaindex.com/player/158023/lionel-messi/" }]
