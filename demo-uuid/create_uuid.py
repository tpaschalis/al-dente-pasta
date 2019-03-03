import uuid

# Let's use uuid4 instead of uuid, since the latter depends on the machine's network address.
# It should be as simple as casting it to a string and removing the dashes
# We don't necessarily need the full length, so at first 
# we could limit it for more readable/shareable URLS.
foo = str(uuid.uuid4()).replace('-', '')
print(foo)
print(foo[:10])
