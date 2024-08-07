def membaca(nama_file):
    with open(nama_file, "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def menulis(nama_file):

    nama_anime = input("list top hero terhewan: ")
    text = "\n {}".format(nama_anime)

    membaca("file.txt")

    with open(nama_file, "a") as file_anime:
        file_anime.write(text)

menulis("file.txt")