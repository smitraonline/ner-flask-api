import re

ex = 'I changed my email from johnd@in.ibm.com to john_peter.ibm@quick.learner.co.uk yesterday.'

pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

# email anonymize handler for api.
def anonymize(data):
    try:
        # data = re.sub(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", " ", data)
        data = pattern.sub("[Email]", data)
    finally:
        return data
        pass

# test
# print(anonymize_email(ex))
