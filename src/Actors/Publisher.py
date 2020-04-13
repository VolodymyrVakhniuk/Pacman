from Actors.Actor import Actor


class Publisher:

    def __init__(self):
        self.actorsList = []


    def addActor(self, *actors : Actor):

        for actor in actors:
            self.actorsList.append(actor)


    def notify(self, data):

        for actor in self.actorsList:
            actor.notify()

    
