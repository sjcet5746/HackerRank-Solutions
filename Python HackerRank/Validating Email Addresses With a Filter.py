#Written by Gskd
import re

def fun(s):
    email_pattern = r'^[\w|\-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    m = re.match(email_pattern, s)
    return m

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
