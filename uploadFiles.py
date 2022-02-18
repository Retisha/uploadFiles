import os
import dropbox


class transferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(relative_path, file_to)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(dropbox_path, f.read(),
                                     mode=WriteMode('overwrite'))


def main():
    access_token = 'MLpAwF_nsk8AAAAAAAAAAackKS3ko4TPCCSzlbDLoYNKAxqIsOL8a4hm9vxT_iAP'
    transferData = transferData(access_token)
    file_from = str(input('Please enter the folder path to transfer-'))
    file_to = input('Please enter the full path to upload to dropbox')
    transferData.upload_file(file_from, file_to)
    print('Your file has been moved successfully')


main()
