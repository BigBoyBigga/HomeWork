"""
Достаньте имя из словаря
"""

task = {
    "kluch1":[
        {"info1": "not name"},
        {
            "info2":{"still not name": "not name",
                     ("not name","oleg","another name"):"that what we need"
                     }
        }
    ]
}
name = list(task["kluch1"][1]["info2"].keys())[1][1]
print(name)
