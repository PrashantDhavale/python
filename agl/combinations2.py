import json
import itertools

params_info = {
    "x": [1, 2, 3],
    "y": ["a", "b", "c"],
    "z": ["A", "B", "C"],
    "dvValues": [True, False],
    "regValues": [True, False],
    "hasDobValues": [True, False],
    "hasAgeValues": [True, False],
    "deceasedValues": [True, False],
    "relTypeValues": ["OWNER", "SECONDARY_USER", "NOMINATED_REPRESENTATIVE"],
}

for param_vals in itertools.product(*params_info.values()):
    params = dict(zip(params_info.keys(), param_vals))

    data = {
        "relationships": [
            {
                "type": params["relTypeValues"]
            }
        ],
        "eligibility": [
            {
                "type": "dvStatus",
                "value": params["dvValues"]
            },
            {
                "type": "registrationStatus",
                "value": params["regValues"]
            },
            {
                "type": "hasDob",
                "value": params["hasDobValues"]
            },
            {
                "type": "hasAge",
                "value": params["hasAgeValues"]
            },
            {
                "type": "deceased",
                "value": params["deceasedValues"]
            },
        ]
    }

    jsonStr = json.dumps(data)
    print(jsonStr)
