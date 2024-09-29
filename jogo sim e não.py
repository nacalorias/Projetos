print('Você está em uma floresta e existem apenas dois caminhos para seguir.')
print('O caminho da esquerda leva a um rio, o da direita leva a uma montanha.')
caminho = input('Digite esquerda se deseja ir para o rio e direita se deseja ir para a montanha: ')

if caminho == 'esquerda':
    print('Você encontrou um belo rio!')
    escolha = input('Você deseja atravessar esse rio? Digite sim ou não: ')
    if escolha == 'sim':
        print('Você atravessou o rio e encontrou um baú de tesouro!!!')
    elif escolha == 'não':
        print('Poxa, você não atravessou o rio e voltou para casa sem um baú de tesouro!')
        voltar = input('No meio do caminho você encontra um mago, deseja conversar com ele? (sim/não): ')
        if voltar == 'sim':
            print('Ele te oferece um livro misterioso, você aceita?')
            aceitarLivro = input("Digite sim se deseja aceitar o livro do mago: ")
            if aceitarLivro == 'sim':
                print('Parabéns!! Você ganhou um livro de poderes mágicos')
            elif aceitarLivro == 'não':
                print('Poxa, você perdeu a oportunidade de invocar poderes mágicos :( ')
        elif voltar == 'não':
            print('O mago ficou chateado com você e lançou um feitiço te transformando em um rato!')
            print('Fim de jogo!')

if caminho == 'direita':
    print("Você encontrou uma bela montanha!")
    vaiSubir = input("Você deseja subir essa montanha? Digite sim ou não: ")
    if vaiSubir == 'sim':
        print('Enquanto você sobe a montanha encontra uma caverna escura e úmida.')
        caverna = input('Deseja explora-la?')
        if caverna == 'sim':
            print("A entrada da caverna é muito escura, mas ao decorrer do caminho você encontra uma gruta de diamantes!!")
        elif caverna == 'não':
            print('Você continua a sua jornada até o topo da montanha.')
    print('Você chega ao topo da montanha e aprecia uma bela vista do por do sol!')
    descer = input('Uma águia colossal te oferece ajuda para descer a montanha à noite, você aceita? ')
    if descer == 'sim':
        print("A águia não só te ajuda a descer a montanha como te leva até a sua casa, vocês viraram grandes amigos!! ")
    elif descer == 'não':
        print('Que azar!! águia ficou furiosa por você recusar sua ajuda e o raptou para ser alimento para seus filhotes gigantes.')
        print('Fim de Jogo!')

    elif vaiSubir == 'não':
        print('Você não subiu a montanha e decidiu voltar para a casa.')
        gnomo = input('No caminho de casa você encontra um gnomo, ele deseja conversar, você aceita? ')

        if gnomo == 'sim':
            print('Ele te oferece uma poção mágica que promete o saber dos mistérios intergalácticos!')
            aceitarPocao = input('Você aceita essa poção mágica? ')
            if aceitarPocao == 'sim':
                print('Você tomou a poção do saber e agora tem consciência de todas as verdades do universo, aprenda a lidar com isso!!')
            elif aceitarPocao == 'não':
                print('Você não aceitou a poção, mas agradeceu a oferta do gnomo.')

        if gnomo == 'não':
            print('Ele ficou chateado e começou a te perseguir loucamente. Fuja o mais rápido que pode!!')
            fuga = input('Enquanto você corre precisa escolher quais caminhos seguir, direita ou esquerda? ')
            if fuga == 'direita':
                print('Infelizmente tinha um buraco gigante no chão, o gnomo consegue te capturar e agora você é obrigado a conviver com os seres místicos florestais!')
                print('Fim de jogo!')
            elif fuga == 'esquerda':
                print('Você encontrou um atalho e despistou o gnomo. Ufa! Essa foi por pouco, agora você pode voltar para casa em paz!')
