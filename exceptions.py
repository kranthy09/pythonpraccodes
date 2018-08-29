main_list = [(19, 20), (40, 0), (34, 10), (99,78), (100,0)]

for num, denum in main_list:
    try:
        result = num/denum
        print(result)
    except ZeroDivisionError as exc:
        print(exc.__str__(), "i got exception")


class AgeLessThanVoterPermitException(Exception):
    pass


def validate_voter_age(age):
    if age < 18:
        raise AgeLessThanVoterPermitException('age less that 18')

    return True

#validate_voter_age(10)


try:
     validate_voter_age(10)
except AgeLessThanVoterPermitException as exc:
    print(' i catched exception')





