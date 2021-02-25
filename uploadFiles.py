import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ar7solFKFMu16Qu9JC2k-_iLKfi86Nqid5aXMYIV6_gCx4Baqj5FSOvkLtWekfEFp7Er6eqYU0Y_2qT1Z1-P861nGvtkyzD0eHJ52vzlAFD3UUuE8zPy3t7ffbkkFZ6c2fL02pE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("Enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()  
