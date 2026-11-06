import json
from loadable import Loadable

# These would be better in separate files
class Event:
    def __init__(
            self,
            attendance_mode="",
            start_date="",
            end_date=""
        ):
        self.attendance_mode = attendance_mode
        self.start_date = start_date
        self.end_date = end_date

class Hackathon(Event, Loadable):
    def __init__(self,
            attendance_mode="",
            start_date="",
            end_date="",
            theme="",
            description=""
        ):
        super().__init__(attendance_mode, start_date, end_date)
        self.theme = theme
        self.description = description

    @classmethod
    def load(cls, object_dictionary):
        # Assume the object dictionary has all keys?
        return cls(
            attendance_mode=object_dictionary.get("attendance_mode"),
            start_date=object_dictionary.get("start_date"),
            end_date=object_dictionary.get("end_date"),
            theme=object_dictionary.get("theme"),
            description=object_dictionary.get("description")
        )



class Conference(Event, Loadable):
    def __init__(self,
            attendance_mode="",
            start_date="",
            end_date="",
            subject="",
        ):
        super().__init__(attendance_mode, start_date, end_date)
        self.subject = subject

    @classmethod
    def load(cls, object_dictionary):
        # Assume the object dictionary has all keys?
        return cls(
            attendance_mode=object_dictionary.get("attendance_mode"),
            start_date=object_dictionary.get("start_date"),
            end_date=object_dictionary.get("end_date"),
            subject=object_dictionary.get("subject"),
        )


# Look at this function -- it takes a file that it assumes is json and parses it
# Experiment with giving it files and see what it returns.
# Remember that you can run files in python 'interactively' with `python -i filename.py`
def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        try:
            return json.loads(file.read())
        except json.JSONDecodeError:
            print("JSONDecode error! Check your formatting")
            return []

events = []

for entry in read_file("fixture.json"):
    kind = entry.get("kind")
    if kind == None:
        continue
    if kind == 'conference':
        events.append(Conference.load(entry))
    if kind == 'hackathon':
        events.append(Hackathon.load(entry))

for event in events:
    print(event.start_date, event.end_date)