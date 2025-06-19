emails = "ali@gmail.com,vali@mail.ru,karim@gmail.com"
domains = list({f"@{email.strip().split('@')[1]}" for email in emails.split(",")})
print(domains)
