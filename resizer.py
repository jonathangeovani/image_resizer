from PIL import Image

basewidth = int(input('Largura final desejada para as imagens: '))
path = input('Escreva o caminho completo para a pasta com as fotos: ')
total = int(input('Total de fotos que serão redimensionadas: '))
name = input('Nome das imagens sem o número: ')
format = input('Formato das imagens: ')
count = 0

while count <= (total-1):
    img = Image.open(f'{path}{name}{count}.{format}')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    img.save(f'{path}{count}.{format}')
    count += 1