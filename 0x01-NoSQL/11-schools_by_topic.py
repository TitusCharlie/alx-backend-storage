def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    :param mongo_collection: pymongo collection object
    :param topic: string, topic to search
    :return: list of schools that have the topic
    """
    return mongo_collection.find({"topics": topic})