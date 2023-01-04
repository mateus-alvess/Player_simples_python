from pygame import mixer

print('musicas')
print('1 = Alfons - Corona (City Of Wuhan).mp3')
print('2 = Alfons - Ganjaman.mp3 ')
print('3 = Alfons - Jamrock Land.mp3')
print('4 = Bassjackers & Jay Hardway - El Mariachi (Official Music Video).mp3 ')
print('5 = Breaking Beattz - American Boy (Extended Mix).mp3')
print('6 = Breaking Beattz - Plan B (Lyric Video).mp3')
print('7 = Husman x Jaxx & Vega - Venom (Official Audio).mp3')
print('8 = Jason Mraz - 93 Million Miles (Official Video).mp3')
print('9 = Menumas - Energy.mp3')
print('10 = Pitty - Na Sua Estante (Ao Vivo)   Matriz Ao Vivo na Bahia.mp3')

x = input('QUAL musica DESEJA ESCUTAR? (digite 0 caso não queira escutar mais musicas) = ')


while x != '0':
    if x == '1':
        mixer.init()
        mixer.music.load('Alfons - Corona (City Of Wuhan).mp3')
        mixer.music.play()

    elif x == '2':
        mixer.init()
        mixer.music.load('Alfons - Ganjaman.mp3')
        mixer.music.play()

    elif x == '3':
        mixer.init()
        mixer.music.load('Alfons - Jamrock Land.mp3')
        mixer.music.play()

    elif x == '4':
        mixer.init()
        mixer.music.load('Bassjackers & Jay Hardway - El Mariachi (Official Music Video).mp3')
        mixer.music.play()

    elif x == '5':
        mixer.init()
        mixer.music.load('Breaking Beattz - American Boy (Extended Mix).mp3')
        mixer.music.play()

    elif x == '6':
        mixer.init()
        mixer.music.load('Breaking Beattz - Plan B (Lyric Video).mp3')
        mixer.music.play()

    elif x == '7':
        mixer.init()
        mixer.music.load('Husman x Jaxx & Vega - Venom (Official Audio).mp3')
        mixer.music.play()

    elif x == '8':
        mixer.init()
        mixer.music.load('Jason Mraz - 93 Million Miles (Official Video).mp3')
        mixer.music.play()

    elif x == '9':
        mixer.init()
        mixer.music.load('Menumas - Energy.mp3')
        mixer.music.play()
    elif x == '10':
        mixer.init()
        mixer.music.load('Pitty - Na Sua Estante (Ao Vivo)   Matriz Ao Vivo na Bahia.mp3')
        mixer.music.play()
    x = input('deseja escutar outra musica? = ')
