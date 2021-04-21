function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.querySelector('input#txtano')
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano){
        alert('[ERRO] Verifique os dados e tente novamente')
    }
    else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')

        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 12) {
                //criança
                img.setAttribute('src', 'fotos/kidM.png')
            } 
            else if (idade < 21) {
                //jovem
                img.setAttribute('src', 'fotos/teenM.png')
            }
            else if (idade < 50) {
                //adulto
                img.setAttribute('src', 'fotos/adultM.png')
            }
            else if (idade < 80) {
                //idoso
                img.setAttribute('src', 'fotos/oldM.png')
            }
            else {
                //morto
                img.setAttribute('src', 'fotos/death.png')
            }
        }
        else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 12) {
                //criança
                img.setAttribute('src', 'fotos/kidF.png')
            } 
            else if (idade < 21) {
                //jovem
                img.setAttribute('src', 'fotos/teenF.png')
            }
            else if (idade < 50) {
                //adulto
                img.setAttribute('src', 'fotos/adultF.png')
            }
            else if (idade < 80) {
                //idoso
                img.setAttribute('src', 'fotos/oldF.png')
            }
            else {
                //morto
                img.setAttribute('src', 'fotos/death.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `${genero} com ${idade} anos`
        res.appendChild(img)
    }

}
