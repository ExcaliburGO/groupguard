from fbchat import log, Client
from fbchat.models import *
# Change this to your group id
old_thread_id = '1435863430058152'

# Change these to match your liking

class KeepBot(Client):
    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        # No point in trying to add ourself
        if old_thread_id == thread_id and removed_id != self.uid and author_id != self.uid:
            log.info("{} got removed. They will be re-added".format(removed_id))
            self.addUsersToGroup(removed_id, thread_id=thread_id)
            
client = KeepBot("email", "pass")
client.listen()
