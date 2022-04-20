from gtts import gTTS
import base64
from src import logger

class Helper:
    def __init__(self):
        self.file_object = open("Logs/embedding_log.txt", 'a+')
        self.log_writer = logger.App_Logger()
        
        
    def text2Speech(self, data):
        try:
            my_text = data
            tts = gTTS(text=my_text, lang='en', slow=False)
            tts.save('converted-file.mp3')  # save file as ... (here saving as mp3)
            with open("converted-file.mp3", "rb") as file:
                my_string = base64.b64encode(file.read())
            return my_string
        
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the vectorize function. Error:: %s' % ex)
            raise ex
