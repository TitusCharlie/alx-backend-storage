def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name
    :param mongo_collection: pymongo collection object
    :param name: string, school name to update
    :param topics: list of strings, the topics to set for the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )