/* 
  아래에 코드를 작성해주세요.
*/

const searchInput = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')


const fetchAlbums = async (page, limit) => {
  
  searchResult.replaceChildren()

  const keyword = searchInput.value
  
  try {
    const API_KEY = '9f6016e2207406e446de92a31485beb5'
    const API_URL = 'http://ws.audioscrobbler.com/2.0/?method=album.search&format=json'
    const params = {
      api_key: API_KEY,
      album: keyword,
      page: 1,
      limit: 20,
    }
    const res = await axios.get(API_URL, {params})
    // console.log(res)
  
    const albums = res.data.results.albummatches.album
    console.log(albums)

    if (albums.length == 0) {
      searchResult.textContent = `"${keyword}"`
      const spanTag = document.createElement('span')
      spanTag.textContent = '에 대한 검색 결과가 없습니다.'
      spanTag.style.color = 'grey'
      searchResult.appendChild(spanTag)
    }

    albums.forEach((album) => {
      const card = document.createElement('div')
      card.classList.add('search-result__card')
      
      const cardImg = document.createElement('img')
      cardImg.src = album.image[0]['#text'] ? album.image[0]['#text'] : './assets/default.png'

      const title = document.createElement('p')
      title.textContent = album.name

      const artist = document.createElement('h2')
      artist.textContent = album.artist

      const cardText = document.createElement('div')
      cardText.classList.add('search-result__text')

      cardText.appendChild(artist)
      cardText.appendChild(title)

      card.appendChild(cardImg)
      card.appendChild(cardText)

      searchResult.appendChild(card)
    });
  } catch {
    alert('잠시 후 다시 시도해주세요')
  }

  searchInput.value = ''
}

searchBtn.addEventListener('click', fetchAlbums)
searchInput.addEventListener('keydown', function (e) {
  if (e.keyCode === 13) {
    fetchAlbums()
  }
})