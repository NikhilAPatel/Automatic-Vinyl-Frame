import os

class MusicQueue:
    def __init__(self):
        self.queue = []
    
    def addToQueue(self, filepath):
        self.queue.append(filepath)
    
    def clearQueue(self):
        self.queue = []

    def generateAlbumQueue(self, filepath):
        files = next(os.walk(filepath))[2]
        for i in range(0, len(files)):
            files[i] = int(files[i].replace(".mp3", ""))
        files = sorted(files)
        self.queue = files
        for i in range(0, len(self.queue)):
            self.queue[i] = filepath + "/" + str(self.queue[i]) + ".mp3"
    
    def sendToBack(self):
        tempQueue = self.queue
        self.clearQueue()
        
        for i in range(1, len(tempQueue)):
            self.queue.append(tempQueue[i])
        
        self.queue.append(tempQueue[0])
    
    def getNextSong(self):
        return self.queue[0]
            
            
    def printQueue(self):
        for file in self.queue:
            print(file)

