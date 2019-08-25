from tesserocr import PyTessBaseAPI
from PIL import Image
from underthesea import sent_tokenize
from underthesea import word_tokenize



column = Image.open('sample1.png')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
blackwhite.save("code_bw.jpg")
images = ['sample1.png', 'sample2.png']


my_file = open('data.py', 'w')
with PyTessBaseAPI(path='C:/Users/DELL/Downloads/tesserocr-master/tessdata/.', lang='eng') as api:
    
    for img in images:
        api.SetImageFile(img)
        text = api.GetUTF8Text()
        print(api.GetUTF8Text())
        # print(api.AllWordConfidences())
        my_file.write(text)

my_file.close()

data_file = open('data.py', 'r')
data = data_file.read().splitlines()
print(data)

data_2 = []
for sentence in data:
    if sentence.find('NOTE') != -1 or sentence.find('PART') != -1:
        del sentence
    elif sentence.startswith('('):
        del sentence
    else:
        if sentence.find(':') != -1:
            a = sentence.split(':')
            print(a)

            if a[1] == '':
                data_2.append(a[0])
            else:
                data_2 += a

print(data_2)

for sentence in data_2:
    if sentence == '':
        del sentence  
    else:
        sentence = sentence.strip()
        print(sentence)

data_file.close()


