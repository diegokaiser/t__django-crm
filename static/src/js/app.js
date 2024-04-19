const app = []

app.utils = {
  mediaMatch: () => {
    const windowWidth = window.matchMedia("(min-width: 400ox)")
    return windowWidth.matches
  }
}

app.home = {
  init: () => {
    console.log('Developed with ♥')
  },
  header: () => {
    if (!app.utils.mediaMatch()) {
      let scrollPosition = window.scrollY
      const header = document.querySelector('.header')
      window.addEventListener('scroll', () => {
        scrollPosition = window.scrollY
        if (scrollPosition >= 160) {
          header.classList.add('scrolled')
        } else {
          header.classList.remove('scrolled')
        }
      })
    }
  },
  search: () => {
    if (!app.utils.mediaMatch()) {
      const onClickSearchByProduct = document.querySelector('.js-searchByProduct')
      const onClickSearchByKeyword = document.querySelector('.js-searchByKeyword')
      const searchByProduct = document.querySelector('.search__byProduct')
      const searchByKeyword = document.querySelector('.search__byKeyword')

      onClickSearchByProduct.addEventListener('click', (event) => {
        onClickSearchByProduct.classList.add('active')
        onClickSearchByKeyword.classList.remove('active')
        searchByProduct.classList.add('active')
        searchByKeyword.classList.remove('active')
      })
      onClickSearchByKeyword.addEventListener('click', (event) => {
        onClickSearchByKeyword.classList.add('active')
        onClickSearchByProduct.classList.remove('active')
        searchByProduct.classList.remove('active')
        searchByKeyword.classList.add('active')
      })
    }
  }
}
window.addEventListener('load', () => {
  app.home.init()
  app.home.header()
  app.home.search()
})

