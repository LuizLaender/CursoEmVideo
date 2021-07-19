function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    //var hora = 12
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        //bom dia
        img.src = "fotos/manhã.png"
        document.body.style.background = '#fe9901'
    }
    else if (hora >= 12 && hora < 18) {
        //boa tarde
        img.src = "fotos/tarde.png"
        document.body.style.background = '#dcbea2'
    }
    else {
        //boa noite
        img.src = "fotos/noite.png"
        document.body.style.background = '#03314d'
    }
}
