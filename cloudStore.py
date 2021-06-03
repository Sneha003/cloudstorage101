import dropbox
 
class transferdata:
    def __init__(self,accesstoken) :
        self.accesstoken=accesstoken

    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        with open(filefrom,'rb')as f:
            dbx.files_upload(f.read(),fileto)

def cloud ():
    accesstoken="ZhF8ZWT4ak4AAAAAAAAAAXQfNIrPsdaaCDEOkH7KYSnISri1v5GJavIlIlHJ6RrK"   
    transferfile=transferdata(accesstoken)  
    filefrom=input('enter the file name to upload: ')   
    fileto=input('enter the file name with app name: ')

    transferfile.uploadfile(filefrom,fileto) 
    print('file uploaded successfully to drop box')

cloud()

