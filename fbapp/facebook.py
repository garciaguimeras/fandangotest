from facepy import GraphAPI

def post_message(access_token, facebook_id, msg):
    graph = GraphAPI(access_token)
    fbpath = "{0}/feed".format(facebook_id)
    graph.post(path=fbpath, message=msg)
