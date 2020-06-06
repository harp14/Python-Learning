# Creating customer containers such as this example where we can keep a track of the
# number of various tags on a blog


class TagCloud:
    def __init__(self):
        # To make the tags variable (member) private (not accessible by calling
        # print(clouds.tags["PYTHON"])) put __ at the beginning of the tags variable
        self.__tags = {}

    def add(self, tag):
        # Adding 1 to the value of tag (making tags lower case)
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")

# If we didn't add in the additional method above we would see Python separate to python
cloud.add("Python")

# We can only do the below because of the __getitem__ method
print(cloud["python"])

# We can only do the below because of the __len__ and __iter__ methods
print(len(cloud))

'''
# Here are the various operations we can do to containers:
cloud = TagCloud()
# Number of items in container
len(cloud)
# Get number of items by key
cloud["python"] = 10
# Iterate over this container
for tag in cloud:
    print(tag)
'''
