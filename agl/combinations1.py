import json

o = json.loads("""
{
    "Success": true,
    "Options": [
        {
            "OptionId": 123,
            "Question": "Color:",
            "Choices": [
                {
                    "ChoiceId": 333,
                    "Choice": "red",
                    "Url": "color/red/",
                    "Exceptions": []
                },
                {
                    "ChoiceId": 334,
                    "Choice": "green",
                    "Url": "color/green/",
                    "Exceptions": []
                }
            ]

        },
        {
            "OptionId": 223,
            "Question": "material:",
            "Choices": [
                {
                    "ChoiceId": 223,
                    "Choice": "metal",
                    "Url": "material/metal/",
                    "Exceptions": []
                },
                {
                    "ChoiceId": 227,
                    "Choice": "rubber",
                    "Url": "material/rubber/",
                    "Exceptions": []
                },
                {
                    "ChoiceId": 229,
                    "Choice": "glass",
                    "Url": "material/glass/",
                    "Exceptions": []
                }
            ]

        },
        {
            "OptionId": 123,
            "Question": "finish:",
            "Choices": [
                {
                    "ChoiceId": 123,
                    "Choice": "matte",
                    "Url": "finish/matte/",
                    "Exceptions": []
                },
                {
                    "ChoiceId": 123,
                    "Choice": "glossy",
                    "Url": "finish/glossy/",
                    "Exceptions": []
                },
                {
                    "ChoiceId": 123,
                    "Choice": "mix",
                    "Url": "finish/mix/",
                    "Exceptions": []
                }
            ]

        }

    ]

}              """)
# now we have the JSON data in the Python object o
questions = [oo["Question"] for oo in o["Options"]]
# now we have the questions = ['Color:', 'material:', 'finish:']
choices = [[c["Choice"] for c in oo["Choices"]] for oo in o["Options"]]


# now we have the choices = [['red', 'green'],
#                            ['metal', 'rubber', 'glass'],
#                            ['matte', 'glossy', 'mix']]

# a well-known recursive algorithm for the cartesian product
# (could instead use itertools.product() as suggested)
def products(cs):
    if cs:
        for c in cs[-1]:
            for p in products(cs[:-1]): yield p + [c]
    else:
        yield []


cnt = 0
for p in products(choices):  # count and print each result in the desired format
    cnt += 1
    print("%d." % cnt, ", ".join([" ".join(qc) for qc in zip(questions, p)]))