
"""
You are given an integer  followed by  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is . 

"""




def fun(s):
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").isalnum(): 
        return False
    elif not website.isalnum():
        return False
    elif len(extension)>3:
        return False
    else:
        return True
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input("Enter number of Emails to check "))
    emails = []
    for _ in range(n):
        emails.append(input("Enter email to check validity. "))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)




"""
replace() function replaces a character.
Since, "-","_" is allowed it is replaced by "". Now can be checked for other alphanumeric comditions.

"""
