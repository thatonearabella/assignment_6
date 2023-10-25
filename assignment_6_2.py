nfile = "mbox.txt"

host1 = set()
with open(nfile, "r") as file:
  for i in file:
    if i.startswith("From:"):
      email_account = i.split()[1]
      hostName = email_account.split("@")[1]
      host1.add(hostName)
      
for hostName in host1:
  print(hostName)

print(f"Total {len(host1)} hosts printed")