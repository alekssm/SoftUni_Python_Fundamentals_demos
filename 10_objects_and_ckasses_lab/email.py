class Email():
    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


data = input()
emails = []

while not data == "Stop":
    the_input = data.split()
    sender = the_input[0]
    receiver = the_input[1]
    content = the_input[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    data = input()

indexes = list(map(int, input().split(", ")))
for ele in indexes:
    emails[ele].send()

for ele in emails:
    print(ele.get_info())