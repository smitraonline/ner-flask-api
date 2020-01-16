import phonenumbers

text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."

# word tokenize and pos tagging
def test(sent):  
    for match in phonenumbers.PhoneNumberMatcher(text, "US"):
        print(match)

    for match in phonenumbers.PhoneNumberMatcher(text, "US"):
        print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))

# preprocess(text)


# phone anonymize handler for api
def anonymize(data):
    try:
        for match in phonenumbers.PhoneNumberMatcher(data, "US"):
            data = data.replace(match.raw_string, '<Phone>')   
    finally:
        return data
        pass