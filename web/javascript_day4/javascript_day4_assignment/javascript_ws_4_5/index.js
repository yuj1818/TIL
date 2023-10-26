// 코드를 작성해 주세요
const scissor = document.querySelector('#scissors-button')
const rock = document.querySelector('#rock-button')
const paper = document.querySelector('#paper-button')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')

const countA = document.querySelector('.countA')
const countB = document.querySelector('.countB')

modal.addEventListener('click', e => {
    modal.style.display = 'none'

    scissor.disabled = false
    rock.disabled = false
    paper.disabled = false
})

function play (player1, player2) {
    let winner = ''
    if (player1 == 'scissors') {
        if (player2 == 'rock') {
            winner = 'player2'
        } else if (player2 == 'paper') {
            winner = 'player1'
        }
    } else if (player1 == 'rock') {
        if (player2 == 'paper') {
            winner = 'player2'
        } else if (player2 == 'scissors') {
            winner = 'player1'
        }
    } else {
        if (player2 == 'scissors') { 
            winner = 'player2'
        } else if (player2 == 'rock') {
            winner = 'player1'
        }
    }

    if (winner == 'player1') {
        countA.textContent = parseInt(countA.textContent) + 1
    } else if (winner == 'player2') {
        countB.textContent = parseInt(countB.textContent) + 1
    }
    return winner
}

function choose (e) {
    const player1Choice = e.currentTarget.id.replace('-button', '')
    const player1Img = document.querySelector('#player1-img')
    player1Img.src = `./img/${player1Choice}.png`

    scissor.disabled = true
    rock.disabled = true
    paper.disabled = true

    const player2Img = document.querySelector('#player2-img')
    const choices = ['scissors', 'rock', 'paper']

    let i = 0
    const changeImg = setInterval(function() {
        player2Img.src = `./img/${choices[i%3]}.png`
        i += 1
    }, 100)

    setTimeout(function() {
        clearTimeout(changeImg)
        const player2Choice = choices[Math.floor(Math.random() * 3)]
        // console.log(player2Choice)
        player2Img.src = `./img/${player2Choice}.png`

        winner = play(player1Choice, player2Choice)
        
        if (winner) {
            modalContent.textContent = `${winner}의 승리입니다!`
        } else {
            modalContent.textContent = '무승부입니다!'
        }
        
        modal.style.display = 'flex'
    }, 3000)
}

scissor.addEventListener('click', choose)
rock.addEventListener('click', choose)
paper.addEventListener('click', choose)