from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is DAVID and I am going to help you behalf of EIGHT 21.", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)created(.*)",
        ["team EIGHT 21 created me", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bengaluru, India', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|games|sport)(.*)",
        ["I'm a very big fan of Cricket|Footbal", ]
    ],
[
        r"who (.*) (player)?",
        ["I am a big fan of Sachin Ramesh Tendulkar"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Die heart fan of Shah Rukh Khan"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],


    [
        r"can i(.*)(models|model|watches|watch)(.*)",
        ["Sure ! I will help you",]
    ],
    [
        r"i am looking for watches(.*)(below 1000|less than 1000|not more than 1000(.*)",
        ["We have 3 models available in our collections, E21-001,E21-002,E21-003",]
    ],
    [
        r"i am looking for watches(.*)(below 2000|less than 2000|not more than 2000(.*)",
        ["We have 7 models available in our collections, E21-001,E21-002,E21-003,E21-004,E21-005,E21-006,E21-007",]
    ],
    [
        r"i am looking for watches(.*)(below 3000|less than 2000|not more than 2000(.*)",
        ["We have 10 models available in our collections, E21-001,E21-002,E21-003,E21-004,E21-005,E21-006,E21-007,E21-008,E21-008,E21-009,E21-010", ]
    ],
    [
        r"i am looking for watches(.*)(above 1000|more than 1000(.*)",
        [
            "We have 7 models available in our collections, E21-004,E21-005,E21-006,E21-007,E21-008,E21-008,E21-009,E21-010", ]
    ],
    [
        r"i am looking for watches(.*)(above 2000|more than 2000(.*)",
        [
            "We have 3 models available in our collections, E21-008,E21-008,E21-009,E21-010", ]
    ],
    [
        r"who is your(.*)(md|managing director|m.d|owner(.*)",
        [
            "Geetha Sebastian owns our company. She is the head of the designing department and Managing director for that past years", ]
    ],
    [
        r"when did company(.*)(established|started|orginated(.*)",
        [
            "Our company was started in 1994, and we have 26 years of experience and hand in this area.", ]
    ],



]
my_dummy_reflections= {
    "go": "gone",
    "hello": "hey there"
}
chat = Chat(pairs, reflections)
chat.converse()
