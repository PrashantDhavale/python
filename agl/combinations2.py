import json
import itertools

params_info = {

    "dvValues": [True, False],
    "regValues": [True, False],
    "hasDobValues": [True, False],
    "hasAgeValues": [True, False],
    "deceasedValues": [True, False]
}

for param_vals in itertools.product(*params_info.values()):
    params = dict(zip(params_info.keys(), param_vals))

    data = {
        "eligibility": [
            {
                "name": "dvStatus",
                "value": params["dvValues"]
            },
            {
                "name": "registrationStatus",
                "value": params["regValues"]
            },
            {
                "name": "hasDob",
                "value": params["hasDobValues"]
            },
            {
                "name": "hasAge",
                "value": params["hasAgeValues"]
            },
            {
                "name": "deceased",
                "value": params["deceasedValues"]
            }
        ]
    }

    jsonStr = json.dumps(data) + ","
    print(jsonStr)
